import { StreamType } from '../types/dag';

// Type definitions
type Constructor<T> = new (...args: unknown[]) => T;
type SerializableValue =
  | string
  | number
  | boolean
  | null
  | undefined
  | Date
  | Map<unknown, unknown>
  | Set<unknown>
  | SerializableValue[]
  | Record<string, SerializableValue>;
type SerializedObject = { [key: string]: SerializedValue };
type SerializedValue = string | number | boolean | null | undefined | SerializedObject;

// Class registry for deserialization
const CLASS_REGISTRY: Record<string, Constructor<unknown>> = {};

// Function to register a class for deserialization
export function serializable<T extends Constructor<unknown>>(cls: T): T {
  const className = cls.name;
  if (className in CLASS_REGISTRY) {
    // Instead of throwing, just return the existing class
    return CLASS_REGISTRY[className] as T;
  }
  CLASS_REGISTRY[className] = cls;
  return cls;
}

// Function to load a class by name
function loadClass(className: string): Constructor<unknown> {
  const cls = CLASS_REGISTRY[className];
  if (!cls) {
    throw new Error(`Class ${className} not registered`);
  }
  return cls;
}

// Function to convert mutable data structures to immutable equivalents
function freeze<T extends SerializableValue>(obj: T): T {
  if (obj === null || typeof obj !== 'object') {
    return obj;
  }

  if (obj instanceof Map) {
    return new Map(Array.from(obj.entries()).map(([k, v]) => [k, freeze(v)])) as T;
  }

  if (obj instanceof Set) {
    return new Set(Array.from(obj).map(freeze)) as T;
  }

  if (obj instanceof Date) {
    return new Date(obj.getTime()) as T;
  }

  if (Array.isArray(obj)) {
    return obj.map(freeze) as T;
  }

  const result = {} as T;
  for (const key in obj) {
    if (Object.prototype.hasOwnProperty.call(obj, key)) {
      result[key] = freeze(obj[key]);
    }
  }
  return result;
}

// Convert object to dictionary with embedded class information
function toDictWithClassInfo(obj: SerializableValue, seen = new WeakSet()): SerializedValue {
  if (obj === null || typeof obj !== 'object') {
    return obj;
  }

  // Handle circular references
  if (seen.has(obj)) {
    return { __circular__: true };
  }
  seen.add(obj);

  if (obj instanceof Map) {
    return {
      __type__: 'Map',
      value: Array.from(obj.entries()),
    };
  }

  if (obj instanceof Set) {
    return {
      __type__: 'Set',
      value: Array.from(obj),
    };
  }

  if (obj instanceof Date) {
    return {
      __type__: 'Date',
      value: obj.toISOString(),
    };
  }

  if (Array.isArray(obj)) {
    return obj.map((item) => toDictWithClassInfo(item as SerializableValue, seen));
  }

  if (obj instanceof Object && obj.constructor !== Object) {
    const result: SerializedObject = {
      __class__: obj.constructor.name,
    };
    for (const key in obj) {
      if (Object.prototype.hasOwnProperty.call(obj, key)) {
        result[key] = toDictWithClassInfo(
          (obj as Record<string, unknown>)[key] as SerializableValue,
          seen
        );
      }
    }
    return result;
  }

  const result: SerializedObject = {};
  for (const key in obj) {
    if (Object.prototype.hasOwnProperty.call(obj, key)) {
      result[key] = toDictWithClassInfo(
        (obj as Record<string, unknown>)[key] as SerializableValue,
        seen
      );
    }
  }
  return result;
}

// Custom JSON deserialization
function objectHook(_key: string, value: SerializedValue): unknown {
  if (value && typeof value === 'object' && '__class__' in value) {
    const cls = loadClass(value.__class__);
    const instance = new cls();
    const { __class__, ...rest } = value;
    Object.assign(instance, rest);
    return instance;
  }

  if (value && typeof value === 'object' && '__type__' in value) {
    switch (value.__type__) {
      case 'Map':
        return new Map(value.value as [unknown, unknown][]);
      case 'Set':
        return new Set(value.value as unknown[]);
      case 'Date':
        return new Date(value.value as string);
      default:
        return value;
    }
  }

  return value;
}

// Serialize object to JSON string
export function dumps(obj: SerializableValue): string {
  return JSON.stringify(toDictWithClassInfo(obj), null, 2);
}

// Deserialize JSON string to object
export function loads(json: string): unknown {
  return JSON.parse(json, objectHook);
}

// Base class for serializable objects
export abstract class Serializable {
  constructor() {
    // Register the class if it's not already registered
    const cls = this.constructor as Constructor<unknown>;
    if (!(cls.name in CLASS_REGISTRY)) {
      serializable(cls);
    }
  }

  toJSON(): string {
    return dumps(this);
  }

  static fromJSON<T extends Serializable>(this: Constructor<T>, json: string): T {
    return loads(json) as T;
  }
}

// Clear the class registry (for testing)
export function clearClassRegistry(): void {
  Object.keys(CLASS_REGISTRY).forEach((key) => {
    delete CLASS_REGISTRY[key];
  });
}
