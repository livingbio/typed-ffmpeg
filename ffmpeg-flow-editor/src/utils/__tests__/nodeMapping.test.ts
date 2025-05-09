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
    it('should add a FilterNode to mapping', () => {
      const id = nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'test',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });
      expect(id).toMatch(/^filter-test-/);
      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id)!;
      expect(node).toBeInstanceOf(FilterNode);
      expect(nodeMappingManager.getNodeMapping().reverseMap.get(node)).toBe(id);
    });

    it('should add an InputNode to mapping', () => {
      const id = nodeMappingManager.addNodeToMapping({
        type: 'input',
        filename: 'test.mp4',
      });
      expect(id).toMatch(/^input-/);
      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id)!;
      expect(node).toBeInstanceOf(InputNode);
      expect(nodeMappingManager.getNodeMapping().reverseMap.get(node)).toBe(id);
    });

    it('should add an OutputNode to mapping', () => {
      const id = nodeMappingManager.addNodeToMapping({
        type: 'output',
        filename: 'test.mp4',
        inputs: [],
      });
      expect(id).toMatch(/^output-/);
      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id)!;
      expect(node).toBeInstanceOf(OutputNode);
      expect(nodeMappingManager.getNodeMapping().reverseMap.get(node)).toBe(id);
    });

    it('should add a GlobalNode to mapping', () => {
      const id = nodeMappingManager.addNodeToMapping({
        type: 'global',
        inputs: [],
      });
      expect(id).toMatch(/^global-/);
      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id)!;
      expect(node).toBeInstanceOf(GlobalNode);
      expect(nodeMappingManager.getNodeMapping().reverseMap.get(node)).toBe(id);
    });
  });

  describe('removeNodeFromMapping', () => {
    it('should remove a node from mapping', () => {
      const id = nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'test',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });
      const node = nodeMappingManager.getNodeMapping().nodeMap.get(id)!;
      nodeMappingManager.removeNodeFromMapping(id);
      expect(nodeMappingManager.getNodeMapping().nodeMap.get(id)).toBeUndefined();
      expect(nodeMappingManager.getNodeMapping().reverseMap.get(node)).toBeUndefined();
    });
  });

  describe('addEdgeToMapping', () => {
    it('should add a video stream edge between FilterNodes', () => {
      const sourceId = nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'source',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });
      const targetId = nodeMappingManager.addNodeToMapping({
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

    it('should add an audio stream edge between FilterNodes', () => {
      const sourceId = nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'source',
        input_typings: [new StreamType('audio')],
        output_typings: [new StreamType('audio')],
      });
      const targetId = nodeMappingManager.addNodeToMapping({
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

    it('should add an AV stream edge from InputNode to FilterNode', () => {
      const sourceId = nodeMappingManager.addNodeToMapping({
        type: 'input',
        filename: 'test.mp4',
      });
      const targetId = nodeMappingManager.addNodeToMapping({
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

    it('should throw error when connecting video to audio input', () => {
      const sourceId = nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'source',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });
      const targetId = nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'target',
        input_typings: [new StreamType('audio')],
        output_typings: [new StreamType('audio')],
      });

      expect(() => nodeMappingManager.addEdgeToMapping(sourceId, targetId, 0, 0)).toThrow(
        'Video stream cannot be connected to audio input'
      );
    });

    it('should throw error when connecting audio to video input', () => {
      const sourceId = nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'source',
        input_typings: [new StreamType('audio')],
        output_typings: [new StreamType('audio')],
      });
      const targetId = nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'target',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });

      expect(() => nodeMappingManager.addEdgeToMapping(sourceId, targetId, 0, 0)).toThrow(
        'Audio stream cannot be connected to video input'
      );
    });
  });

  describe('removeEdgeFromMapping', () => {
    it('should remove an edge and clear the input', () => {
      const sourceId = nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'source',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });
      const targetId = nodeMappingManager.addNodeToMapping({
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
  });

  describe('updateNode', () => {
    it('should update FilterNode properties', () => {
      const id = nodeMappingManager.addNodeToMapping({
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

    it('should update InputNode properties', () => {
      const id = nodeMappingManager.addNodeToMapping({
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

    it('should update OutputNode properties', () => {
      const id = nodeMappingManager.addNodeToMapping({
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

    it('should update GlobalNode properties', () => {
      const id = nodeMappingManager.addNodeToMapping({
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
        'Node not found in mapping'
      );
    });
  });

  describe('resetNodeMapping', () => {
    it('should reset both node and edge mappings', () => {
      const id = nodeMappingManager.addNodeToMapping({
        type: 'filter',
        name: 'test',
        input_typings: [new StreamType('video')],
        output_typings: [new StreamType('video')],
      });
      nodeMappingManager.addEdgeToMapping(id, id, 0, 0);

      nodeMappingManager.resetNodeMapping();

      expect(nodeMappingManager.getNodeMapping().nodeMap.size).toBe(1);
      expect(nodeMappingManager.getNodeMapping().reverseMap.size).toBe(1);
      expect(nodeMappingManager.getEdgeMapping().edgeMap.size).toBe(0);
      expect(nodeMappingManager.getEdgeMapping().reverseMap.size).toBe(0);
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

  it.each(testFiles)('should handle $name case', ({ data }) => {
    const jsonString = JSON.stringify(data);

    // Deserialize
    const deserialized = loads(jsonString);
    nodeMappingManager.recursiveAddToMapping(
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
  });
});
