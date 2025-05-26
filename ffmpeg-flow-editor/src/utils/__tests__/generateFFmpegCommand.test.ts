import { generateFFmpegPythonCode, generateFFmpegCommand } from '../generateFFmpegCommand';
import { describe, it, expect, beforeEach } from 'vitest';
import { NodeMappingManager } from '../nodeMapping';
import { setupPyodideMock } from './testUtils';

describe('generateFFmpegCommand', () => {
  beforeEach(() => {
    setupPyodideMock();
  });

  it('returns error message if no input or output nodes', async () => {
    const nodeMappingManager = new NodeMappingManager();
    // Add a global node with no inputs
    nodeMappingManager.addNode({ type: 'global', inputs: [] });
    const result = await generateFFmpegCommand(nodeMappingManager.toJson());

    // Check that error was logged
    expect(result).toMatchSnapshot();
    expect(result.error).toBeDefined();
  });

  it('generates basic input-output-global chain command', async () => {
    const nodeMapping = new NodeMappingManager();

    // Add nodes to mapping
    const inputId = await nodeMapping.addNode({
      type: 'input',
      filename: 'input.mp4',
    });
    const outputId = await nodeMapping.addNode({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Connect input -> output -> global
    nodeMapping.addEdge(inputId, outputId, 0, 0);
    const globalId = nodeMapping.getGlobalNodeId();
    nodeMapping.addEdge(outputId, globalId, 0, 0);

    const result = await generateFFmpegCommand(nodeMapping.toJson());
    expect(result).toMatchSnapshot();
    expect(result.error).toBeNull();
    expect(result.result).toContain('ffmpeg');
    expect(result.result).toContain('input.mp4');
    expect(result.result).toContain('output.mp4');
  });

  it('generates command with filter nodes, output and global node', async () => {
    const nodeMapping = new NodeMappingManager();

    // Add nodes to mapping
    const inputId = await nodeMapping.addNode({
      type: 'input',
      filename: 'input.mp4',
    });
    const filterId = await nodeMapping.addNode({
      type: 'filter',
      name: 'scale',
      kwargs: { width: 640, height: 480 },
    });
    const outputId = await nodeMapping.addNode({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Connect input -> filter -> output -> global
    nodeMapping.addEdge(inputId, filterId, 0, 0);
    nodeMapping.addEdge(filterId, outputId, 0, 0);
    const globalId = nodeMapping.getGlobalNodeId();
    nodeMapping.addEdge(outputId, globalId, 0, 0);

    const result = await generateFFmpegCommand(nodeMapping.toJson());
    expect(result).toMatchSnapshot();
    expect(result.error).toBeNull();
    expect(result.result).toContain('ffmpeg');
    expect(result.result).toContain('scale=width=640:height=480');
  });

  it('handles multiple input nodes and outputs to global node', async () => {
    const nodeMapping = new NodeMappingManager();

    // Add nodes to mapping
    const input1Id = await nodeMapping.addNode({
      type: 'input',
      filename: 'input1.mp4',
    });
    const input2Id = await nodeMapping.addNode({
      type: 'input',
      filename: 'input2.mp4',
    });
    const outputId = await nodeMapping.addNode({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Connect inputs -> output -> global
    nodeMapping.addEdge(input1Id, outputId, 0, 0);
    nodeMapping.addEdge(input2Id, outputId, 0, 1);
    const globalId = nodeMapping.getGlobalNodeId();
    nodeMapping.addEdge(outputId, globalId, 0, 0);

    const result = await generateFFmpegCommand(nodeMapping.toJson());
    expect(result).toMatchSnapshot();
    expect(result.error).toBeNull();
    expect(result.result).toContain('ffmpeg');
    expect(result.result).toContain('input1.mp4');
    expect(result.result).toContain('input2.mp4');
  });

  it('handles complex filter chains with outputs to global node', async () => {
    const nodeMapping = new NodeMappingManager();

    // Add nodes to mapping
    const inputId = await nodeMapping.addNode({
      type: 'input',
      filename: 'input.mp4',
    });
    const filter1Id = await nodeMapping.addNode({
      type: 'filter',
      name: 'scale',
      kwargs: { width: 640, height: 480 },
    });
    const filter2Id = await nodeMapping.addNode({
      type: 'filter',
      name: 'volume',
      kwargs: { volume: 2.0 },
    });
    const outputId = await nodeMapping.addNode({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Connect input -> filters -> output -> global
    nodeMapping.addEdge(inputId, filter1Id, 0, 0);
    nodeMapping.addEdge(inputId, filter2Id, 1, 0);
    nodeMapping.addEdge(filter1Id, outputId, 0, 0);
    nodeMapping.addEdge(filter2Id, outputId, 0, 1);
    const globalId = nodeMapping.getGlobalNodeId();
    nodeMapping.addEdge(outputId, globalId, 0, 0);

    const result = await generateFFmpegCommand(nodeMapping.toJson());
    expect(result).toMatchSnapshot();
    expect(result.error).toBeNull();
    expect(result.result).toContain('ffmpeg');
    expect(result.result).toContain('scale=width=640:height=480');
    expect(result.result).toContain('volume=volume=2');
  });

  it('handles numeric and boolean parameters correctly with outputs to global node', async () => {
    const nodeMapping = new NodeMappingManager();

    // Add nodes to mapping
    const inputId = await nodeMapping.addNode({
      type: 'input',
      filename: 'input.mp4',
    });
    const filterId = await nodeMapping.addNode({
      type: 'filter',
      name: 'scale',
      kwargs: { width: 640, height: 480, force_original_aspect_ratio: true },
    });
    const outputId = await nodeMapping.addNode({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Connect input -> filter -> output -> global
    nodeMapping.addEdge(inputId, filterId, 0, 0);
    nodeMapping.addEdge(filterId, outputId, 0, 0);
    const globalId = nodeMapping.getGlobalNodeId();
    nodeMapping.addEdge(outputId, globalId, 0, 0);

    const result = await generateFFmpegCommand(nodeMapping.toJson());
    expect(result).toMatchSnapshot();
    expect(result.error).toBeNull();
    expect(result.result).toContain('ffmpeg');
    expect(result.result).toContain('scale=width=640:height=480:force_original_aspect_ratio=1');
  });

  it('handles disconnected nodes with global node', async () => {
    const nodeMappingManager = new NodeMappingManager();

    // Add input node
    nodeMappingManager.addNode({
      type: 'input',
      filename: 'input.mp4',
    });

    // Add output node
    nodeMappingManager.addNode({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Add global node (no connections)
    nodeMappingManager.addNode({
      type: 'global',
      inputs: [],
    });

    // Don't connect the nodes

    const result = await generateFFmpegCommand(nodeMappingManager.toJson());
    expect(result).toMatchSnapshot();
    expect(result.error).toBeDefined();
  });
});

// Keep existing tests for generateFFmpegPythonCode
describe('generateFFmpegPythonCode', () => {
  beforeEach(() => {
    setupPyodideMock();
  });

  it('returns error message if no input or output nodes', async () => {
    const nodeMappingManager = new NodeMappingManager();
    // Add a global node with no inputs
    nodeMappingManager.addNode({ type: 'global', inputs: [] });
    const result = await generateFFmpegPythonCode(nodeMappingManager.toJson());

    // Check that error was logged
    expect(result).toMatchSnapshot();
    expect(result.error).toBeDefined();
  });

  it('generates basic input-output-global chain', async () => {
    const nodeMapping = new NodeMappingManager();

    // Add nodes to mapping
    const inputId = await nodeMapping.addNode({
      type: 'input',
      filename: 'input.mp4',
    });
    const outputId = await nodeMapping.addNode({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Connect input -> output -> global
    nodeMapping.addEdge(inputId, outputId, 0, 0);
    const globalId = nodeMapping.getGlobalNodeId();
    nodeMapping.addEdge(outputId, globalId, 0, 0);

    const result = await generateFFmpegPythonCode(nodeMapping.toJson());
    expect(result).toMatchSnapshot();
    expect(result.error).toBeNull();
  });

  it('generates code with filter nodes, output and global node', async () => {
    const nodeMapping = new NodeMappingManager();

    // Add nodes to mapping
    const inputId = await nodeMapping.addNode({
      type: 'input',
      filename: 'input.mp4',
    });
    const filterId = await nodeMapping.addNode({
      type: 'filter',
      name: 'scale',
      kwargs: { width: 640, height: 480 },
    });
    const outputId = await nodeMapping.addNode({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Connect input -> filter -> output -> global
    nodeMapping.addEdge(inputId, filterId, 0, 0);
    nodeMapping.addEdge(filterId, outputId, 0, 0);
    const globalId = nodeMapping.getGlobalNodeId();
    nodeMapping.addEdge(outputId, globalId, 0, 0);

    const result = await generateFFmpegPythonCode(nodeMapping.toJson());
    expect(result).toMatchSnapshot();
    expect(result.error).toBeNull();
  });

  it('handles multiple input nodes and outputs to global node', async () => {
    const nodeMapping = new NodeMappingManager();

    // Add nodes to mapping
    const input1Id = await nodeMapping.addNode({
      type: 'input',
      filename: 'input1.mp4',
    });
    const input2Id = await nodeMapping.addNode({
      type: 'input',
      filename: 'input2.mp4',
    });
    const outputId = await nodeMapping.addNode({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Connect inputs -> output -> global
    nodeMapping.addEdge(input1Id, outputId, 0, 0);
    nodeMapping.addEdge(input2Id, outputId, 0, 1);
    const globalId = nodeMapping.getGlobalNodeId();
    nodeMapping.addEdge(outputId, globalId, 0, 0);

    const result = await generateFFmpegPythonCode(nodeMapping.toJson());
    expect(result).toMatchSnapshot();
    expect(result.error).toBeNull();
  });

  it('handles complex filter chains with outputs to global node', async () => {
    const nodeMapping = new NodeMappingManager();

    // Add nodes to mapping
    const inputId = await nodeMapping.addNode({
      type: 'input',
      filename: 'input.mp4',
    });
    const filter1Id = await nodeMapping.addNode({
      type: 'filter',
      name: 'scale',
      kwargs: { width: 640, height: 480 },
    });
    const filter2Id = await nodeMapping.addNode({
      type: 'filter',
      name: 'volume',
      kwargs: { volume: 2.0 },
    });
    const outputId = await nodeMapping.addNode({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Connect input -> filters -> output -> global
    nodeMapping.addEdge(inputId, filter1Id, 0, 0);
    nodeMapping.addEdge(inputId, filter2Id, 1, 0);
    nodeMapping.addEdge(filter1Id, outputId, 0, 0);
    nodeMapping.addEdge(filter2Id, outputId, 0, 1);
    const globalId = nodeMapping.getGlobalNodeId();
    nodeMapping.addEdge(outputId, globalId, 0, 0);

    const result = await generateFFmpegPythonCode(nodeMapping.toJson());
    expect(result).toMatchSnapshot();
    expect(result.error).toBeNull();
  });

  it('handles numeric and boolean parameters correctly with outputs to global node', async () => {
    const nodeMapping = new NodeMappingManager();

    // Add nodes to mapping
    const inputId = await nodeMapping.addNode({
      type: 'input',
      filename: 'input.mp4',
    });
    const filterId = await nodeMapping.addNode({
      type: 'filter',
      name: 'scale',
      kwargs: { width: 640, height: 480, force_original_aspect_ratio: true },
    });
    const outputId = await nodeMapping.addNode({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Connect input -> filter -> output -> global
    nodeMapping.addEdge(inputId, filterId, 0, 0);
    nodeMapping.addEdge(filterId, outputId, 0, 0);
    const globalId = nodeMapping.getGlobalNodeId();
    nodeMapping.addEdge(outputId, globalId, 0, 0);

    const result = await generateFFmpegPythonCode(nodeMapping.toJson());
    expect(result).toMatchSnapshot();
    expect(result.error).toBeNull();
  });

  it('handles disconnected nodes with global node', async () => {
    const nodeMappingManager = new NodeMappingManager();

    // Add input node
    nodeMappingManager.addNode({
      type: 'input',
      filename: 'input.mp4',
    });

    // Add output node
    nodeMappingManager.addNode({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    // Add global node (no connections)
    nodeMappingManager.addNode({
      type: 'global',
      inputs: [],
    });

    // Don't connect the nodes

    const result = await generateFFmpegPythonCode(nodeMappingManager.toJson());
    expect(result).toMatchSnapshot();
    expect(result.error).toBeDefined();
  });

  it('handles empty result from Python execution', async () => {
    const nodeMappingManager = new NodeMappingManager();

    // Add a global node with no inputs
    nodeMappingManager.addNode({ type: 'global', inputs: [] });

    const result = await generateFFmpegPythonCode(nodeMappingManager.toJson());
    expect(result).toMatchSnapshot();
    expect(result.error).toBeDefined();
  });
});
