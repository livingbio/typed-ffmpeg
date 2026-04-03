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
    const result = await generateFFmpegCommand(nodeMappingManager);

    expect(result.error).toBeDefined();
  });

  it('generates basic input-output-global chain command', async () => {
    const nodeMapping = new NodeMappingManager();

    const inputId = await nodeMapping.addNode({
      type: 'input',
      filename: 'input.mp4',
    });
    const outputId = await nodeMapping.addNode({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    nodeMapping.addEdge(inputId, outputId, 0, 0);
    const globalId = nodeMapping.getGlobalNodeId();
    nodeMapping.addEdge(outputId, globalId, 0, 0);

    const result = await generateFFmpegCommand(nodeMapping);
    expect(result.error).toBeNull();
    expect(result.result).toContain('ffmpeg');
    expect(result.result).toContain('input.mp4');
    expect(result.result).toContain('output.mp4');
  });

  it('generates command with filter nodes, output and global node', async () => {
    const nodeMapping = new NodeMappingManager();

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

    nodeMapping.addEdge(inputId, filterId, 0, 0);
    nodeMapping.addEdge(filterId, outputId, 0, 0);
    const globalId = nodeMapping.getGlobalNodeId();
    nodeMapping.addEdge(outputId, globalId, 0, 0);

    const result = await generateFFmpegCommand(nodeMapping);
    expect(result.error).toBeNull();
    expect(result.result).toContain('ffmpeg');
    expect(result.result).toContain('scale');
    expect(result.result).toContain('640');
  });

  it('handles multiple input nodes and outputs to global node', async () => {
    const nodeMapping = new NodeMappingManager();

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

    nodeMapping.addEdge(input1Id, outputId, 0, 0);
    nodeMapping.addEdge(input2Id, outputId, 0, 1);
    const globalId = nodeMapping.getGlobalNodeId();
    nodeMapping.addEdge(outputId, globalId, 0, 0);

    const result = await generateFFmpegCommand(nodeMapping);
    expect(result.error).toBeNull();
    expect(result.result).toContain('ffmpeg');
    expect(result.result).toContain('input1.mp4');
    expect(result.result).toContain('input2.mp4');
  });

  it('handles disconnected nodes with global node', async () => {
    const nodeMappingManager = new NodeMappingManager();

    nodeMappingManager.addNode({
      type: 'input',
      filename: 'input.mp4',
    });
    nodeMappingManager.addNode({
      type: 'output',
      filename: 'output.mp4',
      inputs: [],
    });

    const result = await generateFFmpegCommand(nodeMappingManager);
    expect(result.error).toBeDefined();
  });
});

describe('generateFFmpegPythonCode', () => {
  it('returns a placeholder message (Python generation not supported)', async () => {
    const manager = new NodeMappingManager();
    const result = await generateFFmpegPythonCode(manager);
    expect(result.error).toBeNull();
    expect(result.result).toContain('not available');
  });
});
