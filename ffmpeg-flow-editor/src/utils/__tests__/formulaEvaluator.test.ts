import { describe, it, expect, beforeEach } from 'vitest';
import { evaluateFormula, parseStringParameter } from '../formulaEvaluator';
import { setupPyodideMock } from './testUtils';

describe('formulaEvaluator', () => {
  beforeEach(async () => {
    setupPyodideMock();
  });

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
    it('should parse numeric string to number', () => {
      expect(parseStringParameter('123')).toBe(123);
      expect(parseStringParameter('-123')).toBe(-123);
      expect(parseStringParameter('0')).toBe(0);
    });

    it('should parse boolean strings to boolean', () => {
      expect(parseStringParameter('true')).toBe(true);
      expect(parseStringParameter('True')).toBe(true);
      expect(parseStringParameter('false')).toBe(false);
      expect(parseStringParameter('False')).toBe(false);
    });

    it('should return string for non-numeric, non-boolean strings', () => {
      expect(parseStringParameter('hello')).toBe('hello');
      expect(parseStringParameter('')).toBe('');
    });
  });
});
