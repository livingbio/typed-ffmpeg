import { StreamTypeEnum } from '../types/dag';

// ─── Runtime helpers injected into formula evaluation ─────────────────────

const CHANNEL_LAYOUT_MAP: Record<string, number> = {
  mono: 1, stereo: 2, '2.1': 3, '3.0': 3, '3.0(back)': 3,
  '4.0': 4, quad: 4, 'quad(side)': 4, '3.1': 4, '5.0': 5,
  '5.0(side)': 5, '4.1': 5, '5.1': 6, '5.1(side)': 6, '6.0': 6,
  '6.0(front)': 6, hexagonal: 6, '3.1.2.0': 6, '6.1': 7,
  '6.1(back)': 7, '6.1(front)': 7, '7.0': 7, '7.0(front)': 7,
  '7.1': 8, '7.1(wide)': 8, '7.1(wide-side)': 8, octagonal: 8,
  hexadecagonal: 16, downmix: 2,
};

// ─── Python-subset formula parser ─────────────────────────────────────────

/**
 * Transpiles a Python list-expression formula to a JavaScript expression string.
 *
 * Supported Python constructs:
 *  - List literals  [a, b, c]
 *  - List repeat    list * n      →  __repeat(list, n)
 *  - List concat    list + list   →  list.concat(list)
 *  - Ternary        x if c else y →  (c) ? (x) : (y)
 *  - Arithmetic     + - (binary/unary)
 *  - Comparisons    == != < > <= >=
 *  - Logic          and or not    →  && || !
 *  - Functions      int str len max hex
 *  - re module      re.split re.findall
 *  - Method calls   .split() .length etc.
 *  - Subscript      s[n]
 *  - Slice          s[start::step]  →  __slice(s, start, step)
 *  - Raw strings    r'...'
 *  - Boolean atoms  True False None
 *  - CHANNEL_LAYOUT lookup
 */
class PythonExprParser {
  private pos = 0;

  constructor(private src: string) {}

  // ── Entry point ────────────────────────────────────────────────────────

  parse(): string {
    const result = this.parseTernary();
    this.skipWS();
    if (this.pos < this.src.length) {
      throw new Error(`Unexpected token at ${this.pos}: '${this.src.slice(this.pos, this.pos + 10)}'`);
    }
    return result;
  }

  // ── Precedence levels ──────────────────────────────────────────────────

  /** ternary: expr if cond else alt */
  private parseTernary(): string {
    const expr = this.parseOr();
    this.skipWS();
    if (this.matchKeyword('if')) {
      const cond = this.parseOr();
      this.skipWS();
      if (!this.matchKeyword('else')) throw new Error("Expected 'else' in ternary");
      const alt = this.parseTernary();
      return `(${cond}) ? (${expr}) : (${alt})`;
    }
    return expr;
  }

  private parseOr(): string {
    let left = this.parseAnd();
    this.skipWS();
    while (this.matchKeyword('or')) {
      const right = this.parseAnd();
      left = `(${left} || ${right})`;
      this.skipWS();
    }
    return left;
  }

  private parseAnd(): string {
    let left = this.parseNot();
    this.skipWS();
    while (this.matchKeyword('and')) {
      const right = this.parseNot();
      left = `(${left} && ${right})`;
      this.skipWS();
    }
    return left;
  }

  private parseNot(): string {
    this.skipWS();
    if (this.matchKeyword('not')) {
      const operand = this.parseNot();
      return `!(${operand})`;
    }
    return this.parseComparison();
  }

  private parseComparison(): string {
    let left = this.parseAdd();
    this.skipWS();
    while (true) {
      let op: string;
      if (this.match('==')) op = '===';
      else if (this.match('!=')) op = '!==';
      else if (this.match('<=')) op = '<=';
      else if (this.match('>=')) op = '>=';
      else if (this.match('<')) op = '<';
      else if (this.match('>')) op = '>';
      else break;
      this.skipWS();
      const right = this.parseAdd();
      left = `(${left} ${op} ${right})`;
      this.skipWS();
    }
    return left;
  }

