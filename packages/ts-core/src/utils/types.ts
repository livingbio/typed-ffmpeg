/**
 * Sentinel types for default and auto-computed values.
 *
 * Default represents a value that FFmpeg should use its built-in default for.
 * Auto represents a value computed dynamically based on context.
 */

/**
 * Represents a default value for an FFmpeg option.
 * When a parameter is marked with Default, it will not be explicitly passed
 * to FFmpeg, letting FFmpeg use its built-in default.
 */
export class Default {
  readonly _brand = "Default" as const;

  constructor(readonly value: string) {}

  toString(): string {
    return this.value;
  }
}

/**
 * Represents an automatically derived value for an FFmpeg option.
 * The value is calculated based on context (e.g., number of input streams).
 */
export class Auto extends Default {
  readonly _brand2 = "Auto" as const;
}

/** Type guard for Default values. */
export function isDefault(v: unknown): v is Default {
  return v instanceof Default;
}

/** Type guard for Auto values. */
export function isAuto(v: unknown): v is Auto {
  return v instanceof Auto;
}
