import { Node, Edge } from 'reactflow';
import { loadPyodide, PyodideInterface } from 'pyodide';
import path from 'path';

interface SerializedNode {
  __class__: string;
  node: {
    __class__: string;
    kwargs: Record<string, string>;
    inputs: SerializedNode[];
    name?: string;
    input_typings?: { __class__: string; value: string }[];
    output_typings?: { __class__: string; value: string }[];
    filename?: string;
  };
  index?: number | null;
}

interface Handle {
  id: string;
  type: string;
}

interface NodeData {
  label?: string;
  filterType: string;
  filterName: string;
  parameters?: Record<string, string>;
  handles: {
    inputs: Handle[];
    outputs: Handle[];
  };
  input_typings?: { __class__: string; value: string }[];
  output_typings?: { __class__: string; value: string }[];
  filename?: string;
  __class__?: string;
  name?: string;
  kwargs?: Record<string, string>;
}

interface DeserializedFlow {
  nodes: Node[];
  edges: Edge[];
}

let pyodideInstance: PyodideInterface | null = null;

async function getPyodide() {
  if (!pyodideInstance) {
    // Get the path to the pyodide files in node_modules
    const pyodidePath = path.resolve(process.cwd(), 'node_modules', 'pyodide');

    pyodideInstance = await loadPyodide({
      indexURL: pyodidePath,
    });
    await pyodideInstance.loadPackage('micropip');
    const micropip = pyodideInstance.pyimport('micropip');
    await micropip.install('typed-ffmpeg');
  }
  return pyodideInstance;
}

function convertNullToNone(obj: unknown): unknown {
  if (obj === null) {
    if (!pyodideInstance) {
      throw new Error('Pyodide instance not initialized');
    }
    return pyodideInstance.globals.get('None');
  }
  if (Array.isArray(obj)) {
    return obj.map(convertNullToNone);
  }
  if (typeof obj === 'object') {
    const result: Record<string, unknown> = {};
    for (const [key, value] of Object.entries(obj as Record<string, unknown>)) {
      result[key] = convertNullToNone(value);
    }
    return result;
  }
  return obj;
}

function toPlainObject(obj: unknown): unknown {
  if (obj === null || obj === undefined) {
    return obj;
  }
  if (Array.isArray(obj)) {
    return obj.map(toPlainObject);
  }
  if (typeof obj === 'object') {
    const result: Record<string, unknown> = {};
    for (const [key, value] of Object.entries(obj as Record<string, unknown>)) {
      result[key] = toPlainObject(value);
    }
    return result;
  }
  return obj;
}

async function validateSerializedFlow(serializedFlow: SerializedNode): Promise<boolean> {
  try {
    const pyodide = await getPyodide();

    // Convert the flow to Python-compatible format and convert JsProxy to plain object
    const plainFlow = toPlainObject(serializedFlow);
    const pythonFlow = convertNullToNone(plainFlow);

    // Create Python code to validate the flow
    const pythonCode = `
import json
from ffmpeg.common.serialize import loads

flow = json.loads('${JSON.stringify(pythonFlow)}')
loads(json.dumps(flow))
`;

    // Execute the Python code
    await pyodide.runPythonAsync(pythonCode);
    return true;
  } catch (error) {
    console.error('Validation error:', error);
    throw new Error(`Invalid flow structure: ${error}`);
  }
}

async function validateDeserializedFlow(serializedFlow: SerializedNode): Promise<boolean> {
  try {
    const pyodide = await getPyodide();

    // Convert the flow to Python-compatible format and convert JsProxy to plain object
    const plainFlow = toPlainObject(serializedFlow);
    const pythonFlow = convertNullToNone(plainFlow);

    // Create Python code to validate the flow
    const pythonCode = `
import json
from ffmpeg.common.serialize import loads

flow = json.loads('${JSON.stringify(pythonFlow)}')
loads(json.dumps(flow))
`;

    // Execute the Python code
    await pyodide.runPythonAsync(pythonCode);
    return true;
  } catch (error) {
    console.error('Validation error:', error);
    throw new Error(`Invalid flow structure: ${error}`);
  }
}

