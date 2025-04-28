import { describe, it, expect, vi } from 'vitest';
import { evaluateFormula, parseStringParameter } from '../formulaEvaluator';
import { PyodideMock } from '../pyodideMock';

// Mock Pyodide
vi.mock('../pyodideMock', () => ({
  PyodideMock: vi.fn().mockImplementation(() => ({
    runPythonAsync: vi.fn().mockImplementation(() => {
      // Mock the Python evaluation result
      return Promise.resolve(JSON.stringify([{ value: 'video' }, { value: 'audio' }]));
    }),
    loadPackage: vi.fn().mockResolvedValue(undefined),
  })),
}));

describe('formulaEvaluator', () => {
  describe('evaluateFormula', () => {
    it('should return empty array for empty formula', async () => {
      const result = await evaluateFormula('', {});
      expect(result).toEqual([]);
    });

    it('should evaluate formula using Python', async () => {
      const result = await evaluateFormula('test_formula', { param1: 'value1' });
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

    it('should handle Python evaluation errors', async () => {
      // Override the mock for this specific test
      const mockPyodide = new PyodideMock();
      vi.mocked(mockPyodide.runPythonAsync).mockRejectedValueOnce(new Error('Python error'));

      // Clear the singleton instance to force a new one
      vi.mocked(PyodideMock).mockImplementationOnce(() => mockPyodide);

      const result = await evaluateFormula('invalid_formula', {});
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
