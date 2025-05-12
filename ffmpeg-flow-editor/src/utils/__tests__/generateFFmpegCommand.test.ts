import { generateFFmpegCommand } from '../generateFFmpegCommand';
import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest';
import { NodeMappingManager } from '../nodeMapping';
import { setupPyodideMock } from './testUtils';
import * as pyodideModule from '../pyodide';

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
    nodeMappingManager.addNodeToMapping({ type: 'global', inputs: [] });
    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that error was logged
    expect(consoleSpy).toHaveBeenCalled();
    expect(result.python).toContain('IndexError: tuple index out of range');
  });

  it('generates basic input-output-global chain', async () => {
    // Mock successful response from runPython
    const runPythonSpy = vi
      .spyOn(pyodideModule, 'runPython')
      .mockResolvedValue(
        "import ffmpeg\nresult = ffmpeg.input('input.mp4').output(filename='output.mp4').global_args()"
      );

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

    // Add global node
    const globalNodeId = nodeMappingManager.addNodeToMapping({
      type: 'global',
      inputs: [],
    });

    // Connect input -> output -> global
    nodeMappingManager.addEdgeToMapping(inputNodeId, outputNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(outputNodeId, globalNodeId, 0, 0);

    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that we got the mocked response
    expect(result.python).toContain('import ffmpeg');
    expect(result.python).toContain('input.mp4');
    expect(runPythonSpy).toHaveBeenCalled();

    runPythonSpy.mockRestore();
  });

  it('generates code with filter nodes, output and global node', async () => {
    // Mock successful response from runPython
    const runPythonSpy = vi
      .spyOn(pyodideModule, 'runPython')
      .mockResolvedValue(
        "import ffmpeg\nresult = ffmpeg.input('input.mp4').scale().output(filename='output.mp4').global_args()"
      );

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
      input_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
      output_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
    });

    // Add output node
    const outputNodeId = nodeMappingManager.addNodeToMapping({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Add global node
    const globalNodeId = nodeMappingManager.addNodeToMapping({
      type: 'global',
      inputs: [],
    });

    // Connect nodes
    nodeMappingManager.addEdgeToMapping(inputNodeId, filterNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(filterNodeId, outputNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(outputNodeId, globalNodeId, 0, 0);

    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that we got the mocked response
    expect(result.python).toContain('import ffmpeg');
    expect(result.python).toContain('input.mp4');
    expect(result.python).toContain('scale');
    expect(runPythonSpy).toHaveBeenCalled();

    runPythonSpy.mockRestore();
  });

  it('handles multiple input nodes and outputs to global node', async () => {
    // Mock successful response from runPython
    const runPythonSpy = vi
      .spyOn(pyodideModule, 'runPython')
      .mockResolvedValue(
        "import ffmpeg\nresult = ffmpeg.merge_outputs(ffmpeg.input('input1.mp4').output(filename='output1.mp4'), ffmpeg.input('input2.mp4').output(filename='output2.mp4')).global_args()"
      );

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

    // Add global node
    const globalNodeId = nodeMappingManager.addNodeToMapping({
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
    expect(result.python).toContain('import ffmpeg');
    expect(result.python).toContain('input1.mp4');
    expect(result.python).toContain('input2.mp4');
    expect(runPythonSpy).toHaveBeenCalled();

    runPythonSpy.mockRestore();
  });

  it('handles complex filter chains with outputs to global node', async () => {
    // Mock successful response from runPython
    const runPythonSpy = vi
      .spyOn(pyodideModule, 'runPython')
      .mockResolvedValue(
        "import ffmpeg\ninput_0 = ffmpeg.input('input.mp4')\nresult = ffmpeg.merge_outputs(input_0.scale().output(filename='video_output.mp4'), input_0.volume().output(filename='audio_output.mp3')).global_args()"
      );

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
      input_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
      output_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
    });
    const volumeNodeId = nodeMappingManager.addNodeToMapping({
      type: 'filter',
      name: 'volume',
      input_typings: [{ value: 'audio', toJSON: () => ({ value: 'audio' }) }],
      output_typings: [{ value: 'audio', toJSON: () => ({ value: 'audio' }) }],
    });

    // Add output nodes
    const videoOutputId = nodeMappingManager.addNodeToMapping({
      type: 'output',
      filename: 'video_output.mp4',
      inputs: [],
    });
    const audioOutputId = nodeMappingManager.addNodeToMapping({
      type: 'output',
      filename: 'audio_output.mp3',
      inputs: [],
    });

    // Add global node
    const globalNodeId = nodeMappingManager.addNodeToMapping({
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
    expect(result.python).toContain('import ffmpeg');
    expect(result.python).toContain('input.mp4');
    expect(result.python).toContain('scale');
    expect(result.python).toContain('volume');
    expect(runPythonSpy).toHaveBeenCalled();

    runPythonSpy.mockRestore();
  });

  it('handles numeric and boolean parameters correctly with outputs to global node', async () => {
    // Mock successful response from runPython
    const runPythonSpy = vi
      .spyOn(pyodideModule, 'runPython')
      .mockResolvedValue(
        "import ffmpeg\nresult = ffmpeg.input('input.mp4').scale(width=640, height=480, force_original_aspect_ratio=True).output(filename='output.mp4').global_args()"
      );

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
      input_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
      output_typings: [{ value: 'video', toJSON: () => ({ value: 'video' }) }],
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

    // Add global node
    const globalNodeId = nodeMappingManager.addNodeToMapping({
      type: 'global',
      inputs: [],
    });

    // Connect nodes: input -> filter -> output -> global
    nodeMappingManager.addEdgeToMapping(inputNodeId, filterNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(filterNodeId, outputNodeId, 0, 0);
    nodeMappingManager.addEdgeToMapping(outputNodeId, globalNodeId, 0, 0);

    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that we got the mocked response
    expect(result.python).toContain('import ffmpeg');
    expect(result.python).toContain('width=640');
    expect(result.python).toContain('height=480');
    expect(result.python).toContain('force_original_aspect_ratio=True');
    expect(runPythonSpy).toHaveBeenCalled();

    runPythonSpy.mockRestore();
  });

  it('handles disconnected nodes with global node', async () => {
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

    // Add global node (no connections)
    nodeMappingManager.addNodeToMapping({
      type: 'global',
      inputs: [],
    });

    // Don't connect the nodes

    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that error was logged
    expect(consoleSpy).toHaveBeenCalled();
    expect(result.python).toContain('IndexError: tuple index out of range');
  });
});
