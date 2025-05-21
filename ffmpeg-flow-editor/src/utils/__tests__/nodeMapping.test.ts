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
    await nodeMappingManager._recursiveAddInternal(
      deserialized as
        | FilterNode
        | InputNode
        | OutputNode
        | GlobalNode
        | FilterableStream
        | VideoStream
        | AudioStream
        | AVStream
        | OutputStream
        | GlobalStream
    );
    // check node mapping's snapshot
    expect(nodeMappingManager.getNodeMapping()).toMatchSnapshot();
    // check edge mapping's snapshot
    expect(nodeMappingManager.getEdgeMapping()).toMatchSnapshot();
    // check node mapping's json
    expect(nodeMappingManager.toJson()).toMatchSnapshot();
  });
});

describe('recursiveAddToMapping', () => {
  it('should recursively add nodes and streams to the mapping', async () => {
    const nodeMapping = new NodeMappingManager();
    const sourceId = await nodeMapping.addNodeToMapping({
      type: 'input',
      filename: 'input.mp4',
    });

    const target1Id = await nodeMapping.addNodeToMapping({
      type: 'filter',
      name: 'scale',
      inputs: [null],
      kwargs: { width: 640, height: 480 },
    });

    const target2Id = await nodeMapping.addNodeToMapping({
      type: 'output',
      filename: 'output.mp4',
    });

    // Add edges to mapping
    const edge1 = nodeMapping.addEdgeToMapping(sourceId, target1Id, 0, 0);
    const edge2 = nodeMapping.addEdgeToMapping(target1Id, target2Id, 0, 0);

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
    const inputId = await nodeMapping.addNodeToMapping({
      type: 'input',
      filename: 'input.mp4',
      kwargs: {},
    });
    const filterId = await nodeMapping.addNodeToMapping({
      type: 'filter',
      name: 'scale',
      inputs: [null],
      kwargs: { width: 640, height: 480 },
    });
    const outputId = await nodeMapping.addNodeToMapping({
      type: 'output',
      filename: 'output.mp4',
      kwargs: {},
    });

    // Add edges to mapping
    const edge1 = nodeMapping.addEdgeToMapping(inputId, filterId, 0, 0);
    const edge2 = nodeMapping.addEdgeToMapping(filterId, outputId, 0, 0);

    // Verify nodes are in mapping
    expect(nodeMapping.getNodeMapping().nodeMap.get(inputId)).toBeInstanceOf(InputNode);
    expect(nodeMapping.getNodeMapping().nodeMap.get(filterId)).toBeInstanceOf(FilterNode);
    expect(nodeMapping.getNodeMapping().nodeMap.get(outputId)).toBeInstanceOf(OutputNode);

    // Verify edges are in mapping
    expect(nodeMapping.getEdgeMapping().edgeMap.get(edge1)).toBeDefined();
    expect(nodeMapping.getEdgeMapping().edgeMap.get(edge2)).toBeDefined();
  });
});
