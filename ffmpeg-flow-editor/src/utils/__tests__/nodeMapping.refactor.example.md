# NodeMappingManager Refactoring Guide

Based on the code review, here are specific examples of how to refactor the `NodeMappingManager` class to address the identified issues without making wholesale changes to the codebase.

## 1. Improve Lookup Performance

The current lookup methods (`getNodeId` and `getEdgeId`) iterate through all entries. We can create reverse lookup maps to improve performance:

```typescript
// Add reverse lookup maps in the class declaration
private nodeMap: Map<string, Node> = new Map();
private reverseNodeMap: Map<Node, string> = new Map(); // Add this

private edgeMap: Map<string, Stream> = new Map();
private reverseEdgeMap: Map<Stream, string> = new Map(); // Add this
```

Then update the methods:

```typescript
private getNodeId(node: Node): string {
  const nodeId = this.reverseNodeMap.get(node);
  if (!nodeId) {
    throw new Error('Node not found in mapping');
  }
  return nodeId;
}

private getEdgeId(stream: Stream): string {
  const edgeId = this.reverseEdgeMap.get(stream);
  if (!edgeId) {
    throw new Error('Edge not found in mapping');
  }
  return edgeId;
}
```

And update all methods that add/remove nodes/edges to maintain both maps:

```typescript
// When adding a node
this.nodeMap.set(nodeId, node);
this.reverseNodeMap.set(node, nodeId);

// When removing a node
const node = this.nodeMap.get(nodeId);
this.nodeMap.delete(nodeId);
this.reverseNodeMap.delete(node);

// Similarly for edges
```

## 2. Consistent Error Handling

Replace silent failures with proper error handling:

```typescript
// Current
private async evaluateIOtypings(
  filter: FFmpegFilter,
  kwargs: Record<string, string | number | boolean>
): Promise<{ input_typings: StreamType[]; output_typings: StreamType[] }> {
  // ... existing code ...
  
  let input_typings: FFMpegIOType[] = [];
  if (!filter.formula_typings_input) {
    input_typings = filter.stream_typings_input;
  } else {
    input_typings = await evaluateFormula(filter.formula_typings_input, parameters);
  }
  // ... similar for output_typings ...
  
  return {
    input_typings: input_typings.map((t) => t.type),
    output_typings: output_typings.map((t) => t.type),
  };
}
```

Refactored with proper error handling:

```typescript
private async evaluateIOtypings(
  filter: FFmpegFilter,
  kwargs: Record<string, string | number | boolean>
): Promise<{ input_typings: StreamType[]; output_typings: StreamType[] }> {
  // ... existing code ...
  
  let input_typings: FFMpegIOType[] = [];
  try {
    if (!filter.formula_typings_input) {
      input_typings = filter.stream_typings_input;
    } else {
      input_typings = await evaluateFormula(filter.formula_typings_input, parameters);
    }
  } catch (error) {
    console.error(`Failed to evaluate input typings for filter ${filter.name}:`, error);
    // Fall back to empty array instead of silently failing
  }
  
  let output_typings: FFMpegIOType[] = [];
  try {
    if (!filter.formula_typings_output) {
      output_typings = filter.stream_typings_output;
    } else {
      output_typings = await evaluateFormula(filter.formula_typings_output, parameters);
    }
  } catch (error) {
    console.error(`Failed to evaluate output typings for filter ${filter.name}:`, error);
    // Fall back to empty array instead of silently failing
  }
  
  return {
    input_typings: input_typings.map((t) => t.type),
    output_typings: output_typings.map((t) => t.type),
  };
}
```

## 3. Consistent Null Checks

Replace `!` operator and inconsistent null checks:

```typescript
// Current - Inconsistent checks
if (edge.index === null) {
  throw new Error('Edge index is null');
}

// Later in code
if (!stream.index) {
  throw new Error('Edge index is null');
}
```

Refactored to be consistent:

```typescript
// Always use strict equality for null checks
if (edge.index === null) {
  throw new Error('Edge index is null');
}

// And later in code, also use strict equality
if (stream.index === null) {
  throw new Error('Edge index is null');
}
```

## 4. Reduce Code Duplication

Extract common patterns into helper methods:

```typescript
// Current - Duplicate logic in getEdgesBySource and getEdgesByTarget
private getEdgesBySource(source: Node): (Stream | null)[] {
  if (!(source instanceof FilterNode)) {
    return Array.from(this.edgeMap.values()).filter((s) => s.node === source);
  }
  // ... more code ...
}

private getEdgesByTarget(target: Node): (Stream | null)[] {
  return target.inputs;
}
```

Refactored:

