import { describe, it, expect } from 'vitest';
import { evaluateFormula, parseStringParameter } from '../formulaEvaluator';

describe('formulaEvaluator', () => {
  describe('evaluateFormula', () => {
    it('should return empty array for empty formula', async () => {
      const result = await evaluateFormula('', {});
      expect(result).toEqual([]);
    });

    it('should evaluate simple formula with video and audio', async () => {
      const result = await evaluateFormula('[StreamType.video] + [StreamType.audio]', {});
      expect(result).toEqual([
        {
          __class__: 'FFMpegIOType',
          name: '',
          type: {
            __class__: 'StreamType',
            value: 'video',
          },
        },
        {
          __class__: 'FFMpegIOType',
          name: '',
          type: {
            __class__: 'StreamType',
            value: 'audio',
          },
        },
      ]);
    });

    it('should evaluate formula with numeric multiplication', async () => {
      const result = await evaluateFormula('[StreamType.video] * int(inputs)', { inputs: 2 });
      expect(result).toEqual([
        {
          __class__: 'FFMpegIOType',
          name: '',
          type: {
            __class__: 'StreamType',
            value: 'video',
          },
        },
        {
          __class__: 'FFMpegIOType',
          name: '',
          type: {
            __class__: 'StreamType',
            value: 'video',
          },
        },
      ]);
    });

    it('should evaluate formula with string splitting', async () => {
      const result = await evaluateFormula('[StreamType.video] * len("1+2+3".split("+"))', {});
      expect(result).toEqual([
        {
          __class__: 'FFMpegIOType',
          name: '',
          type: {
            __class__: 'StreamType',
            value: 'video',
          },
        },
        {
          __class__: 'FFMpegIOType',
          name: '',
          type: {
            __class__: 'StreamType',
            value: 'video',
          },
        },
        {
          __class__: 'FFMpegIOType',
          name: '',
          type: {
            __class__: 'StreamType',
            value: 'video',
          },
        },
      ]);
    });

    it('should evaluate formula with hex conversion', async () => {
      const result = await evaluateFormula(
        '[StreamType.video] * int(max(hex(int(mapping))[2::2]))',
        { mapping: 0x123 }
      );
      expect(result).toEqual([
        {
          __class__: 'FFMpegIOType',
          name: '',
          type: {
            __class__: 'StreamType',
            value: 'video',
          },
        },
        {
          __class__: 'FFMpegIOType',
          name: '',
          type: {
            __class__: 'StreamType',
            value: 'video',
          },
        },
        {
          __class__: 'FFMpegIOType',
          name: '',
          type: {
            __class__: 'StreamType',
            value: 'video',
          },
        },
      ]);
    });

    it('should evaluate formula with conditional reference', async () => {
      const result = await evaluateFormula(
        '[StreamType.video, StreamType.video] + ([StreamType.video] if reference else [])',
        { reference: 'True' }
      );
      expect(result).toEqual([
        {
          __class__: 'FFMpegIOType',
          name: '',
          type: {
            __class__: 'StreamType',
            value: 'video',
          },
        },
        {
          __class__: 'FFMpegIOType',
          name: '',
          type: {
            __class__: 'StreamType',
            value: 'video',
          },
        },
        {
          __class__: 'FFMpegIOType',
          name: '',
          type: {
            __class__: 'StreamType',
            value: 'video',
          },
        },
      ]);
    });

    it('should evaluate formula with conditional inplace', async () => {
      const result = await evaluateFormula(
        '[StreamType.video] + ([StreamType.video] if inplace else [])',
        { inplace: 'True' }
      );
      expect(result).toEqual([
        {
          __class__: 'FFMpegIOType',
          name: '',
          type: {
            __class__: 'StreamType',
            value: 'video',
          },
        },
        {
          __class__: 'FFMpegIOType',
          name: '',
          type: {
            __class__: 'StreamType',
            value: 'video',
          },
        },
      ]);
    });

    it('should evaluate formula with mixed audio and video', async () => {
      const result = await evaluateFormula(
        '[StreamType.video]*int(v) + [StreamType.audio]*int(a)',
        { v: 2, a: 1 }
      );
      expect(result).toEqual([
        {
          __class__: 'FFMpegIOType',
          name: '',
          type: {
            __class__: 'StreamType',
            value: 'video',
          },
        },
        {
          __class__: 'FFMpegIOType',
          name: '',
          type: {
            __class__: 'StreamType',
            value: 'video',
          },
        },
        {
          __class__: 'FFMpegIOType',
          name: '',
          type: {
            __class__: 'StreamType',
            value: 'audio',
          },
        },
      ]);
    });

    it('should handle Python evaluation errors', async () => {
      const result = await evaluateFormula('[StreamType.invalid]', {});
      expect(result).toEqual([]);
    });
  });

  describe('parseStringParameter', () => {
    it('should parse numeric values', () => {
      expect(parseStringParameter('42')).toBe(42);
      expect(parseStringParameter('3.14')).toBe(3.14);
    });

    it('should parse boolean values', () => {
      expect(parseStringParameter('true')).toBe(true);
      expect(parseStringParameter('false')).toBe(false);
    });

    it('should return string for non-numeric, non-boolean values', () => {
      expect(parseStringParameter('hello')).toBe('hello');
      expect(parseStringParameter('123abc')).toBe('123abc');
    });
  });
});
