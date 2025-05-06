// Class registry for serialization
const classRegistry = new Map<string, new (...args: any[]) => any>();

// Base class for serializable objects
export class Serializable {
  toJSON(): any {
    const obj: any = {};
    for (const key in this) {
      if (Object.prototype.hasOwnProperty.call(this, key)) {
        obj[key] = this[key];
      }
    }
    obj.__class__ = this.constructor.name;
    return obj;
  }
}

// Register multiple classes at once
export function registerClasses(classes: Record<string, new (...args: any[]) => any>) {
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
export function dumps(obj: any): string {
  return JSON.stringify(obj);
}

// Deserialize a JSON string to an object
export function loads(json: string): any {
  const obj = JSON.parse(json);
  return deserializeObject(obj);
}

// Helper function to deserialize an object
function deserializeObject(obj: any): any {
  if (obj === null || typeof obj !== 'object') {
    return obj;
  }

  // Handle arrays
  if (Array.isArray(obj)) {
    return obj.map(deserializeObject);
  }

  // Handle special types
  if (obj instanceof Date) {
    return new Date(obj);
  }

  if (obj instanceof Map) {
    return new Map(Array.from(obj.entries()).map(([k, v]) => [k, deserializeObject(v)]));
  }

  if (obj instanceof Set) {
    return new Set(Array.from(obj).map(deserializeObject));
  }

  // Handle class instances
  if (obj.__class__) {
    console.log('Looking for class:', obj.__class__);
    console.log('Registered classes:', getRegisteredClassNames());
    const Constructor = classRegistry.get(obj.__class__);
    if (!Constructor) {
      throw new Error(`Class ${obj.__class__} not registered`);
    }

    // Create a new instance without calling constructor
    const instance = Object.create(Constructor.prototype);

    // Deserialize all properties
    for (const key in obj) {
      if (key !== '__class__') {
        instance[key] = deserializeObject(obj[key]);
      }
    }

    return instance;
  }

  // Handle plain objects
  const result: any = {};
  for (const key in obj) {
    result[key] = deserializeObject(obj[key]);
  }
  return result;
}
