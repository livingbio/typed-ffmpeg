import { describe, expect, it, beforeEach } from 'vitest';
import { dumps, loads, Serializable, serializable, clearClassRegistry } from '../serialize';
import { StreamType } from '../../types/dag';

// Test classes
@serializable
class TestNode extends Serializable {
  constructor(
    public name: string,
    public value: number,
    public children: TestNode[] = []
  ) {
    super();
  }
}

@serializable
class ComplexNode extends Serializable {
  constructor(
    public name: string,
    public data: {
      numbers: number[];
      strings: string[];
      nested: {
        key: string;
        value: number;
      };
    },
    public type: StreamType = StreamType.video
  ) {
    super();
  }
}

describe('Serialization System', () => {
  beforeEach(() => {
    clearClassRegistry();
  });

  describe('Basic Serialization', () => {
    it('should serialize a simple node', () => {
      const node = new TestNode('test', 42);
      const serialized = dumps(node);

      expect(serialized).toMatchSnapshot();
    });

    it('should serialize a node with children', () => {
      const node = new TestNode('parent', 1, [
        new TestNode('child1', 2),
        new TestNode('child2', 3),
      ]);
      const serialized = dumps(node);

      expect(serialized).toMatchSnapshot();
    });

    it('should serialize a complex node with nested data', () => {
      const node = new ComplexNode('complex', {
        numbers: [1, 2, 3],
        strings: ['a', 'b', 'c'],
        nested: {
          key: 'test',
          value: 42,
        },
      });
      const serialized = dumps(node);

      expect(serialized).toMatchSnapshot();
    });
  });

  describe('Round-trip Conversion', () => {
    it('should deserialize a simple node correctly', () => {
      const original = new TestNode('test', 42);
      const serialized = dumps(original);
      const deserialized = loads(serialized);

      expect(deserialized).toBeInstanceOf(TestNode);
      expect(deserialized.name).toBe(original.name);
      expect(deserialized.value).toBe(original.value);
    });

    it('should deserialize a node with children correctly', () => {
      const original = new TestNode('parent', 1, [
        new TestNode('child1', 2),
        new TestNode('child2', 3),
      ]);
      const serialized = dumps(original);
      const deserialized = loads(serialized);

      expect(deserialized).toBeInstanceOf(TestNode);
      expect(deserialized.name).toBe(original.name);
      expect(deserialized.value).toBe(original.value);
      expect(deserialized.children).toHaveLength(2);
      expect(deserialized.children[0]).toBeInstanceOf(TestNode);
      expect(deserialized.children[0].name).toBe('child1');
      expect(deserialized.children[1].name).toBe('child2');
    });

    it('should deserialize a complex node correctly', () => {
      const original = new ComplexNode('complex', {
        numbers: [1, 2, 3],
        strings: ['a', 'b', 'c'],
        nested: {
          key: 'test',
          value: 42,
        },
      });
      const serialized = dumps(original);
      const deserialized = loads(serialized);

      expect(deserialized).toBeInstanceOf(ComplexNode);
      expect(deserialized.name).toBe(original.name);
      expect(deserialized.data).toEqual(original.data);
      expect(deserialized.type).toBe(original.type);
    });
  });

  describe('Special Types', () => {
    it('should handle Maps correctly', () => {
      const map = new Map([
        ['key1', 'value1'],
        ['key2', 'value2'],
      ]);
      const serialized = dumps(map);
      const deserialized = loads(serialized);

      expect(deserialized).toBeInstanceOf(Map);
      expect(Array.from(deserialized.entries())).toEqual(Array.from(map.entries()));
    });

    it('should handle Sets correctly', () => {
      const set = new Set(['value1', 'value2', 'value3']);
      const serialized = dumps(set);
      const deserialized = loads(serialized);

      expect(deserialized).toBeInstanceOf(Set);
      expect(Array.from(deserialized)).toEqual(Array.from(set));
    });

    it('should handle Dates correctly', () => {
      const date = new Date('2024-01-01T00:00:00Z');
      const serialized = dumps(date);
      const deserialized = loads(serialized);

      expect(deserialized).toBeInstanceOf(Date);
      expect(deserialized.toISOString()).toBe(date.toISOString());
    });
  });

  describe('Error Handling', () => {
    it('should throw error when deserializing unknown class', () => {
      const invalidJson = JSON.stringify({
        __class__: 'NonExistentClass',
        name: 'test',
      });

      expect(() => loads(invalidJson)).toThrow('Class NonExistentClass not registered');
    });

    it('should handle circular references', () => {
      const parent = new TestNode('parent', 1);
      const child = new TestNode('child', 2, [parent]);
      parent.children = [child];

      expect(() => dumps(parent)).not.toThrow();
    });
  });
});
