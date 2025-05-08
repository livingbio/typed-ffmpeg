import { generateFFmpegCommand } from '../../utils/generateFFmpegCommand';
import { Node, Edge } from 'reactflow';
import { describe, it, expect, beforeEach } from 'vitest';
import { setupPyodideMock } from '../../utils/__tests__/testUtils';

interface FilterData {
  filterType: 'input' | 'output' | 'filter';
  filterName?: string;
  parameters?: Record<string, string>;
}

interface FilterNode extends Node {
  type: 'filter';
  data: FilterData;
}

describe('generateFFmpegCommand', () => {
  beforeEach(() => {
    setupPyodideMock();
  });

  it('returns empty python string if no input or output nodes', async () => {
    const nodes: FilterNode[] = [];
    const edges: Edge[] = [];
    const result = await generateFFmpegCommand(nodes, edges);
    expect(result).toMatchSnapshot();
  });

  it('generates basic input-output chain', async () => {
    const nodes: FilterNode[] = [
      {
        id: 'input1',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: { filterType: 'input' },
      },
      {
        id: 'output1',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: { filterType: 'output' },
      },
    ];
    const edges: Edge[] = [
      {
        id: 'edge1',
        source: 'input1',
        target: 'output1',
        data: { type: 'video' },
      },
    ];

    const result = await generateFFmpegCommand(nodes, edges);
    expect(result).toMatchSnapshot();
  });

  it('generates code with filter nodes', async () => {
    const nodes: FilterNode[] = [
      {
        id: 'input1',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: { filterType: 'input' },
      },
      {
        id: 'filter1',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: {
          filterType: 'filter',
          filterName: 'scale',
          parameters: { width: '1280', height: '720' },
        },
      },
      {
        id: 'output1',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: { filterType: 'output' },
      },
    ];
    const edges: Edge[] = [
      {
        id: 'edge1',
        source: 'input1',
        target: 'filter1',
        data: { type: 'video' },
      },
      {
        id: 'edge2',
        source: 'filter1',
        target: 'output1',
        data: { type: 'video' },
      },
    ];

    const result = await generateFFmpegCommand(nodes, edges);
    expect(result).toMatchSnapshot();
  });

  it('handles multiple input and output nodes', async () => {
    const nodes: FilterNode[] = [
      {
        id: 'input1',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: { filterType: 'input' },
      },
      {
        id: 'input2',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: { filterType: 'input' },
      },
      {
        id: 'output1',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: { filterType: 'output' },
      },
      {
        id: 'output2',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: { filterType: 'output' },
      },
    ];
    const edges: Edge[] = [
      {
        id: 'edge1',
        source: 'input1',
        target: 'output1',
        data: { type: 'video' },
      },
      {
        id: 'edge2',
        source: 'input2',
        target: 'output2',
        data: { type: 'video' },
      },
    ];

    const result = await generateFFmpegCommand(nodes, edges);
    expect(result).toMatchSnapshot();
  });

  it('handles complex filter chains', async () => {
    const nodes: FilterNode[] = [
      {
        id: 'input1',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: { filterType: 'input' },
      },
      {
        id: 'filter1',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: {
          filterType: 'filter',
          filterName: 'scale',
          parameters: { width: '1280', height: '720' },
        },
      },
      {
        id: 'filter2',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: {
          filterType: 'filter',
          filterName: 'crop',
          parameters: { x: '0', y: '0', width: '640', height: '480' },
        },
      },
      {
        id: 'output1',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: { filterType: 'output' },
      },
    ];
    const edges: Edge[] = [
      {
        id: 'edge1',
        source: 'input1',
        target: 'filter1',
        data: { type: 'video' },
      },
      {
        id: 'edge2',
        source: 'filter1',
        target: 'filter2',
        data: { type: 'video' },
      },
      {
        id: 'edge3',
        source: 'filter2',
        target: 'output1',
        data: { type: 'video' },
      },
    ];

    const result = await generateFFmpegCommand(nodes, edges);
    expect(result).toMatchSnapshot();
  });

  it('handles numeric and boolean parameters correctly', async () => {
    const nodes: FilterNode[] = [
      {
        id: 'input1',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: { filterType: 'input' },
      },
      {
        id: 'filter1',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: {
          filterType: 'filter',
          filterName: 'filter',
          parameters: {
            number: '42',
            boolean: 'true',
            string: 'test',
          },
        },
      },
      {
        id: 'output1',
        type: 'filter',
        position: { x: 0, y: 0 },
        data: { filterType: 'output' },
      },
    ];
    const edges: Edge[] = [
      {
        id: 'edge1',
        source: 'input1',
        target: 'filter1',
        data: { type: 'video' },
      },
      {
        id: 'edge2',
        source: 'filter1',
        target: 'output1',
        data: { type: 'video' },
      },
    ];

    const result = await generateFFmpegCommand(nodes, edges);
    expect(result).toMatchSnapshot();
  });
});