  private parseAdd(): string {
    let left = this.parseMul();
    this.skipWS();
    while (true) {
      if (this.match('+')) {
        this.skipWS();
        const right = this.parseMul();
        // Use .concat() for array addition; works for numbers too since
        // both sides in these formulas are always arrays.
        left = `(${left}).concat(${right})`;
        this.skipWS();
      } else if (this.match('-')) {
        this.skipWS();
        const right = this.parseMul();
        left = `(${left} - ${right})`;
        this.skipWS();
      } else {
        break;
      }
    }
    return left;
  }

  private parseMul(): string {
    let left = this.parseUnary();
    this.skipWS();
    while (this.match('*')) {
      this.skipWS();
      const right = this.parseUnary();
      // All * in these formulas is list repetition
      left = `__repeat(${left}, ${right})`;
      this.skipWS();
    }
    return left;
  }

  private parseUnary(): string {
    this.skipWS();
    if (this.match('-')) {
      const operand = this.parsePostfix();
      return `-(${operand})`;
    }
    return this.parsePostfix();
  }

  /** Handle postfix operations: subscript, slice, method/attribute access */
  private parsePostfix(): string {
    let expr = this.parsePrimary();
    while (true) {
      this.skipWS();
      if (this.current() === '.') {
        this.pos++;
        const name = this.readIdent();
        this.skipWS();
        if (this.current() === '(') {
          const args = this.parseCallArgs();
          expr = `${expr}.${name}(${args})`;
        } else {
          expr = `${expr}.${name}`;
        }
      } else if (this.current() === '[') {
        this.pos++; // skip '['
        this.skipWS();
        if (this.current() === ':') {
          // slice starting at 0: [::step]
          this.pos++; // first ':'
          if (this.current() === ':') {
            this.pos++; // second ':'
            const step = this.parseAdd();
            this.skipWS();
            this.consume(']');
            expr = `__slice(${expr}, 0, ${step})`;
          } else {
            const end = this.parseAdd();
            this.skipWS();
            this.consume(']');
            expr = `${expr}.slice(0, ${end})`;
          }
        } else {
          const start = this.parseAdd();
          this.skipWS();
          if (this.current() === ':') {
            this.pos++; // skip ':'
            this.skipWS();
            if (this.current() === ':') {
              // [start::step]
              this.pos++; // skip second ':'
              const step = this.parseAdd();
              this.skipWS();
              this.consume(']');
              expr = `__slice(${expr}, ${start}, ${step})`;
            } else if (this.current() === ']') {
              this.consume(']');
              expr = `${expr}.slice(${start})`;
            } else {
              const end = this.parseAdd();
              this.skipWS();
              this.consume(']');
              expr = `${expr}.slice(${start}, ${end})`;
            }
          } else {
            this.consume(']');
            expr = `${expr}[${start}]`;
          }
        }
      } else {
        break;
      }
    }
    return expr;
  }

  private parsePrimary(): string {
    this.skipWS();
    const c = this.current();

    // List literal
    if (c === '[') {
      this.pos++; // skip '['
      const items: string[] = [];
      this.skipWS();
      while (this.current() !== ']') {
        items.push(this.parseTernary());
        this.skipWS();
        if (this.current() === ',') { this.pos++; this.skipWS(); }
      }
      this.pos++; // skip ']'
      return `[${items.join(', ')}]`;
    }

    // Parenthesised expression
    if (c === '(') {
      this.pos++; // skip '('
      this.skipWS();
      const inner = this.parseTernary();
      this.skipWS();
      this.consume(')');
      return `(${inner})`;
    }

    // String literal (including raw strings r'...')
    if (c === 'r' && (this.src[this.pos + 1] === '"' || this.src[this.pos + 1] === "'")) {
      this.pos++; // skip 'r'
      return this.parseStringLiteral();
    }
    if (c === '"' || c === "'") {
      return this.parseStringLiteral();
    }

    // Number literal
    if (this.isDigit(c)) {
      return this.readNumber();
    }

    // Identifier, keyword, or function call
    if (this.isIdStart(c)) {
      const name = this.readIdent();
      this.skipWS();
      if (this.current() === '(') {
        const args = this.parseCallArgs();
        return this.mapFunctionCall(name, args);
      }
      return this.mapIdentifier(name);
    }

    throw new Error(`Unexpected char '${c}' at pos ${this.pos} in: ${this.src}`);
  }

