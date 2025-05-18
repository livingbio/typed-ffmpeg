import { describe, it, expect, beforeEach, beforeAll, afterEach, vi } from 'vitest';
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
import { evaluateFormula } from '../formulaEvaluator';

// Mock the formulaEvaluator
vi.mock('../formulaEvaluator', () => ({
  evaluateFormula: vi.fn().mockImplementation(async (formula, parameters) => {
    // Simple mock implementation that returns video for 'v', audio for 'a'
    if (formula === 'v') return [{ type: { value: 'video' } }];
    if (formula === 'a') return [{ type: { value: 'audio' } }];
    if (formula === 'v,v') return [{ type: { value: 'video' } }, { type: { value: 'video' } }];
    if (formula === 'a,a') return [{ type: { value: 'audio' } }, { type: { value: 'audio' } }];
    return [];
  }),
}));

// Mock predefined filters
vi.mock('../../types/ffmpeg', () => ({
  predefinedFilters: [
    {
      name: 'test',
      description: 'Test filter',
      ref: 'test',
      is_support_slice_threading: true,
      is_support_timeline: true,
      is_support_framesync: true,
      is_support_command: false,
      is_filter_sink: false,
      is_filter_source: false,
      is_dynamic_input: false,
      is_dynamic_output: false,
      stream_typings_input: [{ type: { value: 'video' } }],
      stream_typings_output: [{ type: { value: 'video' } }],
      formula_typings_input: null,
      formula_typings_output: null,
      pre: [],
      options: [],
    },
    {
      name: 'dynamic_filter',
      description: 'Filter with dynamic io',
      ref: 'test',
      is_support_slice_threading: true,
      is_support_timeline: true,
      is_support_framesync: true,
      is_support_command: false,
      is_filter_sink: false,
      is_filter_source: false,
      is_dynamic_input: true,
      is_dynamic_output: true,
      stream_typings_input: [],
      stream_typings_output: [],
      formula_typings_input: 'v,v',
      formula_typings_output: 'a,a',
      pre: [],
      options: [
        {
          name: 'mode',
          alias: [],
          description: 'operating mode',
          type: { value: 'string' },
          min: null,
          max: null,
          default: 'default',
          required: false,
          choices: [],
          flags: '',
        },
      ],
    },
  ],
}));

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

