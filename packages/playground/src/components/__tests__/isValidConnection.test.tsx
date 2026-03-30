import { describe, it, expect, beforeEach } from 'vitest';
import { Connection, Node, Edge } from 'reactflow';
import { EdgeType, EdgeData } from '../../types/edge';
import { validateConnection } from '../../utils/connectionValidation';

// Mock types needed for testing
interface HandleInfo {
  id: string;
  type: EdgeType;
}

interface FilterNodeData {
  filterType: 'input' | 'filter' | 'output';
  filterName?: string;
  handles: {
    inputs: HandleInfo[];
    outputs: HandleInfo[];
  };
}

// Create test nodes that match the ReactFlow Node type
type TestNode = Node<FilterNodeData>;
type TestEdge = Edge<EdgeData>;

describe('validateConnection', () => {
  let mockNodes: TestNode[];
  let mockEdges: TestEdge[];

  beforeEach(() => {
    // Setup test data before each test
    mockNodes = [
      // Input node with 'av' output
      {
        id: 'input-1',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: {
          filterType: 'input',
          handles: {
            inputs: [],
            outputs: [{ id: 'output-0', type: 'av' }],
          },
        },
      },
      // Output node with 'av' input
      {
        id: 'output-1',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: {
          filterType: 'output',
          handles: {
            inputs: [{ id: 'input-0', type: 'av' }],
            outputs: [],
          },
        },
      },
      // Audio filter
      {
        id: 'audio-filter-1',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: {
          filterType: 'filter',
          filterName: 'volume',
          handles: {
            inputs: [{ id: 'input-0', type: 'audio' }],
            outputs: [{ id: 'output-0', type: 'audio' }],
          },
        },
      },
      // Video filter
      {
        id: 'video-filter-1',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: {
          filterType: 'filter',
          filterName: 'scale',
          handles: {
            inputs: [{ id: 'input-0', type: 'video' }],
            outputs: [{ id: 'output-0', type: 'video' }],
          },
        },
      },
      // AV filter
      {
        id: 'av-filter-1',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: {
          filterType: 'filter',
          filterName: 'overlay',
          handles: {
            inputs: [
              { id: 'input-0', type: 'video' },
              { id: 'input-1', type: 'video' },
            ],
            outputs: [{ id: 'output-0', type: 'av' }],
          },
        },
      },
      // Second audio filter (for testing connections)
      {
        id: 'audio-filter-2',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: {
          filterType: 'filter',
          filterName: 'loudnorm',
          handles: {
            inputs: [{ id: 'input-0', type: 'audio' }],
            outputs: [{ id: 'output-0', type: 'audio' }],
          },
        },
      },
    ];

    // Start with one edge already connected
    mockEdges = [
      {
        id: 'edge-1',
        source: 'audio-filter-1',
        sourceHandle: 'output-0',
        target: 'audio-filter-2',
        targetHandle: 'input-0',
        type: 'smoothstep',
      },
    ];
  });

  // Test Rule 1: Input nodes can connect to any filter
  it('allows input nodes to connect to any filter node', () => {
    const audioConnection: Connection = {
      source: 'input-1',
      sourceHandle: 'output-0',
      target: 'audio-filter-1',
      targetHandle: 'input-0',
    };

    const videoConnection: Connection = {
      source: 'input-1',
      sourceHandle: 'output-0',
      target: 'video-filter-1',
      targetHandle: 'input-0',
    };

    expect(validateConnection(audioConnection, mockNodes, [])).toBe(true);
    expect(validateConnection(videoConnection, mockNodes, [])).toBe(true);
  });

  // Test Rule 2: Filter input handles can only have one connection
  it('prevents connecting to an input handle that already has a connection', () => {
    const connection: Connection = {
      source: 'video-filter-1',
      sourceHandle: 'output-0',
      target: 'audio-filter-2', // Already has a connection from audio-filter-1
      targetHandle: 'input-0', // This handle is already connected
    };

    expect(validateConnection(connection, mockNodes, mockEdges)).toBe(false);
  });

  // Test Rule 3: Type compatibility - matching types
  it('allows connections between compatible types (audio to audio)', () => {
    const connection: Connection = {
      source: 'audio-filter-1',
      sourceHandle: 'output-0',
      target: 'output-1',
      targetHandle: 'input-0',
    };

    expect(validateConnection(connection, mockNodes, [])).toBe(true);
  });

  // Test Rule 3: Type compatibility - mismatching types
  it('prevents connections between incompatible types (audio to video)', () => {
    const connection: Connection = {
      source: 'audio-filter-1',
      sourceHandle: 'output-0',
      target: 'video-filter-1',
      targetHandle: 'input-0',
    };

    expect(validateConnection(connection, mockNodes, [])).toBe(false);
  });

  // Test Rule 3: AV source can connect to anything
  it('allows AV source to connect to any type', () => {
    const avToAudioConnection: Connection = {
      source: 'av-filter-1',
      sourceHandle: 'output-0', // AV type
      target: 'audio-filter-1',
      targetHandle: 'input-0', // Audio type
    };

    const avToVideoConnection: Connection = {
      source: 'av-filter-1',
      sourceHandle: 'output-0', // AV type
      target: 'video-filter-1',
      targetHandle: 'input-0', // Video type
    };

    expect(validateConnection(avToAudioConnection, mockNodes, [])).toBe(true);
    expect(validateConnection(avToVideoConnection, mockNodes, [])).toBe(true);
  });

  // Test Rule 4: Output nodes can accept any connection
  it('allows any filter to connect to output nodes', () => {
    const audioToOutputConnection: Connection = {
      source: 'audio-filter-1',
      sourceHandle: 'output-0',
      target: 'output-1',
      targetHandle: 'input-0',
    };

    const videoToOutputConnection: Connection = {
      source: 'video-filter-1',
      sourceHandle: 'output-0',
      target: 'output-1',
      targetHandle: 'input-0',
    };

    expect(validateConnection(audioToOutputConnection, mockNodes, [])).toBe(true);
    expect(validateConnection(videoToOutputConnection, mockNodes, [])).toBe(true);
  });

  // Test invalid connection data
  it('rejects connections with missing node or handle data', () => {
    const invalidConnection: Connection = {
      source: 'non-existent-node',
      sourceHandle: 'output-0',
      target: 'audio-filter-1',
      targetHandle: 'input-0',
    };

    expect(validateConnection(invalidConnection, mockNodes, [])).toBe(false);
  });

  // Test multiple outgoing connections from one node
  it('allows a filter node to have multiple outgoing connections', () => {
    // Create new audio filter nodes to avoid existing connections
    mockNodes.push({
      id: 'audio-filter-3',
      type: 'filter',
      position: { x: 0, y: 0 },
      data: {
        filterType: 'filter',
        filterName: 'aecho',
        handles: {
          inputs: [{ id: 'input-0', type: 'audio' }],
          outputs: [{ id: 'output-0', type: 'audio' }],
        },
      },
    });

    mockNodes.push({
      id: 'audio-filter-4',
      type: 'filter',
      position: { x: 0, y: 0 },
      data: {
        filterType: 'filter',
        filterName: 'acompressor',
        handles: {
          inputs: [{ id: 'input-0', type: 'audio' }],
          outputs: [{ id: 'output-0', type: 'audio' }],
        },
      },
    });

    // First connection
    const connection1: Connection = {
      source: 'audio-filter-1',
      sourceHandle: 'output-0',
      target: 'audio-filter-3',
      targetHandle: 'input-0',
    };

    // Second connection from same source handle
    const connection2: Connection = {
      source: 'audio-filter-1',
      sourceHandle: 'output-0',
      target: 'audio-filter-4',
      targetHandle: 'input-0',
    };

    // Both should be valid
    expect(validateConnection(connection1, mockNodes, mockEdges)).toBe(true);

    // Add the first connection
    mockEdges.push({
      id: 'new-edge',
      source: connection1.source!,
      sourceHandle: connection1.sourceHandle!,
      target: connection1.target!,
      targetHandle: connection1.targetHandle!,
      type: 'smoothstep',
    });

    // Second connection should still be valid (source can have multiple outgoing)
    expect(validateConnection(connection2, mockNodes, mockEdges)).toBe(true);
  });
});
