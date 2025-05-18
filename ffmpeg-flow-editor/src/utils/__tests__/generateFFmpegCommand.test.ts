import { generateFFmpegCommand } from '../generateFFmpegCommand';
import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest';
import { NodeMappingManager } from '../nodeMapping';
import { setupPyodideMock } from './testUtils';
import * as pyodideModule from '../pyodideUtils';

describe('generateFFmpegCommand', () => {
  let consoleSpy: ReturnType<typeof vi.spyOn>;

  beforeEach(() => {
    setupPyodideMock();
    consoleSpy = vi.spyOn(console, 'error').mockImplementation(() => {});
  });

  afterEach(() => {
    consoleSpy.mockRestore();
  });

  it('returns error message if no input or output nodes', async () => {
    const nodeMappingManager = new NodeMappingManager();
    // Add a global node with no inputs
    nodeMappingManager.addNodeMapping({ type: 'global', inputs: [] });
    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that error was logged
    expect(result).toMatchSnapshot();
  });

  it('generates basic input-output-global chain', async () => {
    // Mock successful response from runPython

    const nodeMappingManager = new NodeMappingManager();

    // Add input node
    const inputNodeId = nodeMappingManager.addNodeMapping({
      type: 'input',
      filename: 'input.mp4',
    });

    // Add output node
    const outputNodeId = nodeMappingManager.addNodeMapping({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Add global node
    const globalNodeId = nodeMappingManager.addNodeMapping({
      type: 'global',
      inputs: [],
    });

    // Connect input -> output -> global
    nodeMappingManager.addEdgeMapping(inputNodeId, outputNodeId, 0, 0);
    nodeMappingManager.addEdgeMapping(outputNodeId, globalNodeId, 0, 0);

    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that we got the mocked response
    expect(result).toMatchSnapshot();
  });

  it('generates code with filter nodes, output and global node', async () => {
    // Mock successful response from runPython

    const nodeMappingManager = new NodeMappingManager();

    // Add input node
    const inputNodeId = nodeMappingManager.addNodeMapping({
      type: 'input',
      filename: 'input.mp4',
    });

    // Add filter node
    const filterNodeId = nodeMappingManager.addNodeMapping({
      type: 'filter',
      name: 'scale',
      input_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
      output_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
    });

    // Add output node
    const outputNodeId = nodeMappingManager.addNodeMapping({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Add global node
    const globalNodeId = nodeMappingManager.addNodeMapping({
      type: 'global',
      inputs: [],
    });

    // Connect nodes
    nodeMappingManager.addEdgeMapping(inputNodeId, filterNodeId, 0, 0);
    nodeMappingManager.addEdgeMapping(filterNodeId, outputNodeId, 0, 0);
    nodeMappingManager.addEdgeMapping(outputNodeId, globalNodeId, 0, 0);

    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that we got the mocked response
    expect(result).toMatchSnapshot();
  });

  it('handles multiple input nodes and outputs to global node', async () => {
    const nodeMappingManager = new NodeMappingManager();

    // Add input nodes
    const input1NodeId = nodeMappingManager.addNodeMapping({
      type: 'input',
      filename: 'input1.mp4',
    });
    const input2NodeId = nodeMappingManager.addNodeMapping({
      type: 'input',
      filename: 'input2.mp4',
    });

    // Add output nodes
    const output1NodeId = nodeMappingManager.addNodeMapping({
      type: 'output',
      filename: 'output1.mp4',
      inputs: [],
    });
    const output2NodeId = nodeMappingManager.addNodeMapping({
      type: 'output',
      filename: 'output2.mp4',
      inputs: [],
    });

    // Add global node
    const globalNodeId = nodeMappingManager.addNodeMapping({
      type: 'global',
      inputs: [],
    });

    // Connect input -> output -> global
    nodeMappingManager.addEdgeMapping(input1NodeId, output1NodeId, 0, 0);
    nodeMappingManager.addEdgeMapping(input2NodeId, output2NodeId, 0, 0);
    nodeMappingManager.addEdgeMapping(output1NodeId, globalNodeId, 0, 0);
    nodeMappingManager.addEdgeMapping(output2NodeId, globalNodeId, 0, 1);

    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that we got the mocked response
    expect(result).toMatchSnapshot();
  });

  it('handles complex filter chains with outputs to global node', async () => {
    // Mock successful response from runPython

    const nodeMappingManager = new NodeMappingManager();

    // Add input node
    const inputNodeId = nodeMappingManager.addNodeMapping({
      type: 'input',
      filename: 'input.mp4',
    });

    // Add filter nodes
    const scaleNodeId = nodeMappingManager.addNodeMapping({
      type: 'filter',
      name: 'scale',
      input_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
      output_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
    });
    const volumeNodeId = nodeMappingManager.addNodeMapping({
      type: 'filter',
      name: 'volume',
      input_typings: [{ value: 'audio', toJSON: () => ({ value: 'audio' }) }],
      output_typings: [{ value: 'audio', toJSON: () => ({ value: 'audio' }) }],
    });

    // Add output nodes
    const videoOutputId = nodeMappingManager.addNodeMapping({
      type: 'output',
      filename: 'video_output.mp4',
      inputs: [],
    });
    const audioOutputId = nodeMappingManager.addNodeMapping({
      type: 'output',
      filename: 'audio_output.mp3',
      inputs: [],
    });

    // Add global node
    const globalNodeId = nodeMappingManager.addNodeMapping({
      type: 'global',
      inputs: [],
    });

    // Connect nodes: input -> filters -> outputs -> global
    nodeMappingManager.addEdgeMapping(inputNodeId, scaleNodeId, 0, 0);
    nodeMappingManager.addEdgeMapping(inputNodeId, volumeNodeId, 1, 0);
    nodeMappingManager.addEdgeMapping(scaleNodeId, videoOutputId, 0, 0);
    nodeMappingManager.addEdgeMapping(volumeNodeId, audioOutputId, 0, 0);
    nodeMappingManager.addEdgeMapping(videoOutputId, globalNodeId, 0, 0);
    nodeMappingManager.addEdgeMapping(audioOutputId, globalNodeId, 0, 1);

    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that we got the mocked response
    expect(result).toMatchSnapshot();
  });

  it('handles numeric and boolean parameters correctly with outputs to global node', async () => {
    // Mock successful response from runPython

    const nodeMappingManager = new NodeMappingManager();

    // Add input node
    const inputNodeId = nodeMappingManager.addNodeMapping({
      type: 'input',
      filename: 'input.mp4',
    });

    // Add filter node with parameters
    const filterNodeId = nodeMappingManager.addNodeMapping({
      type: 'filter',
      name: 'scale',
      input_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
      output_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
      kwargs: {
        width: 640,
        height: 480,
        force_original_aspect_ratio: true,
      },
    });

    // Add output node
    const outputNodeId = nodeMappingManager.addNodeMapping({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Add global node
    const globalNodeId = nodeMappingManager.addNodeMapping({
      type: 'global',
      inputs: [],
    });

    // Connect nodes: input -> filter -> output -> global
    nodeMappingManager.addEdgeMapping(inputNodeId, filterNodeId, 0, 0);
    nodeMappingManager.addEdgeMapping(filterNodeId, outputNodeId, 0, 0);
    nodeMappingManager.addEdgeMapping(outputNodeId, globalNodeId, 0, 0);

    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that we got the mocked response
    expect(result).toMatchSnapshot();
  });

  it('handles disconnected nodes with global node', async () => {
    const nodeMappingManager = new NodeMappingManager();

    // Add input node
    nodeMappingManager.addNodeMapping({
      type: 'input',
      filename: 'input.mp4',
    });

    // Add output node
    nodeMappingManager.addNodeMapping({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Add global node (no connections)
    nodeMappingManager.addNodeMapping({
      type: 'global',
      inputs: [],
    });

    // Don't connect the nodes

    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that error was logged
    expect(result).toMatchSnapshot();
  });

  it('handles empty result from Python execution', async () => {
    // Mock empty response from runPython
    const consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});

    const nodeMappingManager = new NodeMappingManager();

    // Add a global node with no inputs
    nodeMappingManager.addNodeMapping({ type: 'global', inputs: [] });

    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that a warning was logged
    expect(result).toMatchSnapshot();

    consoleWarnSpy.mockRestore();
  });
});
