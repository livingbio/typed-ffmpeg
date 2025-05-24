import { describe, it, expect, beforeEach, beforeAll } from 'vitest';
import {
  FilterNode,
  InputNode,
  OutputNode,
  GlobalNode,
  VideoStream,
  AudioStream,
  AVStream,
  StreamType,
  FilterableStream,
  OutputStream,
  GlobalStream,
  Stream,
} from '../../types/dag';
import { NodeMappingManager } from '../nodeMapping';
import { loads, clearClassRegistry, registerClasses } from '../../utils/serialize';
import { readdirSync, readFileSync } from 'fs';
import { join } from 'path';
import { setupPyodideMock } from './testUtils';

// Clear and register classes before tests
beforeAll(() => {
  clearClassRegistry();

  beforeEach(() => {
    setupPyodideMock();
  });

  // Register all classes explicitly
  registerClasses({
    StreamType,
    FilterNode,
    InputNode,
    OutputNode,
    GlobalNode,
    FilterableStream,
    VideoStream,
    AudioStream,
    AVStream,
    OutputStream,
    GlobalStream,
  });
});

const testDataDir = join(__dirname, '__testdata__');
const testFiles = readdirSync(testDataDir)
  .filter((file) => file.endsWith('.json'))
  .map((file) => ({
    name: file.replace('.json', ''),
    data: JSON.parse(readFileSync(join(testDataDir, file), 'utf-8')),
  }));

describe('Node Mapping', () => {
  let nodeMappingManager: NodeMappingManager;

  beforeEach(() => {
    nodeMappingManager = new NodeMappingManager();
    setupPyodideMock();
  });

  it.each(testFiles)('should handle $name case', async ({ data }) => {
    const jsonString = JSON.stringify(data);

    // Deserialize
    const deserialized = loads(jsonString);
    await nodeMappingManager._recursiveAddInternal(deserialized as Node | Stream);
    // check node mapping's snapshot
    expect(nodeMappingManager.toJson()).toEqual(jsonString);
    expect(nodeMappingManager.getNodeMapping()).toMatchSnapshot();
    // check edge mapping's snapshot
    expect(nodeMappingManager.getEdgeMapping()).toMatchSnapshot();
    // check node mapping's json
    expect(nodeMappingManager.toJson()).toMatchSnapshot();
  });

  it('should import from JSON string', async () => {
    // Create a test graph
    const sourceId = await nodeMappingManager.addNode({
      type: 'input',
      filename: 'input.mp4',
    });

    const filterId = await nodeMappingManager.addNode({
      type: 'filter',
      name: 'scale',
      inputs: [null],
      kwargs: { width: 640, height: 480 },
    });

    const outputId = await nodeMappingManager.addNode({
      type: 'output',
      filename: 'output.mp4',
    });

    const globalId = await nodeMappingManager.addNode({
      type: 'global',
    });

    // Add edges
    nodeMappingManager.addEdge(sourceId, filterId, 0, 0);
    nodeMappingManager.addEdge(filterId, outputId, 0, 0);
    nodeMappingManager.addEdge(outputId, globalId, 0, 0);

    // Export to JSON
    const jsonString = nodeMappingManager.toJson();

    // Create a new manager and import from JSON
    const newManager = new NodeMappingManager();
    await newManager.fromJson(jsonString);

    // Verify the imported graph matches the original
    expect(newManager.toJson()).toEqual(jsonString);
  });
});

describe('recursiveAddToMapping', () => {
  it('should recursively add nodes and streams to the mapping', async () => {
    const nodeMapping = new NodeMappingManager();
    const sourceId = await nodeMapping.addNode({
      type: 'input',
      filename: 'input.mp4',
    });

    const target1Id = await nodeMapping.addNode({
      type: 'filter',
      name: 'scale',
      inputs: [null],
      kwargs: { width: 640, height: 480 },
    });

    const target2Id = await nodeMapping.addNode({
      type: 'output',
      filename: 'output.mp4',
    });

    // Add edges to mapping
    const edge1 = nodeMapping.addEdge(sourceId, target1Id, 0, 0);
    const edge2 = nodeMapping.addEdge(target1Id, target2Id, 0, 0);

    // Verify nodes are in mapping
    expect(nodeMapping.getNodeMapping().nodeMap.get(sourceId)).toBeInstanceOf(InputNode);
    expect(nodeMapping.getNodeMapping().nodeMap.get(target1Id)).toBeInstanceOf(FilterNode);
    expect(nodeMapping.getNodeMapping().nodeMap.get(target2Id)).toBeInstanceOf(OutputNode);

    // Verify edges are in mapping
    expect(nodeMapping.getEdgeMapping().edgeMap.get(edge1)).toBeDefined();
    expect(nodeMapping.getEdgeMapping().edgeMap.get(edge2)).toBeDefined();
  });

  it('should recursively add nodes and edges to mapping', async () => {
    const nodeMapping = new NodeMappingManager();

    // Add nodes to mapping
    const inputId = await nodeMapping.addNode({
      type: 'input',
      filename: 'input.mp4',
      kwargs: {},
    });
    const filterId = await nodeMapping.addNode({
      type: 'filter',
      name: 'scale',
      inputs: [null],
      kwargs: { width: 640, height: 480 },
    });
    const outputId = await nodeMapping.addNode({
      type: 'output',
      filename: 'output.mp4',
      kwargs: {},
    });

    // Add edges to mapping
    const edge1 = nodeMapping.addEdge(inputId, filterId, 0, 0);
    const edge2 = nodeMapping.addEdge(filterId, outputId, 0, 0);

    // Verify nodes are in mapping
    expect(nodeMapping.getNodeMapping().nodeMap.get(inputId)).toBeInstanceOf(InputNode);
    expect(nodeMapping.getNodeMapping().nodeMap.get(filterId)).toBeInstanceOf(FilterNode);
    expect(nodeMapping.getNodeMapping().nodeMap.get(outputId)).toBeInstanceOf(OutputNode);

    // Verify edges are in mapping
    expect(nodeMapping.getEdgeMapping().edgeMap.get(edge1)).toBeDefined();
    expect(nodeMapping.getEdgeMapping().edgeMap.get(edge2)).toBeDefined();
  });
});
