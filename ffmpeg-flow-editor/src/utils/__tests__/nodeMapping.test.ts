import { describe, it, expect, beforeEach, beforeAll, afterEach } from 'vitest';
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
import { nodeMappingManager } from '../nodeMapping';
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
  beforeEach(() => {
    nodeMappingManager.resetNodeMapping();
    nodeMappingManager.enableTestMode();
  });

  afterEach(() => {
    nodeMappingManager.disableTestMode();
  });

  describe('addNodeToMapping', () => {
    it('should add a FilterNode to mapping', () => {
      const node = new FilterNode('test', [], [new StreamType('video')], [new StreamType('video')]);
      const id = nodeMappingManager.addNodeToMapping(node);
      expect(id).toMatch(/^filter-test-/);
      expect(nodeMappingManager.getNodeMapping().nodeMap.get(id)).toBe(node);
      expect(nodeMappingManager.getNodeMapping().reverseMap.get(node)).toBe(id);
    });

    it('should add an InputNode to mapping', () => {
      const node = new InputNode('test.mp4');
      const id = nodeMappingManager.addNodeToMapping(node);
      expect(id).toMatch(/^input-/);
      expect(nodeMappingManager.getNodeMapping().nodeMap.get(id)).toBe(node);
      expect(nodeMappingManager.getNodeMapping().reverseMap.get(node)).toBe(id);
    });

    it('should add an OutputNode to mapping', () => {
      const node = new OutputNode('test.mp4', []);
      const id = nodeMappingManager.addNodeToMapping(node);
      expect(id).toMatch(/^output-/);
      expect(nodeMappingManager.getNodeMapping().nodeMap.get(id)).toBe(node);
      expect(nodeMappingManager.getNodeMapping().reverseMap.get(node)).toBe(id);
    });

    it('should add a GlobalNode to mapping', () => {
      const node = new GlobalNode([]);
      const id = nodeMappingManager.addNodeToMapping(node);
      expect(id).toMatch(/^global-/);
      expect(nodeMappingManager.getNodeMapping().nodeMap.get(id)).toBe(node);
      expect(nodeMappingManager.getNodeMapping().reverseMap.get(node)).toBe(id);
    });
  });

  describe('removeNodeFromMapping', () => {
    it('should remove a node from mapping', () => {
      const node = new FilterNode('test', [], [new StreamType('video')], [new StreamType('video')]);
      const id = nodeMappingManager.addNodeToMapping(node);
      nodeMappingManager.removeNodeFromMapping(id);
      expect(nodeMappingManager.getNodeMapping().nodeMap.get(id)).toBeUndefined();
      expect(nodeMappingManager.getNodeMapping().reverseMap.get(node)).toBeUndefined();
    });
  });

  describe('addEdgeToMapping', () => {
    it('should add a video stream edge between FilterNodes', () => {
      const sourceNode = new FilterNode(
        'source',
        [],
        [new StreamType('video')],
        [new StreamType('video')]
      );
      const targetNode = new FilterNode(
        'target',
        [],
        [new StreamType('video')],
        [new StreamType('video')]
      );
      const sourceId = nodeMappingManager.addNodeToMapping(sourceNode);
      const targetId = nodeMappingManager.addNodeToMapping(targetNode);

      const edgeId = nodeMappingManager.addEdgeToMapping(sourceId, targetId, 0, 0);
      expect(edgeId).toMatch(/^edge-/);
      expect(nodeMappingManager.getEdgeMapping().edgeMap.get(edgeId)).toBeInstanceOf(VideoStream);
      expect(targetNode.inputs[0]).toBeInstanceOf(VideoStream);
    });

    it('should add an audio stream edge between FilterNodes', () => {
      const sourceNode = new FilterNode(
        'source',
        [],
        [new StreamType('audio')],
        [new StreamType('audio')]
      );
      const targetNode = new FilterNode(
        'target',
        [],
        [new StreamType('audio')],
        [new StreamType('audio')]
      );
      const sourceId = nodeMappingManager.addNodeToMapping(sourceNode);
      const targetId = nodeMappingManager.addNodeToMapping(targetNode);

      const edgeId = nodeMappingManager.addEdgeToMapping(sourceId, targetId, 0, 0);
      expect(edgeId).toMatch(/^edge-/);
      expect(nodeMappingManager.getEdgeMapping().edgeMap.get(edgeId)).toBeInstanceOf(AudioStream);
      expect(targetNode.inputs[0]).toBeInstanceOf(AudioStream);
    });

    it('should add an AV stream edge from InputNode to FilterNode', () => {
      const sourceNode = new InputNode('test.mp4');
      const targetNode = new FilterNode(
        'target',
        [],
        [new StreamType('av')],
        [new StreamType('av')]
      );
      const sourceId = nodeMappingManager.addNodeToMapping(sourceNode);
      const targetId = nodeMappingManager.addNodeToMapping(targetNode);

      const edgeId = nodeMappingManager.addEdgeToMapping(sourceId, targetId, 0, 0);
      expect(edgeId).toMatch(/^edge-/);
      expect(nodeMappingManager.getEdgeMapping().edgeMap.get(edgeId)).toBeInstanceOf(AVStream);
      expect(targetNode.inputs[0]).toBeInstanceOf(AVStream);
    });

    it('should throw error when connecting video to audio input', () => {
      const sourceNode = new FilterNode(
        'source',
        [],
        [new StreamType('video')],
        [new StreamType('video')]
      );
      const targetNode = new FilterNode(
        'target',
        [],
        [new StreamType('audio')],
        [new StreamType('audio')]
      );
      const sourceId = nodeMappingManager.addNodeToMapping(sourceNode);
      const targetId = nodeMappingManager.addNodeToMapping(targetNode);

      expect(() => nodeMappingManager.addEdgeToMapping(sourceId, targetId, 0, 0)).toThrow(
        'Video stream cannot be connected to audio input'
      );
    });

    it('should throw error when connecting audio to video input', () => {
      const sourceNode = new FilterNode(
        'source',
        [],
        [new StreamType('audio')],
        [new StreamType('audio')]
      );
      const targetNode = new FilterNode(
        'target',
        [],
        [new StreamType('video')],
        [new StreamType('video')]
      );
      const sourceId = nodeMappingManager.addNodeToMapping(sourceNode);
      const targetId = nodeMappingManager.addNodeToMapping(targetNode);

      expect(() => nodeMappingManager.addEdgeToMapping(sourceId, targetId, 0, 0)).toThrow(
        'Audio stream cannot be connected to video input'
      );
    });
  });

  describe('removeEdgeFromMapping', () => {
    it('should remove an edge and clear the input', () => {
      const sourceNode = new FilterNode(
        'source',
        [],
        [new StreamType('video')],
        [new StreamType('video')]
      );
      const targetNode = new FilterNode(
        'target',
        [],
        [new StreamType('video')],
        [new StreamType('video')]
      );
      const sourceId = nodeMappingManager.addNodeToMapping(sourceNode);
      const targetId = nodeMappingManager.addNodeToMapping(targetNode);

      const edgeId = nodeMappingManager.addEdgeToMapping(sourceId, targetId, 0, 0);
      nodeMappingManager.removeEdgeFromMapping(edgeId);

      expect(nodeMappingManager.getEdgeMapping().edgeMap.get(edgeId)).toBeUndefined();
      expect(targetNode.inputs[0]).toBeNull();
    });
  });

  describe('updateNode', () => {
    it('should update FilterNode properties', () => {
      const node = new FilterNode('test', [], [new StreamType('video')], [new StreamType('video')]);
      const id = nodeMappingManager.addNodeToMapping(node);

      const newInputTypings = [new StreamType('audio'), new StreamType('video')];
      const newOutputTypings = [new StreamType('av')];
      const newKwargs = { quality: 'high' };

      nodeMappingManager.updateNode(id, {
        input_typings: newInputTypings,
        output_typings: newOutputTypings,
        kwargs: newKwargs,
      });

      expect(node.input_typings).toEqual(newInputTypings);
      expect(node.output_typings).toEqual(newOutputTypings);
      expect(node.kwargs).toEqual(newKwargs);
      expect(node.inputs).toHaveLength(2);
      expect(node.inputs[0]).toBeNull();
      expect(node.inputs[1]).toBeNull();
    });

    it('should update InputNode properties', () => {
      const node = new InputNode('test.mp4');
      const id = nodeMappingManager.addNodeToMapping(node);

      const newFilename = 'new.mp4';
      const newKwargs = { format: 'mp4' };

      nodeMappingManager.updateNode(id, {
        filename: newFilename,
        kwargs: newKwargs,
      });

      expect(node.filename).toBe(newFilename);
      expect(node.kwargs).toEqual(newKwargs);
    });

    it('should update OutputNode properties', () => {
      const node = new OutputNode('test.mp4', []);
      const id = nodeMappingManager.addNodeToMapping(node);

      const newFilename = 'new.mp4';
      const newKwargs = { format: 'mp4' };

      nodeMappingManager.updateNode(id, {
        filename: newFilename,
        kwargs: newKwargs,
      });

      expect(node.filename).toBe(newFilename);
      expect(node.kwargs).toEqual(newKwargs);
    });

    it('should update GlobalNode properties', () => {
      const node = new GlobalNode([]);
      const id = nodeMappingManager.addNodeToMapping(node);

      const newKwargs = { global: true };

      nodeMappingManager.updateNode(id, {
        kwargs: newKwargs,
      });

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
      const node = new FilterNode('test', [], [new StreamType('video')], [new StreamType('video')]);
      const id = nodeMappingManager.addNodeToMapping(node);
      nodeMappingManager.addEdgeToMapping(id, id, 0, 0);

      nodeMappingManager.resetNodeMapping();

      expect(nodeMappingManager.getNodeMapping().nodeMap.size).toBe(0);
      expect(nodeMappingManager.getNodeMapping().reverseMap.size).toBe(0);
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
