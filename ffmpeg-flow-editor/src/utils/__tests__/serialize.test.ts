import { describe, it, expect, beforeEach } from 'vitest';
import { Serializable, registerClasses, clearClassRegistry, dumps, loads } from '../serialize';

// Test class for serialization
class TestClass extends Serializable {
  constructor(
    public name: string,
    public value: number,
    public nested?: TestClass
  ) {
    super();
  }
}

describe('Serialization Utilities', () => {
  beforeEach(() => {
    clearClassRegistry();
  });

  describe('Serializable', () => {
    it('should serialize class instance to JSON', () => {
      const instance = new TestClass('test', 42);
      const json = instance.toJSON();

      expect(json).toEqual({
        name: 'test',
        value: 42,
        nested: undefined,
        __class__: 'TestClass',
      });
    });

    it('should handle nested serializable objects', () => {
      const nested = new TestClass('nested', 24);
      const instance = new TestClass('parent', 42, nested);
      const json = instance.toJSON();

      expect(json).toEqual({
        name: 'parent',
        value: 42,
        nested: {
          name: 'nested',
          value: 24,
          nested: undefined,
          __class__: 'TestClass',
        },
        __class__: 'TestClass',
      });
    });
  });

  describe('Class Registry', () => {
    it('should register classes', () => {
      registerClasses({ TestClass });
      const json = dumps(new TestClass('test', 42));
      const deserialized = loads(json) as TestClass;

      expect(deserialized).toBeInstanceOf(TestClass);
      expect(deserialized).toEqual(new TestClass('test', 42));
    });

    it('should throw error when deserializing unregistered class', () => {
      const json = dumps(new TestClass('test', 42));
      expect(() => loads(json)).toThrow('Class TestClass not registered');
    });

    it('should clear class registry', () => {
      registerClasses({ TestClass });
      clearClassRegistry();
      const json = dumps(new TestClass('test', 42));
      expect(() => loads(json)).toThrow('Class TestClass not registered');
    });
  });

  describe('dumps and loads', () => {
    beforeEach(() => {
      registerClasses({ TestClass });
    });

    it('should serialize and deserialize primitive values', () => {
      const data = {
        string: 'test',
        number: 42,
        boolean: true,
        null: null,
        array: [1, 2, 3],
        object: { key: 'value' },
      };

      const json = dumps(data);
      const deserialized = loads(json);

      expect(deserialized).toEqual(data);
    });

    it('should handle Map objects', () => {
      const map = new Map([
        ['key1', 'value1'],
        ['key2', 'value2'],
      ]);
      const json = dumps(map);
      const deserialized = loads(json) as Map<string, string>;

      expect(deserialized).toBeInstanceOf(Map);
      expect(Array.from(deserialized.entries())).toEqual(Array.from(map.entries()));
    });

    it('should handle Set objects', () => {
      const set = new Set([1, 2, 3]);
      const json = dumps(set);
      const deserialized = loads(json) as Set<number>;

      expect(deserialized).toBeInstanceOf(Set);
      expect(Array.from(deserialized)).toEqual(Array.from(set));
    });

    it('should handle complex nested objects', () => {
      const nested = new TestClass('nested', 24);
      const instance = new TestClass('parent', 42, nested);
      const data = {
        instance,
        array: [instance, nested],
        map: new Map([['key', instance]]),
        set: new Set([instance, nested]),
      };

      const json = dumps(data);
      const deserialized = loads(json) as typeof data;

      expect(deserialized.instance).toBeInstanceOf(TestClass);
      expect(deserialized.instance.nested).toBeInstanceOf(TestClass);
      expect(deserialized.array[0]).toBeInstanceOf(TestClass);
      expect(deserialized.array[1]).toBeInstanceOf(TestClass);
      expect(deserialized.map.get('key')).toBeInstanceOf(TestClass);
      expect(Array.from(deserialized.set)[0]).toBeInstanceOf(TestClass);
      expect(Array.from(deserialized.set)[1]).toBeInstanceOf(TestClass);
    });
  });
});
