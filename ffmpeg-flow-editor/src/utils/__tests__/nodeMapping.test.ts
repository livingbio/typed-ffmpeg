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

// Clear and register classes before tests
beforeAll(() => {
  clearClassRegistry();

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

describe('nodeMapping', () => {
  let nodeMappingManager: NodeMappingManager;

  beforeEach(() => {
    nodeMappingManager = new NodeMappingManager();
  });

  describe('addNodeToMapping', () => {
    it('should add a FilterNode to mapping', async () => {
      const id = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'test',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });
      expect(id).toMatch(/^filter-test-/);
      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id)!;
      expect(node).toBeInstanceOf(FilterNode);
      expect(node.id).toBe(id);
    });

    it('should add an InputNode to mapping', async () => {
      const id = await nodeMappingManager.addNodeToMapping({
        type: 'input',
        filename: 'test.mp4',
      });
      expect(id).toMatch(/^input-/);
      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id)!;
      expect(node).toBeInstanceOf(InputNode);
      expect(node.id).toBe(id);
    });

    it('should add an OutputNode to mapping', async () => {
      const id = await nodeMappingManager.addNodeToMapping({
        type: 'output',
        filename: 'test.mp4',
        inputs: [],
      });
      expect(id).toMatch(/^output-/);
      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id)!;
      expect(node).toBeInstanceOf(OutputNode);
      expect(node.id).toBe(id);
    });

    it('should add a GlobalNode to mapping', async () => {
      const id = await nodeMappingManager.addNodeToMapping({
        type: 'global',
        inputs: [],
      });
      expect(id).toMatch(/^global-/);
      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id)!;
      expect(node).toBeInstanceOf(GlobalNode);
      expect(node.id).toBe(id);
    });

    it('should add a filter node to the mapping', async () => {
      const id = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'scale',
        input_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
        output_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
      });
      expect(id).toBeDefined();
      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id);
      expect(node).toBeDefined();
    });

    it('should add an input node to the mapping', async () => {
      const id = await nodeMappingManager.addNodeToMapping({
        type: 'input',
        filename: 'input.mp4',
      });
      expect(id).toBeDefined();
      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id);
      expect(node).toBeDefined();
    });

    it('should add an output node to the mapping', async () => {
      const id = await nodeMappingManager.addNodeToMapping({
        type: 'output',
        filename: 'output.mp4',
      });
      expect(id).toBeDefined();
      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id);
      expect(node).toBeDefined();
    });

    it('should add a global node to the mapping', async () => {
      const id = await nodeMappingManager.addNodeToMapping({
        type: 'global',
        inputs: [],
      });
      expect(id).toBeDefined();
      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id);
      expect(node).toBeDefined();
    });

    it('should throw an error for invalid node type', async () => {
      await expect(
        nodeMappingManager.addNodeToMapping({
          type: 'invalid' as 'filter' | 'input' | 'output' | 'global',
        })
      ).rejects.toThrow('Invalid node type');
    });
  });

  describe('removeNodeFromMapping', () => {
    it('should remove a node from mapping', async () => {
      const id = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'test',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });
      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id)!;
      nodeMappingManager.removeNodeFromMapping(id);
      expect(nodeMappingManager.getNodeMapping().nodeMap.get(id)).toBeUndefined();
      expect(node.id).toBeUndefined();
    });

    it('should remove a node and all its connected edges', async () => {
      // Create source node
      const sourceId = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'source',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video'), new StreamType('video')],
      });

      // Create two target nodes
      const target1Id = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'target1',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });

      const target2Id = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'target2',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });

      // Connect source to both targets
      const edge1Id = nodeMappingManager.addEdgeToMapping(sourceId, target1Id, 0, 0);
      const edge2Id = nodeMappingManager.addEdgeToMapping(sourceId, target2Id, 1, 0);

      // Remove source node
      nodeMappingManager.removeNodeFromMapping(sourceId);

      // Check that source node is removed
      expect(nodeMappingManager.getNodeMapping().nodeMap.get(sourceId)).toBeUndefined();

      // Check that edges are removed
      expect(nodeMappingManager.getEdgeMapping().edgeMap.get(edge1Id)).toBeUndefined();
      expect(nodeMappingManager.getEdgeMapping().edgeMap.get(edge2Id)).toBeUndefined();

      // Check that target nodes' inputs are cleared
      const target1Node = nodeMappingManager.getNodeMapping().nodeMap.get(target1Id)! as FilterNode;
      const target2Node = nodeMappingManager.getNodeMapping().nodeMap.get(target2Id)! as FilterNode;
      expect(target1Node.inputs[0]).toBeNull();
      expect(target2Node.inputs[0]).toBeNull();
    });

    it('should throw error when removing non-existent node', () => {
      expect(() => nodeMappingManager.removeNodeFromMapping('non-existent')).toThrow(
        'Node non-existent not found in mapping'
      );
    });
  });

  describe('addEdgeToMapping', () => {
    it('should add a video stream edge between FilterNodes', async () => {
      const sourceId = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'source',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });
      const targetId = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'target',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });

      const edgeId = nodeMappingManager.addEdgeToMapping(sourceId, targetId, 0, 0);
      expect(edgeId).toMatch(/^edge-/);
      const targetNode = nodeMappingManager.getNodeMapping().nodeMap.get(targetId)! as FilterNode;
      expect(nodeMappingManager.getEdgeMapping().edgeMap.get(edgeId)).toBeInstanceOf(VideoStream);
      expect(targetNode.inputs[0]).toBeInstanceOf(VideoStream);
    });

    it('should add an audio stream edge between FilterNodes', async () => {
      const sourceId = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'source',
        input_typings: [new StreamType('audio')],
        output_typings: [new StreamType('audio')],
      });
      const targetId = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'target',
        input_typings: [new StreamType('audio')],
        output_typings: [new StreamType('audio')],
      });

      const edgeId = nodeMappingManager.addEdgeToMapping(sourceId, targetId, 0, 0);
      expect(edgeId).toMatch(/^edge-/);
      const targetNode = nodeMappingManager.getNodeMapping().nodeMap.get(targetId)! as FilterNode;
      expect(nodeMappingManager.getEdgeMapping().edgeMap.get(edgeId)).toBeInstanceOf(AudioStream);
      expect(targetNode.inputs[0]).toBeInstanceOf(AudioStream);
    });

    it('should add an AV stream edge from InputNode to FilterNode', async () => {
      const sourceId = await nodeMappingManager.addNodeToMapping({
        type: 'input',
        filename: 'test.mp4',
      });
      const targetId = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'target',
        input_typings: [new StreamType('av')],
        output_typings: [new StreamType('av')],
      });

      const edgeId = nodeMappingManager.addEdgeToMapping(sourceId, targetId, 0, 0);
      expect(edgeId).toMatch(/^edge-/);
      const targetNode = nodeMappingManager.getNodeMapping().nodeMap.get(targetId)! as FilterNode;
      expect(nodeMappingManager.getEdgeMapping().edgeMap.get(edgeId)).toBeInstanceOf(AVStream);
      expect(targetNode.inputs[0]).toBeInstanceOf(AVStream);
    });

    it('should throw error when connecting video to audio input', async () => {
      const sourceId = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'source',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });
      const targetId = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'target',
        input_typings: [new StreamType('audio')],
        output_typings: [new StreamType('audio')],
      });

      expect(() => nodeMappingManager.addEdgeToMapping(sourceId, targetId, 0, 0)).toThrow(
        'Stream type mismatch'
      );
    });

    it('should throw error when connecting audio to video input', async () => {
      const sourceId = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'source',
        input_typings: [new StreamType('audio')],
        output_typings: [new StreamType('audio')],
      });
      const targetId = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'target',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });

      expect(() => nodeMappingManager.addEdgeToMapping(sourceId, targetId, 0, 0)).toThrow(
        'Stream type mismatch'
      );
    });

    it('should add multiple edges from one source to different targets', async () => {
      const sourceId = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'source',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video'), new StreamType('video')],
      });

      const target1Id = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'target1',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });

      const target2Id = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'target2',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });

      const edge1Id = nodeMappingManager.addEdgeToMapping(sourceId, target1Id, 0, 0);
      const edge2Id = nodeMappingManager.addEdgeToMapping(sourceId, target2Id, 1, 0);

      expect(edge1Id).not.toBe(edge2Id);
      expect(nodeMappingManager.getEdgeMapping().edgeMap.get(edge1Id)).toBeInstanceOf(VideoStream);
      expect(nodeMappingManager.getEdgeMapping().edgeMap.get(edge2Id)).toBeInstanceOf(VideoStream);
    });

    it('should add edge from InputNode to OutputNode', async () => {
      const inputId = await nodeMappingManager.addNodeToMapping({
        type: 'input',
        filename: 'input.mp4',
      });

      const outputId = await nodeMappingManager.addNodeToMapping({
        type: 'output',
        filename: 'output.mp4',
        inputs: [],
      });

      const edgeId = nodeMappingManager.addEdgeToMapping(inputId, outputId, 0, 0);
      expect(edgeId).toMatch(/^edge-/);
      const outputNode = nodeMappingManager.getNodeMapping().nodeMap.get(outputId)! as OutputNode;
      expect(outputNode.inputs[0]).toBeInstanceOf(AVStream);
    });

    it('should throw error when connecting to non-existent node', async () => {
      const sourceId = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'source',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });

      expect(() => nodeMappingManager.addEdgeToMapping(sourceId, 'non-existent', 0, 0)).toThrow(
        'Source or target node not found in mapping'
      );
    });
  });

  describe('removeEdgeFromMapping', () => {
    it('should remove an edge and clear the input', async () => {
      const sourceId = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'source',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });
      const targetId = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'target',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });

      const edgeId = nodeMappingManager.addEdgeToMapping(sourceId, targetId, 0, 0);
      nodeMappingManager.removeEdgeFromMapping(edgeId);

      expect(nodeMappingManager.getEdgeMapping().edgeMap.get(edgeId)).toBeUndefined();
      const targetNode = nodeMappingManager.getNodeMapping().nodeMap.get(targetId)! as FilterNode;
      expect(targetNode.inputs[0]).toBeNull();
    });

    it('should throw error when removing non-existent edge', () => {
      expect(() => nodeMappingManager.removeEdgeFromMapping('non-existent')).toThrow(
        'Edge non-existent not found in mapping'
      );
    });

    it('should handle removing edge from OutputNode', async () => {
      const inputId = await nodeMappingManager.addNodeToMapping({
        type: 'input',
        filename: 'input.mp4',
      });

      const outputId = await nodeMappingManager.addNodeToMapping({
        type: 'output',
        filename: 'output.mp4',
        inputs: [],
      });

      const edgeId = nodeMappingManager.addEdgeToMapping(inputId, outputId, 0, 0);
      nodeMappingManager.removeEdgeFromMapping(edgeId);

      expect(nodeMappingManager.getEdgeMapping().edgeMap.get(edgeId)).toBeUndefined();
      const outputNode = nodeMappingManager.getNodeMapping().nodeMap.get(outputId)! as OutputNode;
      expect(outputNode.inputs[0]).toBeNull();
    });

    it('should handle removing edge from GlobalNode', async () => {
      const outputId = await nodeMappingManager.addNodeToMapping({
        type: 'output',
        filename: 'output.mp4',
        inputs: [],
      });

      const globalId = nodeMappingManager.getGlobalNodeId();
      const edgeId = nodeMappingManager.addEdgeToMapping(outputId, globalId, 0, 0);
      nodeMappingManager.removeEdgeFromMapping(edgeId);

      expect(nodeMappingManager.getEdgeMapping().edgeMap.get(edgeId)).toBeUndefined();
      const globalNode = nodeMappingManager.getGlobalNode();
      expect(globalNode.inputs[0]).toBeNull();
    });
  });

  describe('updateNode', () => {
    it('should update FilterNode properties', async () => {
      const id = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'test',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });

      const newInputTypings = [new StreamType('audio'), new StreamType('video')];
      const newOutputTypings = [new StreamType('av')];
      const newKwargs = { quality: 'high' };

      nodeMappingManager.updateNode(id, {
        input_typings: newInputTypings,
        output_typings: newOutputTypings,
        kwargs: newKwargs,
      });

      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id)! as FilterNode;
      expect(node.input_typings).toEqual(newInputTypings);
      expect(node.output_typings).toEqual(newOutputTypings);
      expect(node.kwargs).toEqual(newKwargs);
      expect(node.inputs).toHaveLength(2);
      expect(node.inputs[0]).toBeNull();
      expect(node.inputs[1]).toBeNull();
    });

    it('should update InputNode properties', async () => {
      const id = await nodeMappingManager.addNodeToMapping({
        type: 'input',
        filename: 'test.mp4',
      });

      const newFilename = 'new.mp4';
      const newKwargs = { format: 'mp4' };

      nodeMappingManager.updateNode(id, {
        filename: newFilename,
        kwargs: newKwargs,
      });

      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id)! as InputNode;
      expect(node.filename).toBe(newFilename);
      expect(node.kwargs).toEqual(newKwargs);
    });

    it('should update OutputNode properties', async () => {
      const id = await nodeMappingManager.addNodeToMapping({
        type: 'output',
        filename: 'test.mp4',
        inputs: [],
      });

      const newFilename = 'new.mp4';
      const newKwargs = { format: 'mp4' };

      nodeMappingManager.updateNode(id, {
        filename: newFilename,
        kwargs: newKwargs,
      });

      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id)! as OutputNode;
      expect(node.filename).toBe(newFilename);
      expect(node.kwargs).toEqual(newKwargs);
    });

    it('should update GlobalNode properties', async () => {
      const id = await nodeMappingManager.addNodeToMapping({
        type: 'global',
        inputs: [],
      });

      const newKwargs = { global: true };

      nodeMappingManager.updateNode(id, {
        kwargs: newKwargs,
      });

      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id)! as GlobalNode;
      expect(node.kwargs).toEqual(newKwargs);
    });

    it('should throw error when node not found', () => {
      expect(() => nodeMappingManager.updateNode('non-existent', {})).toThrow(
        'Node non-existent not found in mapping'
      );
    });
  });

  describe('resetNodeMapping', () => {
    it('should reset both node and edge mappings', async () => {
      const id = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'test',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });
      nodeMappingManager.addEdgeToMapping(id, id, 0, 0);

      nodeMappingManager.resetNodeMapping();

      expect(nodeMappingManager.getNodeMapping().nodeMap.size).toBe(1);
      expect(nodeMappingManager.getEdgeMapping().edgeMap.size).toBe(0);
      expect(nodeMappingManager.getEdgeMapping().reverseMap.size).toBe(0);
    });
  });

  describe('JSON serialization with global node', () => {
    it('should include input node connected to global node in JSON', async () => {
      // Create an input node
      const inputId = await nodeMappingManager.addNodeToMapping({
        type: 'input',
        filename: 'input.mp4',
      });

      // Add output node
      const outputId = await nodeMappingManager.addNodeToMapping({
        type: 'output',
        filename: 'output.mp4',
        inputs: [],
      });

      // Connect input -> output -> global
      nodeMappingManager.addEdgeToMapping(inputId, outputId, 0, 0);
      const globalId = nodeMappingManager.getGlobalNodeId();
      nodeMappingManager.addEdgeToMapping(outputId, globalId, 0, 0);

      // Get JSON representation
      const json = nodeMappingManager.toJson();
      const parsed = JSON.parse(json);

      // Verify global node has the connection chain
      expect(parsed.inputs).toHaveLength(1);
      expect(parsed.inputs[0]).toBeDefined();
      expect(parsed.inputs[0].node.filename).toBe('output.mp4');
      expect(parsed.inputs[0].node.inputs[0].node.filename).toBe('input.mp4');
    });

    it('should include filter node connected to global node in JSON', async () => {
      // Create a filter node
      const filterId = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'test_filter',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });

      // Add output node
      const outputId = await nodeMappingManager.addNodeToMapping({
        type: 'output',
        filename: 'output.mp4',
        inputs: [],
      });

      // Connect filter -> output -> global
      nodeMappingManager.addEdgeToMapping(filterId, outputId, 0, 0);
      const globalId = nodeMappingManager.getGlobalNodeId();
      nodeMappingManager.addEdgeToMapping(outputId, globalId, 0, 0);

      // Get JSON representation
      const json = nodeMappingManager.toJson();
      const parsed = JSON.parse(json);

      // Verify global node has the connection chain
      expect(parsed.inputs).toHaveLength(1);
      expect(parsed.inputs[0]).toBeDefined();
      expect(parsed.inputs[0].node.filename).toBe('output.mp4');
      expect(parsed.inputs[0].node.inputs[0].node.name).toBe('test_filter');
    });

    it('should include multiple nodes connected to global node in JSON', async () => {
      // Create input and filter nodes
      const inputId = await nodeMappingManager.addNodeToMapping({
        type: 'input',
        filename: 'input.mp4',
      });

      const filterId = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'test_filter',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });

      // Add output nodes
      const output1Id = await nodeMappingManager.addNodeToMapping({
        type: 'output',
        filename: 'output1.mp4',
        inputs: [],
      });

      const output2Id = await nodeMappingManager.addNodeToMapping({
        type: 'output',
        filename: 'output2.mp4',
        inputs: [],
      });

      // Connect input -> output1 -> global
      nodeMappingManager.addEdgeToMapping(inputId, output1Id, 0, 0);

      // Connect filter -> output2 -> global
      nodeMappingManager.addEdgeToMapping(filterId, output2Id, 0, 0);

      const globalId = nodeMappingManager.getGlobalNodeId();
      nodeMappingManager.addEdgeToMapping(output1Id, globalId, 0, 0);
      nodeMappingManager.addEdgeToMapping(output2Id, globalId, 0, 1);

      // Get JSON representation
      const json = nodeMappingManager.toJson();
      const parsed = JSON.parse(json);

      // Verify global node has both connections
      expect(parsed.inputs).toHaveLength(2);
      expect(parsed.inputs[0].node.filename).toBe('output1.mp4');
      expect(parsed.inputs[1].node.filename).toBe('output2.mp4');
      expect(parsed.inputs[0].node.inputs[0].node.filename).toBe('input.mp4');
      expect(parsed.inputs[1].node.inputs[0].node.name).toBe('test_filter');
    });

    it('should maintain node properties in JSON when connected to global node', async () => {
      // Create a filter node with kwargs
      const filterId = await nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'test_filter',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
        kwargs: { quality: 'high', format: 'mp4' },
      });

      // Add output node
      const outputId = await nodeMappingManager.addNodeToMapping({
        type: 'output',
        filename: 'output.mp4',
        inputs: [],
      });

      // Connect filter -> output -> global
      nodeMappingManager.addEdgeToMapping(filterId, outputId, 0, 0);
      const globalId = nodeMappingManager.getGlobalNodeId();
      nodeMappingManager.addEdgeToMapping(outputId, globalId, 0, 0);

      // Get JSON representation
      const json = nodeMappingManager.toJson();
      const parsed = JSON.parse(json);

      // Verify node properties are preserved
      expect(parsed.inputs[0].node.inputs[0].node.kwargs).toEqual({
        quality: 'high',
        format: 'mp4',
      });
    });

    it('should handle removing node from global node in JSON', async () => {
      // Create and connect a node to global node
      const inputId = await nodeMappingManager.addNodeToMapping({
        type: 'input',
        filename: 'input.mp4',
      });

      const outputId = await nodeMappingManager.addNodeToMapping({
        type: 'output',
        filename: 'output.mp4',
        inputs: [],
      });
      const globalId = nodeMappingManager.getGlobalNodeId();
      nodeMappingManager.addEdgeToMapping(inputId, outputId, 0, 0);
      const edgeId = nodeMappingManager.addEdgeToMapping(outputId, globalId, 0, 1);

      // Remove the edge between output and global
      nodeMappingManager.removeEdgeFromMapping(edgeId);

      // Get JSON representation
      const json = nodeMappingManager.toJson();
      const parsed = JSON.parse(json);

      // Verify global node has no non-null inputs
      expect(parsed.inputs.filter((i: unknown) => i !== null)).toHaveLength(0);
    });
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
  });

  it.each(testFiles)('should handle $name case', async ({ data }) => {
    const jsonString = JSON.stringify(data);

    // Deserialize
    const deserialized = loads(jsonString);
    await nodeMappingManager.recursiveAddToMapping(
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
      input_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
      output_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
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
      input_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
      output_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
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