export async function serializeFlow(nodes: Node[], edges: Edge[]): Promise<SerializedNode> {
  // Helper function to get input nodes for a given node
  const getInputNodes = (nodeId: string): Node[] => {
    return edges
      .filter((e) => e.target === nodeId)
      .map((e) => nodes.find((n) => n.id === e.source)!)
      .filter(Boolean);
  };

  // Recursive function to build the serialized tree
  const serializeNode = (node: Node): SerializedNode => {
    if (node.data.filterType === 'input') {
      return {
        __class__: 'AVStream',
        node: {
          __class__: 'InputNode',
          kwargs: {},
          inputs: [],
          filename: node.data.filename || 'input.mp4',
        },
      } as SerializedNode;
    }

    const inputNodes = getInputNodes(node.id);

    if (node.data.filterType === 'output') {
      return {
        __class__: 'OutputStream',
        node: {
          __class__: 'OutputNode',
          kwargs: {},
          inputs: inputNodes.map(serializeNode),
          filename: node.data.filename || 'out.mp4',
        },
        index: null,
      };
    }

    // Regular filter node
    const streamType = node.data.handles.outputs[0]?.type || 'video';
    const streamClass = `${streamType.charAt(0).toUpperCase() + streamType.slice(1)}Stream`;
    return {
      __class__: streamClass,
      node: {
        __class__: 'FilterNode',
        kwargs: node.data.parameters || {},
        inputs: inputNodes.map(serializeNode),
        name: node.data.filterName,
        input_typings:
          node.data.input_typings ||
          node.data.handles.inputs.map((h: Handle) => ({
            __class__: 'StreamType',
            value: h.type.toLowerCase(),
          })),
        output_typings:
          node.data.output_typings ||
          node.data.handles.outputs.map((h: Handle) => ({
            __class__: 'StreamType',
            value: h.type.toLowerCase(),
          })),
      },
      index: 0,
    };
  };

  // Find the output node
  const outputNode = nodes.find((n) => n.data.filterType === 'output');
  if (!outputNode) {
    throw new Error('No output node found in the flow');
  }

  // Build the serialized tree starting from the output node
  const serializedFlow = serializeNode(outputNode);

  // Validate the serialized flow
  await validateSerializedFlow(serializedFlow);

  return serializedFlow;
}

export async function deserializeFlow(serializedFlow: SerializedNode): Promise<DeserializedFlow> {
  // Validate the flow structure
  await validateDeserializedFlow(serializedFlow);

  const nodes: Node[] = [];
  const edges: Edge[] = [];
  let nodeIdCounter = 0;

  const generateNodeId = (type: string) => `${type}-${nodeIdCounter++}`;

  const createNode = (
    type: 'input' | 'output' | 'filter',
    position: { x: number; y: number },
    data: NodeData
  ): Node => {
    const getHandles = () => {
      if (type === 'input') {
        return {
          inputs: [],
          outputs: [{ id: 'output-0', type: 'av' }],
        };
      }
      if (type === 'output') {
        return {
          inputs: [{ id: 'input-0', type: 'av' }],
          outputs: [],
        };
      }
      // For filter nodes, use the typings from the data
      return {
        inputs: data.input_typings?.map((t, i) => ({ id: `input-${i}`, type: t.value })) || [],
        outputs: data.output_typings?.map((t, i) => ({ id: `output-${i}`, type: t.value })) || [],
      };
    };

    const streamType =
      type === 'input'
        ? 'av'
        : type === 'output'
          ? 'av'
          : data.output_typings?.[0]?.value || 'video';
    const streamClass =
      type === 'input'
        ? 'AVStream'
        : type === 'output'
          ? 'OutputStream'
          : `${streamType.charAt(0).toUpperCase() + streamType.slice(1)}Stream`;

    return {
      id: generateNodeId(type),
      type: 'filter',
      position,
      data: {
        label: type === 'input' ? 'Input' : type === 'output' ? 'Output' : data.name,
        filterType: type,
        filterName: type === 'filter' ? data.name : type,
        parameters: data.parameters || {},
        handles: getHandles(),
        input_typings: data.input_typings,
        output_typings: data.output_typings,
        filename: data.filename,
        __class__: streamClass,
        name: data.name,
        kwargs: data.kwargs,
      },
    };
  };

  const processNode = (serializedNode: SerializedNode, level: number = 0): string => {
    const isInput = serializedNode.node.__class__ === 'InputNode';
    const isOutput = serializedNode.node.__class__ === 'OutputNode';
    const type = isInput ? 'input' : isOutput ? 'output' : 'filter';

    // Calculate position based on level and number of nodes at this level
    const x = level * 200;
    const y = nodes.filter((n) => n.position.x === x).length * 100;

    const nodeData: NodeData = {
      filterType: type,
      filterName: type === 'filter' ? serializedNode.node.name || '' : type,
      parameters: serializedNode.node.kwargs || {},
      handles: {
        inputs:
          serializedNode.node.input_typings?.map((t, i) => ({ id: `input-${i}`, type: t.value })) ||
          [],
        outputs:
          serializedNode.node.output_typings?.map((t, i) => ({
            id: `output-${i}`,
            type: t.value,
          })) || [],
      },
      input_typings: serializedNode.node.input_typings,
      output_typings: serializedNode.node.output_typings,
      filename: serializedNode.node.filename,
      __class__: serializedNode.__class__,
      name: serializedNode.node.name,
      kwargs: serializedNode.node.kwargs,
    };

    const node = createNode(type, { x, y }, nodeData);
    nodes.push(node);

    // Process input nodes recursively
    serializedNode.node.inputs.forEach((input, index) => {
      const inputId = processNode(input, level + 1);
      edges.push({
        id: `${inputId}-${node.id}`,
        source: inputId,
        target: node.id,
        sourceHandle: 'output-0',
        targetHandle: `input-${index}`,
      });
    });

    return node.id;
  };

  // Start processing from the root (output) node
  processNode(serializedFlow);

  return { nodes, edges };
}
