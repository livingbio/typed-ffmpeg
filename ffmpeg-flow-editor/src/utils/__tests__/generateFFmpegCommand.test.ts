import { generateFFmpegCommand } from '../generateFFmpegCommand';
import { describe, it, expect, beforeEach } from 'vitest';
import { NodeMappingManager } from '../nodeMapping';
import { setupPyodideMock } from './testUtils';
import { StreamType } from '../../types/dag';

describe('generateFFmpegCommand', () => {
  beforeEach(() => {
    setupPyodideMock();
  });

  it('returns empty python string if no input or output nodes', async () => {
    const nodeMappingManager = new NodeMappingManager();
    // Add a global node with no inputs
    nodeMappingManager.addNodeToMapping({ type: 'global', inputs: [] });
    const result = await generateFFmpegCommand(nodeMappingManager);
    expect(result.python).toBe('');
  });

  it('generates basic input-global chain', async () => {
    const nodeMappingManager = new NodeMappingManager();

    // Add input node
    const inputNodeId = nodeMappingManager.addNodeToMapping({
      type: 'input',
      filename: 'input.mp4',
    });

    // Add global node
    const globalNodeId = nodeMappingManager.addNodeToMapping({
      type: 'global',
      inputs: [],
    });

    // Connect input to global
    nodeMappingManager.addEdgeToMapping(inputNodeId, globalNodeId, 0, 0);

    const result = await generateFFmpegCommand(nodeMappingManager);
    expect(result.python).toContain('input.mp4');
  });

  it('generates code with filter nodes and global node', async () => {
    const nodeMappingManager = new NodeMappingManager();

    // Add input node
    const inputNodeId = nodeMappingManager.addNodeToMapping({
      type: 'input',
      filename: 'input.mp4',
    });

    // Add filter node
    const filterNodeId = nodeMappingManager.addNodeToMapping({
      type: 'filter',
      name: 'scale',
      input_typings: [new StreamType('video')],
      output_typings: [new StreamType('video')],
    });

    // Add global node
    const globalNodeId = nodeMappingManager.addNodeToMapping({
      type: 'global',
      inputs: [],
    });

    // Connect nodes
    nodeMappingManager.addEdgeToMapping(inputNodeId, filterNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(filterNodeId, globalNodeId, 0, 0);

    const result = await generateFFmpegCommand(nodeMappingManager);
    expect(result.python).toContain('input.mp4');
    expect(result.python).toContain('scale');
  });

  it('handles multiple input nodes and global node', async () => {
    const nodeMappingManager = new NodeMappingManager();

    // Add input nodes
    const input1NodeId = nodeMappingManager.addNodeToMapping({
      type: 'input',
      filename: 'input1.mp4',
    });
    const input2NodeId = nodeMappingManager.addNodeToMapping({
      type: 'input',
      filename: 'input2.mp4',
    });

    // Add global node
    const globalNodeId = nodeMappingManager.addNodeToMapping({
      type: 'global',
      inputs: [],
    });

    // Connect nodes
    nodeMappingManager.addEdgeToMapping(input1NodeId, globalNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(input2NodeId, globalNodeId, 0, 1);

    const result = await generateFFmpegCommand(nodeMappingManager);
    expect(result.python).toContain('input1.mp4');
    expect(result.python).toContain('input2.mp4');
  });

  it('handles complex filter chains with global node', async () => {
    const nodeMappingManager = new NodeMappingManager();

    // Add input node
    const inputNodeId = nodeMappingManager.addNodeToMapping({
      type: 'input',
      filename: 'input.mp4',
    });

    // Add filter nodes
    const scaleNodeId = nodeMappingManager.addNodeToMapping({
      type: 'filter',
      name: 'scale',
      input_typings: [new StreamType('video')],
      output_typings: [new StreamType('video')],
    });
    const volumeNodeId = nodeMappingManager.addNodeToMapping({
      type: 'filter',
      name: 'volume',
      input_typings: [new StreamType('audio')],
      output_typings: [new StreamType('audio')],
    });

    // Add global node
    const globalNodeId = nodeMappingManager.addNodeToMapping({
      type: 'global',
      inputs: [],
    });

    // Connect nodes
    nodeMappingManager.addEdgeToMapping(inputNodeId, scaleNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(inputNodeId, volumeNodeId, 1, 0);
    nodeMappingManager.addEdgeToMapping(scaleNodeId, globalNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(volumeNodeId, globalNodeId, 0, 1);

    const result = await generateFFmpegCommand(nodeMappingManager);
    expect(result.python).toContain('input.mp4');
    expect(result.python).toContain('scale');
    expect(result.python).toContain('volume');
  });

  it('handles numeric and boolean parameters correctly with global node', async () => {
    const nodeMappingManager = new NodeMappingManager();

    // Add input node
    const inputNodeId = nodeMappingManager.addNodeToMapping({
      type: 'input',
      filename: 'input.mp4',
    });

    // Add filter node with parameters
    const filterNodeId = nodeMappingManager.addNodeToMapping({
      type: 'filter',
      name: 'scale',
      input_typings: [new StreamType('video')],
      output_typings: [new StreamType('video')],
      kwargs: {
        width: 640,
        height: 480,
        force_original_aspect_ratio: true,
      },
    });

    // Add global node
    const globalNodeId = nodeMappingManager.addNodeToMapping({
      type: 'global',
      inputs: [],
    });

    // Connect nodes
    nodeMappingManager.addEdgeToMapping(inputNodeId, filterNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(filterNodeId, globalNodeId, 0, 0);

    const result = await generateFFmpegCommand(nodeMappingManager);
    expect(result.python).toContain('width=640');
    expect(result.python).toContain('height=480');
    expect(result.python).toContain('force_original_aspect_ratio=true');
  });

  it('handles disconnected nodes with global node', async () => {
    const nodeMappingManager = new NodeMappingManager();

    // Add input node
    nodeMappingManager.addNodeToMapping({
      type: 'input',
      filename: 'input.mp4',
    });

    // Add global node (no connections)
    nodeMappingManager.addNodeToMapping({
      type: 'global',
      inputs: [],
    });

    // Don't connect the nodes

    const result = await generateFFmpegCommand(nodeMappingManager);
    expect(result.python).toBe('');
  });
});