describe('NodeMappingManager', () => {
  let manager: NodeMappingManager;
  let updateEventFired: boolean;
  let unsubscribe: () => void;

  beforeEach(() => {
    manager = new NodeMappingManager();
    updateEventFired = false;
    unsubscribe = manager.on('update', () => {
      updateEventFired = true;
    });
  });

  afterEach(() => {
    unsubscribe();
  });

  describe('Node Management', () => {
    describe('Adding Nodes', () => {
      it('should add an InputNode with required filename', async () => {
        const id = await manager.addNodeMapping({
          type: 'input',
          filename: 'input.mp4',
        });

        expect(id).toMatch(/^input-/);
        updateEventFired = false;

        // Check that node exists and is the right type
        const node = Array.from(manager.nodeMap.entries()).find(([key]) => key === id)?.[1];
        expect(node).toBeInstanceOf(InputNode);
        expect((node as InputNode).filename).toBe('input.mp4');
      });

      it('should add an OutputNode with required filename', async () => {
        const id = await manager.addNodeMapping({
          type: 'output',
          filename: 'output.mp4',
          inputs: [],
        });

        expect(id).toMatch(/^output-/);
        expect(updateEventFired).toBe(true);

        // Check that node exists and is the right type
        const node = Array.from(manager.nodeMap.entries()).find(([key]) => key === id)?.[1];
        expect(node).toBeInstanceOf(OutputNode);
        expect((node as OutputNode).filename).toBe('output.mp4');
      });

      it('should add a FilterNode with required name', async () => {
        const id = await manager.addNodeMapping({
          type: 'filter',
          name: 'test',
        });

        expect(id).toMatch(/^filter-test-/);
        expect(updateEventFired).toBe(true);

        // Check that node exists and is the right type
        const node = Array.from(manager.nodeMap.entries()).find(([key]) => key === id)?.[1];
        expect(node).toBeInstanceOf(FilterNode);
        expect((node as FilterNode).name).toBe('test');
      });

      it('should add a GlobalNode', async () => {
        const globalId = manager.getGlobalNodeId();
        expect(globalId).toMatch(/^global-/);

        // Global node is created by default
        const node = Array.from(manager.nodeMap.entries()).find(([key]) => key === globalId)?.[1];
        expect(node).toBeInstanceOf(GlobalNode);
      });

      it('should throw error when adding InputNode without filename', async () => {
        await expect(
          manager.addNodeMapping({
            type: 'input',
          })
        ).rejects.toThrow('InputNode requires filename');
      });

      it('should throw error when adding OutputNode without filename', async () => {
        await expect(
          manager.addNodeMapping({
            type: 'output',
            inputs: [],
          })
        ).rejects.toThrow('OutputNode requires filename');
      });

      it('should throw error when adding FilterNode without name', async () => {
        await expect(
          manager.addNodeMapping({
            type: 'filter',
          })
        ).rejects.toThrow('FilterNode requires name');
      });

      it('should throw error when adding non-existent filter', async () => {
        await expect(
          manager.addNodeMapping({
            type: 'filter',
            name: 'non_existent_filter',
          })
        ).rejects.toThrow('Filter non_existent_filter not found');
      });

      it('should handle filter with dynamic input/output typings', async () => {
        const id = await manager.addNodeMapping({
          type: 'filter',
          name: 'dynamic_filter',
          kwargs: { mode: 'special' },
        });

        // Check that evaluateFormula was called with correct parameters
        expect(evaluateFormula).toHaveBeenCalledWith('v,v', { mode: 'special' });
        expect(evaluateFormula).toHaveBeenCalledWith('a,a', { mode: 'special' });

        // Check node properties
        const node = Array.from(manager.nodeMap.entries()).find(
          ([key]) => key === id
        )?.[1] as FilterNode;
        expect(node.input_typings).toHaveLength(2);
        expect(node.output_typings).toHaveLength(2);
        expect(node.inputs).toHaveLength(2);
      });
    });

    describe('Removing Nodes', () => {
      it('should remove a node and all its connected edges', async () => {
        const sourceId = await manager.addNodeMapping({
          type: 'filter',
          name: 'test',
        });

        const targetId = await manager.addNodeMapping({
          type: 'filter',
          name: 'test',
        });

        const edgeId = await manager.addEdgeMapping(sourceId, targetId, 0, 0);

        // Reset update event tracker
        updateEventFired = false;

        // Remove source node
        manager.removeNodeMapping(sourceId);

        expect(updateEventFired).toBe(true);
        expect(manager.nodeMap.has(sourceId)).toBe(false);
        expect(manager.edgeMap.has(edgeId)).toBe(false);

        // Target node should still exist but its input should be null
        const targetNode = Array.from(manager.nodeMap.entries()).find(
          ([key]) => key === targetId
        )?.[1] as FilterNode;
        expect(targetNode).toBeDefined();
        expect(targetNode.inputs[0]).toBeNull();
      });

      it('should throw error when removing non-existent node', () => {
        expect(() => manager.removeNodeMapping('non-existent')).toThrow(
          'Node non-existent not found in mapping'
        );
      });

      it('should reset the node mapping state', async () => {
        // Add some nodes and edges
        const sourceId = await manager.addNodeMapping({
          type: 'filter',
          name: 'test',
        });

        const targetId = await manager.addNodeMapping({
          type: 'filter',
          name: 'test',
        });

        await manager.addEdgeMapping(sourceId, targetId, 0, 0);

        // Reset update event tracker
        updateEventFired = false;

        // Reset the mapping
        manager.resetNodeMapping();

        expect(updateEventFired).toBe(true);
        expect(manager.nodeMap.size).toBe(1); // Only global node remains
        expect(manager.edgeMap.size).toBe(0);

        // Global node should be recreated
        const globalId = manager.getGlobalNodeId();
        expect(manager.nodeMap.has(globalId)).toBe(true);
      });
    });

    describe('Updating Nodes', () => {
      it('should update a FilterNode with new kwargs', async () => {
        const id = await manager.addNodeMapping({
          type: 'filter',
          name: 'test',
        });

        updateEventFired = false;

        await manager.updateNodeMapping(id, {
          kwargs: { quality: 'high' },
        });

        expect(updateEventFired).toBe(true);

        const node = Array.from(manager.nodeMap.entries()).find(
          ([key]) => key === id
        )?.[1] as FilterNode;
        expect(node.kwargs).toEqual({ quality: 'high' });
      });

      it('should update InputNode filename', async () => {
        const id = await manager.addNodeMapping({
          type: 'input',
          filename: 'old.mp4',
        });

        updateEventFired = false;

        await manager.updateNodeMapping(id, {
          filename: 'new.mp4',
        });

        expect(updateEventFired).toBe(true);

        const node = Array.from(manager.nodeMap.entries()).find(
          ([key]) => key === id
        )?.[1] as InputNode;
        expect(node.filename).toBe('new.mp4');
      });

      it('should update OutputNode filename', async () => {
        const id = await manager.addNodeMapping({
          type: 'output',
          filename: 'old.mp4',
          inputs: [],
        });

        updateEventFired = false;

        await manager.updateNodeMapping(id, {
          filename: 'new.mp4',
        });

        expect(updateEventFired).toBe(true);

        const node = Array.from(manager.nodeMap.entries()).find(
          ([key]) => key === id
        )?.[1] as OutputNode;
        expect(node.filename).toBe('new.mp4');
      });

      it('should throw error when updating non-existent node', async () => {
        await expect(manager.updateNodeMapping('non-existent', { kwargs: {} })).rejects.toThrow(
          'Node non-existent not found in mapping'
        );
      });
    });
  });

  describe('Edge Management', () => {
    describe('Adding Edges', () => {
      it('should add a video stream between FilterNodes', async () => {
        const sourceId = await manager.addNodeMapping({
          type: 'filter',
          name: 'test',
        });

        const targetId = await manager.addNodeMapping({
          type: 'filter',
          name: 'test',
        });

        updateEventFired = false;

        const edgeId = await manager.addEdgeMapping(sourceId, targetId, 0, 0);

        expect(updateEventFired).toBe(true);
        expect(edgeId).toMatch(/^edge-/);

        // Target node should have the stream in its inputs
        const targetNode = Array.from(manager.nodeMap.entries()).find(
          ([key]) => key === targetId
        )?.[1] as FilterNode;
        expect(targetNode.inputs[0]).toBeInstanceOf(VideoStream);

        // Edge should be in the mapping
        const edge = Array.from(manager.edgeMap.entries()).find(([key]) => key === edgeId)?.[1];
        expect(edge).toBeInstanceOf(VideoStream);
      });

      it('should throw error when connecting incompatible stream types', async () => {
        // Create a video filter
        const videoFilterId = await manager.addNodeMapping({
          type: 'filter',
          name: 'test',
        });

        // Create a dynamic filter with audio input
        vi.mocked(evaluateFormula).mockImplementationOnce(async () => [
          { type: { value: 'audio' } },
        ]);
        vi.mocked(evaluateFormula).mockImplementationOnce(async () => [
          { type: { value: 'audio' } },
        ]);

        const audioFilterId = await manager.addNodeMapping({
          type: 'filter',
          name: 'dynamic_filter',
        });

        // Try to connect video output to audio input
        await expect(manager.addEdgeMapping(videoFilterId, audioFilterId, 0, 0)).rejects.toThrow(
          'Stream type mismatch'
        );
      });

      it('should throw error when connecting to non-existent node', async () => {
        const sourceId = await manager.addNodeMapping({
          type: 'filter',
          name: 'test',
        });

        await expect(manager.addEdgeMapping(sourceId, 'non-existent', 0, 0)).rejects.toThrow(
          'Source or target node not found in mapping'
        );
      });

      it('should throw error when connecting from non-existent node', async () => {
        const targetId = await manager.addNodeMapping({
          type: 'filter',
          name: 'test',
        });

        await expect(manager.addEdgeMapping('non-existent', targetId, 0, 0)).rejects.toThrow(
          'Source or target node not found in mapping'
        );
      });

      it('should throw error when connecting to invalid source output index', async () => {
        const sourceId = await manager.addNodeMapping({
          type: 'filter',
          name: 'test',
        });

        const targetId = await manager.addNodeMapping({
          type: 'filter',
          name: 'test',
        });

        // Try to connect from non-existent output index
        await expect(manager.addEdgeMapping(sourceId, targetId, 1, 0)).rejects.toThrow(
          'Source node'
        );
      });

      it('should throw error when connecting to invalid target input index', async () => {
        const sourceId = await manager.addNodeMapping({
          type: 'filter',
          name: 'test',
        });

        const targetId = await manager.addNodeMapping({
          type: 'filter',
          name: 'test',
        });

        // Try to connect to non-existent input index
        await expect(manager.addEdgeMapping(sourceId, targetId, 0, 1)).rejects.toThrow(
          'Target node'
        );
      });
    });

    describe('Removing Edges', () => {
      it('should remove an edge and clear the target input', async () => {
        const sourceId = await manager.addNodeMapping({
          type: 'filter',
          name: 'test',
        });

        const targetId = await manager.addNodeMapping({
          type: 'filter',
          name: 'test',
        });

        const edgeId = await manager.addEdgeMapping(sourceId, targetId, 0, 0);

        updateEventFired = false;

        manager.removeEdgeMapping(edgeId);

        expect(updateEventFired).toBe(true);
        expect(manager.edgeMap.has(edgeId)).toBe(false);

        // Target node's input should be null
        const targetNode = Array.from(manager.nodeMap.entries()).find(
          ([key]) => key === targetId
        )?.[1] as FilterNode;
        expect(targetNode.inputs[0]).toBeNull();
      });

      it('should throw error when removing non-existent edge', () => {
        expect(() => manager.removeEdgeMapping('non-existent')).toThrow(
          'Edge non-existent not found in mapping'
        );
      });
    });
  });

  describe('Recursive Creation and Serialization', () => {
    it('should recursively create a complex node graph', async () => {
      // Create a manual graph structure
      const inputNode = new InputNode('input.mp4');
      const filterNode = new FilterNode(
        'test',
        [],
        [new StreamType('video')],
        [new StreamType('video')],
        { quality: 'high' }
      );
      const outputNode = new OutputNode('output.mp4', []);

      // Connect them together
      const avStream = new AVStream(inputNode);
      filterNode.inputs[0] = avStream;

      const videoStream = new VideoStream(filterNode, 0);
      outputNode.inputs[0] = videoStream;

      // Initialize global node with the output
      const globalNode = new GlobalNode([new OutputStream(outputNode)], { global_option: true });

      // Recursively create the mapping
      updateEventFired = false;

      await manager.recursiveCreateMapping(globalNode);

      expect(updateEventFired).toBe(true);

      // Check node and edge counts
      expect(manager.nodeMap.size).toBe(4); // input, filter, output, global
      expect(manager.edgeMap.size).toBe(3); // input->filter, filter->output, output->global

      // Check serialization
      const json = manager.toJson();
      const parsed = JSON.parse(json);

      // Verify the structure
      expect(parsed.__class__).toBe('GlobalNode');
      expect(parsed.inputs).toHaveLength(1);
      expect(parsed.inputs[0].node.__class__).toBe('OutputNode');
      expect(parsed.inputs[0].node.filename).toBe('output.mp4');
      expect(parsed.inputs[0].node.inputs[0].node.__class__).toBe('FilterNode');
      expect(parsed.inputs[0].node.inputs[0].node.name).toBe('test');
      expect(parsed.inputs[0].node.inputs[0].node.inputs[0].node.__class__).toBe('InputNode');
      expect(parsed.inputs[0].node.inputs[0].node.inputs[0].node.filename).toBe('input.mp4');
    });
  });

  describe('Error Handling', () => {
    it('should handle formula evaluation failures gracefully', async () => {
      // Mock a formula evaluation failure
      vi.mocked(evaluateFormula).mockRejectedValueOnce(new Error('Formula evaluation failed'));

      const id = await manager.addNodeMapping({
        type: 'filter',
        name: 'dynamic_filter',
      });

      // Should still create the node with empty typings
      const node = Array.from(manager.nodeMap.entries()).find(
        ([key]) => key === id
      )?.[1] as FilterNode;
      expect(node).toBeDefined();
      expect(node.input_typings).toEqual([]);
      expect(node.output_typings).toEqual([]);
    });
  });
});
