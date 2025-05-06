import { Node, Edge } from 'reactflow';
import { serializeFlow, deserializeFlow } from '../flowSerialization';
import { loadPyodide } from 'pyodide';
import path from 'path';
import '@testing-library/jest-dom';

// Create a singleton instance of Pyodide
let pyodide: Awaited<ReturnType<typeof loadPyodide>> | null = null;

async function getPyodide() {
  if (!pyodide) {
    // Get the path to the pyodide files in node_modules
    const pyodidePath = path.resolve(process.cwd(), 'node_modules', 'pyodide');

    pyodide = await loadPyodide({
      indexURL: pyodidePath,
    });
    await pyodide.loadPackage('micropip');
    await pyodide.runPythonAsync(`
      import micropip
      await micropip.install('typed-ffmpeg')
    `);
  }
  return pyodide;
}

describe('Flow Serialization and Deserialization', () => {
  beforeEach(async () => {
    // Reset the Pyodide instance
    pyodide = null;

    // Setup window mock with the actual Pyodide
    global.window = {
      loadPyodide: getPyodide,
    } as unknown as Window & typeof globalThis;
  });

  const mockNodes: Node[] = [
    {
      id: 'input-0',
      type: 'filter',
      position: { x: 0, y: 0 },
      data: {
        filterType: 'input',
        filterName: 'input',
        filename: 'input.mp4',
        handles: {
          inputs: [],
          outputs: [{ id: 'output-0', type: 'av' }],
        },
      },
    },
    {
      id: 'output-0',
      type: 'filter',
      position: { x: 200, y: 0 },
      data: {
        filterType: 'output',
        filterName: 'output',
        filename: 'output.mp4',
        handles: {
          inputs: [{ id: 'input-0', type: 'av' }],
          outputs: [],
        },
      },
    },
  ];

  const mockEdges: Edge[] = [
    {
      id: 'input-0-output-0',
      source: 'input-0',
      target: 'output-0',
      sourceHandle: 'output-0',
      targetHandle: 'input-0',
    },
  ];

  describe('serializeFlow', () => {
    it('should serialize a simple input-output flow', async () => {
      const result = await serializeFlow(mockNodes, mockEdges);
      expect(result).toMatchSnapshot();
    });

    it('should handle missing filenames', async () => {
      const nodesWithoutFilenames = mockNodes.map((node) => ({
        ...node,
        data: { ...node.data, filename: undefined },
      }));
      const result = await serializeFlow(nodesWithoutFilenames, mockEdges);
      expect(result).toMatchSnapshot();
    });

    it('should throw error when no output node is found', async () => {
      const nodesWithoutOutput = mockNodes.filter((n) => n.data.filterType !== 'output');
      await expect(serializeFlow(nodesWithoutOutput, mockEdges)).rejects.toThrow(
        'No output node found in the flow'
      );
    });
  });

  describe('deserializeFlow', () => {
    it('should deserialize a simple input-output flow', async () => {
      const serializedFlow = await serializeFlow(mockNodes, mockEdges);
      const result = await deserializeFlow(serializedFlow);
      expect(result).toMatchSnapshot();
    });

    it('should preserve node positions and connections', async () => {
      const serializedFlow = await serializeFlow(mockNodes, mockEdges);
      const result = await deserializeFlow(serializedFlow);

      // Check if we have the same number of nodes and edges
      expect(result.nodes.length).toBe(mockNodes.length);
      expect(result.edges.length).toBe(mockEdges.length);

      // Check if nodes have correct types
      const inputNode = result.nodes.find((n) => n.data.filterType === 'input');
      const outputNode = result.nodes.find((n) => n.data.filterType === 'output');
      expect(inputNode).toBeTruthy();
      expect(outputNode).toBeTruthy();

      // Check if edge connects input to output
      const edge = result.edges[0];
      expect(edge.source).toBe(inputNode?.id);
      expect(edge.target).toBe(outputNode?.id);
    });

    it('should handle complex filter nodes', async () => {
      const complexNodes: Node[] = [
        ...mockNodes,
        {
          id: 'filter-0',
          type: 'filter',
          position: { x: 100, y: 0 },
          data: {
            filterType: 'filter',
            filterName: 'scale',
            parameters: { width: '1280', height: '720' },
            handles: {
              inputs: [{ id: 'input-0', type: 'video' }],
              outputs: [{ id: 'output-0', type: 'video' }],
            },
            input_typings: [{ __class__: 'StreamType', value: 'video' }],
            output_typings: [{ __class__: 'StreamType', value: 'video' }],
          },
        },
      ];

      const complexEdges: Edge[] = [
        {
          id: 'input-0-filter-0',
          source: 'input-0',
          target: 'filter-0',
          sourceHandle: 'output-0',
          targetHandle: 'input-0',
        },
        {
          id: 'filter-0-output-0',
          source: 'filter-0',
          target: 'output-0',
          sourceHandle: 'output-0',
          targetHandle: 'input-0',
        },
      ];

      const serializedFlow = await serializeFlow(complexNodes, complexEdges);
      const result = await deserializeFlow(serializedFlow);
      expect(result).toMatchSnapshot();
    });
  });

  describe('Round-trip serialization', () => {
    it('should preserve node and edge structure after round-trip', async () => {
      const serializedFlow = await serializeFlow(mockNodes, mockEdges);
      const { nodes, edges } = await deserializeFlow(serializedFlow);
      const reserializedFlow = await serializeFlow(nodes, edges);
      expect(reserializedFlow).toMatchSnapshot();
    });
  });
});
