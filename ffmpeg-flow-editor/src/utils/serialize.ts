// Type definitions
type Constructor<T> = new (...args: unknown[]) => T;

// Define base types first to avoid circular references
type SerializablePrimitive = string | number | boolean | null | undefined;
type SerializableArray = SerializableValue[];
type SerializableMap = Map<SerializableValue, SerializableValue>;
type SerializableSet = Set<SerializableValue>;
type SerializableObject = { [key: string]: SerializableValue };
type SerializableValue =
  | SerializablePrimitive
  | Date
  | SerializableMap
  | SerializableSet
  | SerializableArray
  | SerializableObject;

// Special types for serialized form
interface SerializedSpecial {
  __type__: string;
  value: unknown;
}

interface SerializedClass {
  __class__: string;
  [key: string]: SerializedValue;
}

interface SerializedCircular {
  __circular__: true;
}

type SerializedValue =
  | SerializablePrimitive
  | SerializedSpecial
  | SerializedClass
  | SerializedCircular;

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
    const entries = Array.from(obj.entries()).map(([k, v]) => [
      toDictWithClassInfo(k as SerializableValue, seen),
      toDictWithClassInfo(v as SerializableValue, seen),
    ]);
    return {
      __type__: 'Map',
      value: entries,
    } as SerializedSpecial;
  }

  if (obj instanceof Set) {
    const values = Array.from(obj).map((v) => toDictWithClassInfo(v as SerializableValue, seen));
    return {
      __type__: 'Set',
      value: values,
    } as SerializedSpecial;
  }

  if (obj instanceof Date) {
    return {
      __type__: 'Date',
      value: obj.toISOString(),
    } as SerializedSpecial;
  }

  if (Array.isArray(obj)) {
    return obj.map((item) =>
      toDictWithClassInfo(item as SerializableValue, seen)
    ) as unknown as SerializedValue;
  }

  if (obj instanceof Object && obj.constructor !== Object) {
    const result: SerializedClass = {
      __class__: obj.constructor.name,
    };
    for (const key in obj) {
      if (Object.prototype.hasOwnProperty.call(obj, key)) {
        const value = (obj as Record<string, unknown>)[key];
        if (value !== undefined) {
          result[key] = toDictWithClassInfo(value as SerializableValue, seen);
        }
      }
    }
    return result;
  }

  // For plain objects, don't add __class__ information
  const result: Record<string, SerializedValue> = {};
  for (const key in obj) {
    if (Object.prototype.hasOwnProperty.call(obj, key)) {
      const value = (obj as Record<string, unknown>)[key];
      if (value !== undefined) {
        result[key] = toDictWithClassInfo(value as SerializableValue, seen);
      }
    }
  }
  return result as unknown as SerializedValue;
}

// Custom JSON deserialization
function objectHook(_key: string, value: unknown): unknown {
  if (
    value &&
    typeof value === 'object' &&
    '__class__' in value &&
    typeof value.__class__ === 'string'
  ) {
    const cls = loadClass(value.__class__);
    const instance = new cls();
    const rest = { ...value } as Record<string, unknown>;
    delete rest.__class__;
    Object.assign(instance as Record<string, unknown>, rest);
    return instance;
  }

  if (
    value &&
    typeof value === 'object' &&
    '__type__' in value &&
    typeof value.__type__ === 'string'
  ) {
    const typed = value as SerializedSpecial;
    switch (typed.__type__) {
      case 'Map':
        return new Map(typed.value as [unknown, unknown][]);
      case 'Set':
        return new Set(typed.value as unknown[]);
      case 'Date':
        return new Date(typed.value as string);
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

  toJSON(): SerializedValue {
    return toDictWithClassInfo(this as unknown as SerializableValue);
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