  // ── Helpers ────────────────────────────────────────────────────────────

  private parseCallArgs(): string {
    this.pos++; // skip '('
    const args: string[] = [];
    this.skipWS();
    while (this.current() !== ')') {
      args.push(this.parseTernary());
      this.skipWS();
      if (this.current() === ',') { this.pos++; this.skipWS(); }
    }
    this.pos++; // skip ')'
    return args.join(', ');
  }

  private parseStringLiteral(): string {
    const quote = this.src[this.pos];
    this.pos++;
    let s = quote;
    while (this.pos < this.src.length && this.src[this.pos] !== quote) {
      if (this.src[this.pos] === '\\') {
        s += this.src[this.pos] + this.src[this.pos + 1];
        this.pos += 2;
      } else {
        s += this.src[this.pos++];
      }
    }
    this.pos++; // skip closing quote
    return s + quote;
  }

  private readNumber(): string {
    let n = '';
    while (this.pos < this.src.length && (this.isDigit(this.src[this.pos]) || this.src[this.pos] === '.')) {
      n += this.src[this.pos++];
    }
    return n;
  }

  private readIdent(): string {
    let name = '';
    while (this.pos < this.src.length && this.isIdChar(this.src[this.pos])) {
      name += this.src[this.pos++];
    }
    return name;
  }

  /** Map Python identifiers to JS equivalents */
  private mapIdentifier(name: string): string {
    switch (name) {
      case 'True': return 'true';
      case 'False': return 'false';
      case 'None': return 'null';
      case 'StreamType': return 'StreamType'; // handled via mapFunctionCall for attributes
      default: return name;
    }
  }

  /** Map Python function calls to JS equivalents */
  private mapFunctionCall(name: string, args: string): string {
    switch (name) {
      case 'int':   return `Math.floor(Number(${args}))`;
      case 'str':   return `String(${args})`;
      case 'len':   return `__len(${args})`;
      case 'max':   return `__max(${args})`;
      case 'min':   return `__min(${args})`;
      case 'hex':   return `('0x' + Math.floor(Number(${args})).toString(16))`;
      case 'float': return `Number(${args})`;
      case 'abs':   return `Math.abs(${args})`;
      case 'bool':  return `Boolean(${args})`;
      case 'list':  return `Array.from(${args})`;
      // re module handled through attribute access (re.split / re.findall)
      default:      return `${name}(${args})`;
    }
  }

  /** Match and consume an exact string, returning true if found */
  private match(token: string): boolean {
    if (this.src.startsWith(token, this.pos)) {
      this.pos += token.length;
      return true;
    }
    return false;
  }

  /** Match a keyword (must not be followed by an identifier char) */
  private matchKeyword(keyword: string): boolean {
    const end = this.pos + keyword.length;
    if (this.src.startsWith(keyword, this.pos) && !this.isIdChar(this.src[end] ?? '')) {
      this.pos = end;
      this.skipWS();
      return true;
    }
    return false;
  }

  private consume(char: string): void {
    if (this.src[this.pos] !== char) {
      throw new Error(`Expected '${char}' at pos ${this.pos}, got '${this.src[this.pos]}'`);
    }
    this.pos++;
  }

  private current(): string { return this.src[this.pos] ?? ''; }

  private skipWS(): void {
    while (this.pos < this.src.length && /[ \t\n]/.test(this.src[this.pos])) this.pos++;
  }

  private isDigit(c: string): boolean { return c >= '0' && c <= '9'; }
  private isIdStart(c: string): boolean { return /[a-zA-Z_]/.test(c); }
  private isIdChar(c: string): boolean { return /[a-zA-Z0-9_]/.test(c); }
}

// ─── Runtime helpers available inside evaluated formulas ──────────────────

