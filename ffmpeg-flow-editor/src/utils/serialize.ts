// Class registry for serialization
type Constructor<T extends Serializable = Serializable> = new (...args: unknown[]) => T;
const classRegistry = new Map<string, Constructor<Serializable>>();

// Base class for serializable objects
export class Serializable {
<<<<<<< HEAD
  constructor(public id?: string) {}
=======
  id?: string; // Optional id field
>>>>>>> f91210d4 (add id field in Serializable)

  // toJSON will be called by JSON.stringify
  toJSON(): Record<string, unknown> {
    const obj: Record<string, unknown> = {};
    for (const key in this) {
      if (Object.prototype.hasOwnProperty.call(this, key)) {
        // Skip the id property
        if (key === 'id') continue;

        const value = this[key];
        obj[key] = value instanceof Serializable ? value.toJSON() : value;
      }
    }
    obj.__class__ = this.constructor.name;
    return obj;
  }
}

// Register multiple classes at once
export function registerClasses(classes: Record<string, Constructor<Serializable>>) {
  console.log('Registering classes:', Object.keys(classes));
  for (const [name, constructor] of Object.entries(classes)) {
    classRegistry.set(name, constructor);
  }
}

// Clear the class registry
export function clearClassRegistry() {
  console.log('Clearing class registry');
  classRegistry.clear();
}

// Get registered class names
export function getRegisteredClassNames(): string[] {
  return Array.from(classRegistry.keys());
}

// Serialize an object to JSON string
export function dumps(obj: unknown): string {
  return JSON.stringify(obj, (key, value) => {
    if (value instanceof Map) {
      return {
        __type__: 'Map',
        value: Array.from(value.entries()),
      };
    }
    if (value instanceof Set) {
      return {
        __type__: 'Set',
        value: Array.from(value),
      };
    }
    return value;
  });
}

// Deserialize a JSON string to an object
export function loads(json: string): unknown {
  const obj = JSON.parse(json);
  return deserializeObject(obj);
}

// Helper function to deserialize an object
function deserializeObject(obj: unknown): unknown {
  if (obj === null || typeof obj !== 'object') {
    return obj;
  }

  // Handle arrays
  if (Array.isArray(obj)) {
    return obj.map(deserializeObject);
  }

  // Handle special types
  if (obj && typeof obj === 'object' && '__type__' in obj) {
    const typedObj = obj as { __type__: string; value: unknown };
    if (typedObj.__type__ === 'Map') {
      return new Map(
        (typedObj.value as [unknown, unknown][]).map(([k, v]) => [k, deserializeObject(v)])
      );
    }
    if (typedObj.__type__ === 'Set') {
      return new Set((typedObj.value as unknown[]).map(deserializeObject));
    }
  }

  // Handle class instances
  if (obj && typeof obj === 'object' && '__class__' in obj) {
    const classObj = obj as { __class__: string; [key: string]: unknown };
    const Constructor = classRegistry.get(classObj.__class__);
    if (!Constructor) {
      throw new Error(`Class ${classObj.__class__} not registered`);
    }

    // Create a new instance without calling constructor
    const instance = Object.create(Constructor.prototype);

    // Deserialize all properties
    for (const key in classObj) {
      if (key !== '__class__') {
        instance[key] = deserializeObject(classObj[key]);
      }
    }

    return instance;
  }

  // Handle plain objects
  const result: Record<string, unknown> = {};
  for (const key in obj) {
    result[key] = deserializeObject((obj as Record<string, unknown>)[key]);
  }
  return result;
}
