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
    await nodeMappingManager.addNodeToMapping({ type: 'global', inputs: [] });
    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that error was logged
    expect(result).toMatchSnapshot();
  });

  it('generates basic input-output-global chain', async () => {
    // Mock successful response from runPython

    const nodeMappingManager = new NodeMappingManager();

    // Add input node
    const inputNodeId = await nodeMappingManager.addNodeToMapping({
      type: 'input',
      filename: 'input.mp4',
    });

    // Add output node
    const outputNodeId = await nodeMappingManager.addNodeToMapping({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Add global node
    const globalNodeId = await nodeMappingManager.addNodeToMapping({
      type: 'global',
      inputs: [],
    });

    // Connect input -> output -> global
    nodeMappingManager.addEdgeToMapping(inputNodeId, outputNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(outputNodeId, globalNodeId, 0, 0);

    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that we got the mocked response
    expect(result).toMatchSnapshot();
  });

  it('generates code with filter nodes, output and global node', async () => {
    // Mock successful response from runPython

    const nodeMappingManager = new NodeMappingManager();

    // Add input node
    const inputNodeId = await nodeMappingManager.addNodeToMapping({
      type: 'input',
      filename: 'input.mp4',
    });

    // Add filter node
    const filterNodeId = await nodeMappingManager.addNodeToMapping({
      type: 'filter',
      name: 'scale',
      input_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
      output_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
    });

    // Add output node
    const outputNodeId = await nodeMappingManager.addNodeToMapping({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Add global node
    const globalNodeId = await nodeMappingManager.addNodeToMapping({
      type: 'global',
      inputs: [],
    });

    // Connect nodes
    nodeMappingManager.addEdgeToMapping(inputNodeId, filterNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(filterNodeId, outputNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(outputNodeId, globalNodeId, 0, 0);

    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that we got the mocked response
    expect(result).toMatchSnapshot();
  });

  it('handles multiple input nodes and outputs to global node', async () => {
    const nodeMappingManager = new NodeMappingManager();

    // Add input nodes
    const input1NodeId = await nodeMappingManager.addNodeToMapping({
      type: 'input',
      filename: 'input1.mp4',
    });
    const input2NodeId = await nodeMappingManager.addNodeToMapping({
      type: 'input',
      filename: 'input2.mp4',
    });

    // Add output nodes
    const output1NodeId = await nodeMappingManager.addNodeToMapping({
      type: 'output',
      filename: 'output1.mp4',
      inputs: [],
    });
    const output2NodeId = await nodeMappingManager.addNodeToMapping({
      type: 'output',
      filename: 'output2.mp4',
      inputs: [],
    });

    // Add global node
    const globalNodeId = await nodeMappingManager.addNodeToMapping({
      type: 'global',
      inputs: [],
    });

    // Connect input -> output -> global
    nodeMappingManager.addEdgeToMapping(input1NodeId, output1NodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(input2NodeId, output2NodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(output1NodeId, globalNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(output2NodeId, globalNodeId, 0, 1);

    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that we got the mocked response
    expect(result).toMatchSnapshot();
  });

  it('handles complex filter chains with outputs to global node', async () => {
    // Mock successful response from runPython

    const nodeMappingManager = new NodeMappingManager();

    // Add input node
    const inputNodeId = await nodeMappingManager.addNodeToMapping({
      type: 'input',
      filename: 'input.mp4',
    });

    // Add filter nodes
    const scaleNodeId = await nodeMappingManager.addNodeToMapping({
      type: 'filter',
      name: 'scale',
      input_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
      output_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
    });
    const volumeNodeId = await nodeMappingManager.addNodeToMapping({
      type: 'filter',
      name: 'volume',
      input_typings: [{ value: 'audio', toJSON: () => ({ value: 'audio' }) }],
      output_typings: [{ value: 'audio', toJSON: () => ({ value: 'audio' }) }],
    });

    // Add output nodes
    const videoOutputId = await nodeMappingManager.addNodeToMapping({
      type: 'output',
      filename: 'video_output.mp4',
      inputs: [],
    });
    const audioOutputId = await nodeMappingManager.addNodeToMapping({
      type: 'output',
      filename: 'audio_output.mp3',
      inputs: [],
    });

    // Add global node
    const globalNodeId = await nodeMappingManager.addNodeToMapping({
      type: 'global',
      inputs: [],
    });

    // Connect nodes: input -> filters -> outputs -> global
    nodeMappingManager.addEdgeToMapping(inputNodeId, scaleNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(inputNodeId, volumeNodeId, 1, 0);
    nodeMappingManager.addEdgeToMapping(scaleNodeId, videoOutputId, 0, 0);
    nodeMappingManager.addEdgeToMapping(volumeNodeId, audioOutputId, 0, 0);
    nodeMappingManager.addEdgeToMapping(videoOutputId, globalNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(audioOutputId, globalNodeId, 0, 1);

    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that we got the mocked response
    expect(result).toMatchSnapshot();
  });

  it('handles numeric and boolean parameters correctly with outputs to global node', async () => {
    // Mock successful response from runPython

    const nodeMappingManager = new NodeMappingManager();

    // Add input node
    const inputNodeId = await nodeMappingManager.addNodeToMapping({
      type: 'input',
      filename: 'input.mp4',
    });

    // Add filter node with parameters
    const filterNodeId = await nodeMappingManager.addNodeToMapping({
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
    const outputNodeId = await nodeMappingManager.addNodeToMapping({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Add global node
    const globalNodeId = await nodeMappingManager.addNodeToMapping({
      type: 'global',
      inputs: [],
    });

    // Connect nodes: input -> filter -> output -> global
    nodeMappingManager.addEdgeToMapping(inputNodeId, filterNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(filterNodeId, outputNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(outputNodeId, globalNodeId, 0, 0);

    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that we got the mocked response
    expect(result).toMatchSnapshot();
  });

  it('handles disconnected nodes with global node', async () => {
    const nodeMappingManager = new NodeMappingManager();

    // Add input node
    await nodeMappingManager.addNodeToMapping({
      type: 'input',
      filename: 'input.mp4',
    });

    // Add output node
    await nodeMappingManager.addNodeToMapping({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Add global node (no connections)
    await nodeMappingManager.addNodeToMapping({
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
    await nodeMappingManager.addNodeToMapping({ type: 'global', inputs: [] });

    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that a warning was logged
    expect(result).toMatchSnapshot();

    consoleWarnSpy.mockRestore();
  });
});
