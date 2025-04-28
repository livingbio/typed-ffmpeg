import { validateConnection } from '../connectionValidation';
import { Node, Edge } from 'reactflow';
import { predefinedFilters } from '../../types/ffmpeg';

describe('connectionValidation', () => {
  const createNode = (
    id: string,
    filterType: 'input' | 'filter' | 'output',
    filterName?: string,
    parameters: Record<string, string> = {},
    handles: { inputs: { id: string; type: string }[]; outputs: { id: string; type: string }[] } = {
      inputs: [],
      outputs: [],
    }
  ): Node => ({
    id,
    type: 'filter',
    position: { x: 0, y: 0 },
    data: {
      label: filterType,
      filterType,
      filterName,
      parameters,
      handles,
    },
  });

  const createConnection = (
    source: string,
    target: string,
    sourceHandle: string,
    targetHandle: string
  ) => ({
    source,
    target,
    sourceHandle,
    targetHandle,
  });

  it('should allow connections from input nodes', () => {
    const inputNode = createNode('input', 'input');
    const filterNode = createNode(
      'filter',
      'filter',
      'filter',
      {},
      {
        inputs: [{ id: 'input-0', type: 'video' }],
        outputs: [{ id: 'output-0', type: 'video' }],
      }
    );

    const connection = createConnection('input', 'filter', 'output-0', 'input-0');
    expect(validateConnection(connection, [inputNode, filterNode], [])).toBe(true);
  });

  it('should allow connections to output nodes', () => {
    const filterNode = createNode(
      'filter',
      'filter',
      'filter',
      {},
      {
        inputs: [{ id: 'input-0', type: 'video' }],
        outputs: [{ id: 'output-0', type: 'video' }],
      }
    );
    const outputNode = createNode('output', 'output');

    const connection = createConnection('filter', 'output', 'output-0', 'input-0');
    expect(validateConnection(connection, [filterNode, outputNode], [])).toBe(true);
  });

  it('should validate dynamic input streams', () => {
    const sourceNode = createNode(
      'source',
      'filter',
      'source',
      {},
      {
        inputs: [{ id: 'input-0', type: 'video' }],
        outputs: [{ id: 'output-0', type: 'video' }],
      }
    );

    // Create a filter with dynamic inputs based on a parameter
    const dynamicFilter = predefinedFilters.find((f) => f.is_dynamic_input);
    if (!dynamicFilter) {
      throw new Error('No dynamic input filter found in predefined filters');
    }

    const targetNode = createNode(
      'target',
      'filter',
      dynamicFilter.name,
      { inputs: '2' },
      {
        inputs: [
          { id: 'input-0', type: 'video' },
          { id: 'input-1', type: 'video' },
        ],
        outputs: [{ id: 'output-0', type: 'video' }],
      }
    );

    const connection = createConnection('source', 'target', 'output-0', 'input-0');
    expect(validateConnection(connection, [sourceNode, targetNode], [])).toBe(true);
  });

  it('should validate dynamic output streams', () => {
    // Create a filter with dynamic outputs based on a parameter
    const dynamicFilter = predefinedFilters.find((f) => f.is_dynamic_output);
    if (!dynamicFilter) {
      throw new Error('No dynamic output filter found in predefined filters');
    }

    const sourceNode = createNode(
      'source',
      'filter',
      dynamicFilter.name,
      { outputs: '2' },
      {
        inputs: [{ id: 'input-0', type: 'video' }],
        outputs: [
          { id: 'output-0', type: 'video' },
          { id: 'output-1', type: 'video' },
        ],
      }
    );

    const targetNode = createNode(
      'target',
      'filter',
      'target',
      {},
      {
        inputs: [{ id: 'input-0', type: 'video' }],
        outputs: [{ id: 'output-0', type: 'video' }],
      }
    );

    const connection = createConnection('source', 'target', 'output-0', 'input-0');
    expect(validateConnection(connection, [sourceNode, targetNode], [])).toBe(true);
  });

  it('should prevent invalid type connections', () => {
    const sourceNode = createNode(
      'source',
      'filter',
      'source',
      {},
      {
        inputs: [{ id: 'input-0', type: 'video' }],
        outputs: [{ id: 'output-0', type: 'audio' }],
      }
    );

    const targetNode = createNode(
      'target',
      'filter',
      'target',
      {},
      {
        inputs: [{ id: 'input-0', type: 'video' }],
        outputs: [{ id: 'output-0', type: 'video' }],
      }
    );

    const connection = createConnection('source', 'target', 'output-0', 'input-0');
    expect(validateConnection(connection, [sourceNode, targetNode], [])).toBe(false);
  });

  it('should prevent multiple connections to the same input', () => {
    const sourceNode1 = createNode(
      'source1',
      'filter',
      'source',
      {},
      {
        inputs: [{ id: 'input-0', type: 'video' }],
        outputs: [{ id: 'output-0', type: 'video' }],
      }
    );

    const sourceNode2 = createNode(
      'source2',
      'filter',
      'source',
      {},
      {
        inputs: [{ id: 'input-0', type: 'video' }],
        outputs: [{ id: 'output-0', type: 'video' }],
      }
    );

    const targetNode = createNode(
      'target',
      'filter',
      'target',
      {},
      {
        inputs: [{ id: 'input-0', type: 'video' }],
        outputs: [{ id: 'output-0', type: 'video' }],
      }
    );

    const existingEdge: Edge = {
      id: 'edge1',
      source: 'source1',
      target: 'target',
      sourceHandle: 'output-0',
      targetHandle: 'input-0',
    };

    const connection = createConnection('source2', 'target', 'output-0', 'input-0');
    expect(
      validateConnection(connection, [sourceNode1, sourceNode2, targetNode], [existingEdge])
    ).toBe(false);
  });
});
