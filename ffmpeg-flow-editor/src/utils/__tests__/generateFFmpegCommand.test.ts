import { generateFFmpegCommand } from '../generateFFmpegCommand';
import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest';
import { NodeMappingManager } from '../nodeMapping';
import { setupPyodideMock } from './testUtils';

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
    nodeMappingManager.addNode({ type: 'global', inputs: [] });
    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that error was logged
    expect(result).toMatchSnapshot();
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

    const result = await generateFFmpegCommand(nodeMapping);

    expect(result).toMatchSnapshot();
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

    const result = await generateFFmpegCommand(nodeMapping);

    expect(result).toMatchSnapshot();
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

    const result = await generateFFmpegCommand(nodeMapping);

    expect(result).toMatchSnapshot();
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

    const result = await generateFFmpegCommand(nodeMapping);

    expect(result).toMatchSnapshot();
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

    const result = await generateFFmpegCommand(nodeMapping);

    expect(result).toMatchSnapshot();
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

    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that error was logged
    expect(result).toMatchSnapshot();
  });

  it('handles empty result from Python execution', async () => {
    // Mock empty response from runPython
    const consoleWarnSpy = vi.spyOn(console, 'warn').mockImplementation(() => {});

    const nodeMappingManager = new NodeMappingManager();

    // Add a global node with no inputs
    nodeMappingManager.addNode({ type: 'global', inputs: [] });

    const result = await generateFFmpegCommand(nodeMappingManager);

    // Check that a warning was logged
    expect(result).toMatchSnapshot();

    consoleWarnSpy.mockRestore();
  });
});