const FORMULA_RUNTIME = `
  "use strict";

  // List/array repeat: ['video'] * 3  →  __repeat(['video'], 3)
  function __repeat(arr, n) {
    n = Math.max(0, Math.floor(Number(n) || 0));
    if (!Array.isArray(arr)) arr = [arr];
    const result = [];
    for (let i = 0; i < n; i++) result.push(...arr);
    return result;
  }

  // Python-style slice with step: s[start::step]
  function __slice(s, start, step) {
    s = String(s);
    step = Math.max(1, Math.floor(Number(step)));
    const result = [];
    for (let i = start; i < s.length; i += step) result.push(s[i]);
    return result.join('');
  }

  // len() works on strings and arrays
  function __len(x) {
    if (Array.isArray(x)) return x.length;
    if (x == null) return 0;
    return String(x).length;
  }

  // max() behaves like Python's max() — works on strings and numbers
  function __max(...args) {
    const flat = args.flat();
    if (flat.length === 0) return 0;
    if (flat.length === 1 && typeof flat[0] === 'string') {
      // max over characters of a string
      return flat[0].split('').reduce(function(a, b) { return a > b ? a : b; });
    }
    return flat.reduce(function(a, b) {
      return Number(a) >= Number(b) ? a : b;
    });
  }

  function __min(...args) {
    const flat = args.flat();
    if (flat.length === 0) return 0;
    return flat.reduce(function(a, b) {
      return Number(a) <= Number(b) ? a : b;
    });
  }

  // StreamType namespace (these appear as attribute access StreamType.video etc.)
  const StreamType = { video: 'video', audio: 'audio' };

  // re module
  const re = {
    split: function(pattern, text) {
      return String(text).split(new RegExp(pattern));
    },
    findall: function(pattern, text) {
      return String(text).match(new RegExp(pattern, 'g')) || [];
    },
  };

  // CHANNEL_LAYOUT lookup
  const CHANNEL_LAYOUT = new Proxy({}, {
    get: function(_, key) {
      const m = ${JSON.stringify(CHANNEL_LAYOUT_MAP)};
      return m[String(key)] !== undefined ? m[String(key)] : 2;
    }
  });
`;

// ─── Caches (module-level) ─────────────────────────────────────────────────

// formulas come from filters.json — a fixed, finite set — so unbounded caches are fine
const _exprCache = new Map<string, string>();
// eslint-disable-next-line @typescript-eslint/no-unsafe-function-type
const _fnCache = new Map<string, Function>();

// ─── Public API ────────────────────────────────────────────────────────────

/**
 * Evaluate a Python-syntax stream-type formula with the given parameters.
 *
 * @param formula  A Python list-expression string, e.g. "[StreamType.video] * int(inputs)"
 * @param parameters  Key-value map of filter option values
 * @returns Array of StreamTypeEnum values
 */
export async function evaluateFormula(
  formula: string,
  parameters: Record<string, string | number | boolean>,
): Promise<StreamTypeEnum[]> {
  if (!formula.trim()) throw new Error('Empty formula');

  // Transpile once per unique formula string (formulas are static filter metadata)
  let jsExpr = _exprCache.get(formula);
  if (jsExpr === undefined) {
    jsExpr = new PythonExprParser(formula).parse();
    _exprCache.set(formula, jsExpr);
  }

  // Compile Function once per (formula, param-key-set) combination
  const paramKeys = Object.keys(parameters);
  const fnKey = `${formula}\0${paramKeys.join(',')}`;
  let fn = _fnCache.get(fnKey);
  if (!fn) {
    fn = new Function(...paramKeys, FORMULA_RUNTIME + `\nreturn (${jsExpr});`);
    _fnCache.set(fnKey, fn);
  }

  const result: unknown = fn(...paramKeys.map((k) => parameters[k]));

  if (!Array.isArray(result)) {
    throw new Error(`Formula '${formula}' returned non-array: ${String(result)}`);
  }
  return result.flat() as StreamTypeEnum[];
}

// ─── Helper for string parameter parsing ──────────────────────────────────

/** Parse a string UI value to its most appropriate JS type. */
export function parseStringParameter(value: string): string | number | boolean {
  if (value === '') return '';
  if (!isNaN(Number(value))) return Number(value);
  if (value.toLowerCase() === 'true') return true;
  if (value.toLowerCase() === 'false') return false;
  return value;
}
