import { evaluateFormula, parseStringParameter } from '../formulaEvaluator';

describe('formulaEvaluator', () => {
  describe('parseStringParameter', () => {
    it('should parse numeric strings to numbers', () => {
      expect(parseStringParameter('42')).toBe(42);
      expect(parseStringParameter('3.14')).toBe(3.14);
      expect(parseStringParameter('-1')).toBe(-1);
    });

    it('should parse boolean strings to booleans', () => {
      expect(parseStringParameter('true')).toBe(true);
      expect(parseStringParameter('false')).toBe(false);
    });

    it('should return string values as is', () => {
      expect(parseStringParameter('hello')).toBe('hello');
      expect(parseStringParameter('')).toBe('');
    });
  });

  describe('evaluateFormula', () => {
    it('should handle simple multiplication formulas', () => {
      const formula = '[StreamType.audio] * int(inputs)';
      const params = { inputs: 3 };
      const result = evaluateFormula(formula, params);
      expect(result).toHaveLength(3);
      expect(result.every((r) => r.type.value === 'audio')).toBe(true);
    });

    it('should handle conditional formulas', () => {
      const formula = '[StreamType.video] + ([StreamType.audio] if audio else [])';
      const params = { audio: true };
      const result = evaluateFormula(formula, params);
      expect(result).toHaveLength(2);
      expect(result[0].type.value).toBe('video');
      expect(result[1].type.value).toBe('audio');
    });

    it('should handle string-based calculations', () => {
      const formula = '[StreamType.video] * len(streams.split("+"))';
      const params = { streams: '1+2+3' };
      const result = evaluateFormula(formula, params);
      expect(result).toHaveLength(3);
      expect(result.every((r) => r.type.value === 'video')).toBe(true);
    });

    it('should handle channel layout formulas', () => {
      const formula = '[StreamType.audio] * CHANNEL_LAYOUT[str(channel_layout)]';
      const params = { channel_layout: 'stereo' };
      const result = evaluateFormula(formula, params);
      expect(result).toHaveLength(2);
      expect(result.every((r) => r.type.value === 'audio')).toBe(true);
    });

    it('should handle complex formulas with multiple operations', () => {
      const formula = '([StreamType.video]*int(v) + [StreamType.audio]*int(a))*int(n)';
      const params = { v: 2, a: 1, n: 2 };
      const result = evaluateFormula(formula, params);
      expect(result).toHaveLength(6); // (2 video + 1 audio) * 2
      expect(result.filter((r) => r.type.value === 'video')).toHaveLength(4);
      expect(result.filter((r) => r.type.value === 'audio')).toHaveLength(2);
    });

    it('should return empty array for invalid formulas', () => {
      const formula = 'invalid formula';
      const params = {};
      const result = evaluateFormula(formula, params);
      expect(result).toHaveLength(0);
    });

    it('should handle null or undefined formulas', () => {
      expect(evaluateFormula(null, {})).toHaveLength(0);
      expect(evaluateFormula(undefined, {})).toHaveLength(0);
    });
  });
});