```typescript
private findEdgesByNode(node: Node, isSource: boolean): (Stream | null)[] {
  if (isSource) {
    if (!(node instanceof FilterNode)) {
      return Array.from(this.edgeMap.values()).filter((s) => s.node === node);
    }
    // ... FilterNode source logic ...
  } else {
    return node.inputs;
  }
}

private getEdgesBySource(source: Node): (Stream | null)[] {
  return this.findEdgesByNode(source, true);
}

private getEdgesByTarget(target: Node): (Stream | null)[] {
  return this.findEdgesByNode(target, false);
}
```

## 5. Improved Type Safety

Replace type casts with proper type guards:

```typescript
// Current
const target = this.nodeMap.entries().find(([_, n]) => n.inputs.includes(edge))?.[1];
if (!target) {
  throw new Error('Target node not found in mapping');
}
return target;
```

Refactored:

```typescript
private getTargetNodeByEdge(edge: Stream): Node {
  const entry = Array.from(this.nodeMap.entries()).find(([_, n]) => n.inputs.includes(edge));
  if (!entry) {
    throw new Error('Target node not found in mapping');
  }
  return entry[1];
}
```

## 6. Better Event Handling

Improve the event handling system to prevent memory leaks:

```typescript
// Current
public on(eventType: NodeMappingEventType, listener: () => void): () => void {
  this.eventEmitter.on(eventType, listener);
  return () => {
    this.eventEmitter.off(eventType, listener);
  };
}
```

Refactored:

```typescript
private listeners = new Map<string, Set<() => void>>();

public on(eventType: NodeMappingEventType, listener: () => void): () => void {
  if (!this.listeners.has(eventType)) {
    this.listeners.set(eventType, new Set());
  }
  
  const listeners = this.listeners.get(eventType)!;
  listeners.add(listener);
  
  // Return a function to unsubscribe
  return () => {
    if (this.listeners.has(eventType)) {
      const listeners = this.listeners.get(eventType)!;
      listeners.delete(listener);
      if (listeners.size === 0) {
        this.listeners.delete(eventType);
      }
    }
  };
}

private emitUpdate(): void {
  if (this.listeners.has(NODE_MAPPING_EVENTS.UPDATE)) {
    const listeners = this.listeners.get(NODE_MAPPING_EVENTS.UPDATE)!;
    for (const listener of listeners) {
      listener();
    }
  }
}

// Clean up all listeners when the manager is disposed
public dispose(): void {
  this.listeners.clear();
  this.eventEmitter.removeAllListeners();
}
```

## 7. Comprehensive JSDoc Comments

Add detailed JSDoc comments for better code documentation:

```typescript
/**
 * Adds a new node to the mapping
 * 
 * @param params - Node creation parameters
 * @param params.type - The type of node to create ('filter', 'input', 'output', or 'global')
 * @param params.name - The name of the filter (required for 'filter' type)
 * @param params.filename - The filename (required for 'input' and 'output' types)
 * @param params.inputs - Initial input streams for the node (optional)
 * @param params.kwargs - Additional parameters for the node (optional)
 * 
 * @returns A promise that resolves to the ID of the newly created node
 * 
 * @throws {Error} If required parameters are missing or invalid
 * @throws {Error} If the specified filter does not exist
 */
public async addNodeMapping(params: {
  type: 'filter' | 'input' | 'output' | 'global';
  name?: string;
  filename?: string;
  inputs?: (FilterableStream | null | OutputStream)[];
  kwargs?: Record<string, string | number | boolean>;
}): Promise<string> {
  // ... implementation ...
}
```

## 8. Decompose the Manager Class

Split the large class into focused components:

```typescript
// NodeRegistry.ts - Handles node storage and retrieval
export class NodeRegistry {
  private nodeMap = new Map<string, Node>();
  private reverseNodeMap = new Map<Node, string>();
  
  // Node management methods
}

// EdgeRegistry.ts - Handles edge storage and retrieval
export class EdgeRegistry {
  private edgeMap = new Map<string, Stream>();
  private reverseEdgeMap = new Map<Stream, string>();
  
  // Edge management methods
}

// NodeFactory.ts - Handles node creation
export class NodeFactory {
  // Node creation methods
}

// EventManager.ts - Handles event subscription and emission
export class EventManager {
  // Event management methods
}

// Then compose them in the main manager
export class NodeMappingManager {
  private nodeRegistry: NodeRegistry;
  private edgeRegistry: EdgeRegistry;
  private nodeFactory: NodeFactory;
  private eventManager: EventManager;
  
  constructor() {
    this.nodeRegistry = new NodeRegistry();
    this.edgeRegistry = new EdgeRegistry();
    this.nodeFactory = new NodeFactory();
    this.eventManager = new EventManager();
  }
  
  // Delegate to the appropriate component
}
```

These examples provide concrete ways to address the issues identified in the code review while maintaining the existing functionality and API of the `NodeMappingManager` class. 