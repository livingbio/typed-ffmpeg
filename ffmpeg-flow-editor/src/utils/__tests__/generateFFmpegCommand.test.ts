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
    const result = await generateFFmpegCommand(nodeMappingManager);
    expect(result.python).toBe('');
  });

  it('generates basic input-output chain', async () => {
    const nodeMappingManager = new NodeMappingManager();

    // Add input node
    const inputNodeId = nodeMappingManager.addNodeToMapping({
      type: 'input',
      filename: 'input.mp4',
    });

    // Add output node
    const outputNodeId = nodeMappingManager.addNodeToMapping({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Connect input to output
    nodeMappingManager.addEdgeToMapping(inputNodeId, outputNodeId, 0, 0);

    const result = await generateFFmpegCommand(nodeMappingManager);
    expect(result.python).toContain('input.mp4');
    expect(result.python).toContain('output.mp4');
  });

  it('generates code with filter nodes', async () => {
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

    // Add output node
    const outputNodeId = nodeMappingManager.addNodeToMapping({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Connect nodes
    nodeMappingManager.addEdgeToMapping(inputNodeId, filterNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(filterNodeId, outputNodeId, 0, 0);

    const result = await generateFFmpegCommand(nodeMappingManager);
    expect(result.python).toContain('input.mp4');
    expect(result.python).toContain('scale');
    expect(result.python).toContain('output.mp4');
  });

  it('handles multiple input and output nodes', async () => {
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

    // Add output nodes
    const output1NodeId = nodeMappingManager.addNodeToMapping({
      type: 'output',
      filename: 'output1.mp4',
      inputs: [],
    });
    const output2NodeId = nodeMappingManager.addNodeToMapping({
      type: 'output',
      filename: 'output2.mp4',
      inputs: [],
    });

    // Connect nodes
    nodeMappingManager.addEdgeToMapping(input1NodeId, output1NodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(input2NodeId, output2NodeId, 0, 0);

    const result = await generateFFmpegCommand(nodeMappingManager);
    expect(result.python).toContain('input1.mp4');
    expect(result.python).toContain('input2.mp4');
    expect(result.python).toContain('output1.mp4');
    expect(result.python).toContain('output2.mp4');
  });

  it('handles complex filter chains', async () => {
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

    // Add output node
    const outputNodeId = nodeMappingManager.addNodeToMapping({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Connect nodes
    nodeMappingManager.addEdgeToMapping(inputNodeId, scaleNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(inputNodeId, volumeNodeId, 1, 0);
    nodeMappingManager.addEdgeToMapping(scaleNodeId, outputNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(volumeNodeId, outputNodeId, 0, 1);

    const result = await generateFFmpegCommand(nodeMappingManager);
    expect(result.python).toContain('input.mp4');
    expect(result.python).toContain('scale');
    expect(result.python).toContain('volume');
    expect(result.python).toContain('output.mp4');
  });

  it('handles numeric and boolean parameters correctly', async () => {
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

    // Add output node
    const outputNodeId = nodeMappingManager.addNodeToMapping({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Connect nodes
    nodeMappingManager.addEdgeToMapping(inputNodeId, filterNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(filterNodeId, outputNodeId, 0, 0);

    const result = await generateFFmpegCommand(nodeMappingManager);
    expect(result.python).toContain('width=640');
    expect(result.python).toContain('height=480');
    expect(result.python).toContain('force_original_aspect_ratio=true');
  });

  it('handles disconnected nodes', async () => {
    const nodeMappingManager = new NodeMappingManager();

    // Add input node
    nodeMappingManager.addNodeToMapping({
      type: 'input',
      filename: 'input.mp4',
    });

    // Add output node
    nodeMappingManager.addNodeToMapping({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Don't connect the nodes

    const result = await generateFFmpegCommand(nodeMappingManager);
    expect(result.python).toBe('');
  });
});
