import { describe, it, expect } from 'vitest';
import { convertFromDag } from '../convertFromDag';
import { convertToDag } from '../convertToDag';
import { loads } from '../serialize';
import { readdirSync, readFileSync } from 'fs';
import { join } from 'path';
import { 
  GlobalNode, 
  StreamType, 
  VideoStream, 
  AudioStream,
  InputNode,
  OutputNode,
  FilterNode
} from '../../types/dag';
import { Node, Edge } from 'reactflow';
import { EdgeData } from '../../types/edge';

// Helper function to compare DAGs
function compareDags(initial: GlobalNode, final: GlobalNode | null) {
  // Ensure final DAG is not null
  expect(final).not.toBeNull();
  if (!final) return; // TypeScript guard

  // Compare number of output streams
  expect(final.inputs.length).toBe(initial.inputs.length);

  // Helper to compare stream types
  const compareStreamTypes = (initial: StreamType[], final: StreamType[]) => {
    expect(final.length).toBe(initial.length);
    initial.forEach((type, i) => {
      expect(final[i].value).toBe(type.value);
    });
  };

  // Helper to compare filter parameters
  const compareParameters = (initial: Record<string, unknown>, final: Record<string, unknown>) => {
    expect(Object.keys(final)).toEqual(Object.keys(initial));
    Object.entries(initial).forEach(([key, value]) => {
      expect(final[key]).toBe(value);
    });
  };

  // Helper to compare streams
  const compareStreams = (initial: VideoStream | AudioStream, final: VideoStream | AudioStream) => {
    expect(final.constructor).toBe(initial.constructor);
    expect(final.index).toBe(initial.index);
    expect(final.node.constructor).toBe(initial.node.constructor);
  };

  // Compare each output stream
  initial.inputs.forEach((initialStream, index) => {
    const finalStream = final.inputs[index];
    expect(finalStream).toBeInstanceOf(initialStream.constructor);

    const initialNode = initialStream.node;
    const finalNode = finalStream.node;

    // Compare node types
    expect(finalNode.constructor).toBe(initialNode.constructor);

    if (initialNode instanceof InputNode && finalNode instanceof InputNode) {
      expect(finalNode.filename).toBe(initialNode.filename);
    } else if (initialNode instanceof OutputNode && finalNode instanceof OutputNode) {
      expect(finalNode.filename).toBe(initialNode.filename);
      expect(finalNode.inputs.length).toBe(initialNode.inputs.length);
      
      // Compare each input stream of the output node
      initialNode.inputs.forEach((initialInput, inputIndex) => {
        const finalInput = finalNode.inputs[inputIndex];
        compareStreams(initialInput, finalInput);
      });
    } else if (initialNode instanceof FilterNode && finalNode instanceof FilterNode) {
      expect(finalNode.name).toBe(initialNode.name);
      compareStreamTypes(initialNode.input_typings, finalNode.input_typings);
      compareStreamTypes(initialNode.output_typings, finalNode.output_typings);
      compareParameters(initialNode.kwargs, finalNode.kwargs);
      expect(finalNode.inputs.length).toBe(initialNode.inputs.length);
      
      // Compare each input stream of the filter node
      initialNode.inputs.forEach((initialInput, inputIndex) => {
        const finalInput = finalNode.inputs[inputIndex];
        compareStreams(initialInput, finalInput);
      });
    }
  });
}

// Helper function to validate React Flow representation
function validateReactFlowRepresentation(nodes: Node[], edges: Edge<EdgeData>[]) {
  // Validate node positions
  nodes.forEach(node => {
    expect(node.position).toBeDefined();
    expect(typeof node.position.x).toBe('number');
    expect(typeof node.position.y).toBe('number');
  });

  // Validate edge types and styles
  edges.forEach(edge => {
    expect(edge.type).toBe('smoothstep');
    expect(edge.style).toBeDefined();
    expect(edge.data).toBeDefined();
    if (!edge.data) return;
    
    expect(edge.data.type).toBeDefined();
    
    // Validate edge colors based on type
    const expectedColor = edge.data.type === 'video' ? '#f44336' : 
                         edge.data.type === 'audio' ? '#2196f3' : '#9c27b0';
    expect(edge.style?.stroke).toBe(expectedColor);
  });

  // Validate node handles
  nodes.forEach(node => {
    expect(node.data.handles).toBeDefined();
    expect(node.data.handles.inputs).toBeDefined();
    expect(node.data.handles.outputs).toBeDefined();
  });
}

// Get all JSON files from the test data directory
const testDataDir = join(__dirname, '__testdata__');
const testFiles = readdirSync(testDataDir)
  .filter((file) => file.endsWith('.json'))
  .map((file) => ({
    name: file.replace('.json', ''),
    data: JSON.parse(readFileSync(join(testDataDir, file), 'utf-8')),
  }));

describe('DAG Conversion Round Trip', () => {
  it.each(testFiles)('should maintain consistency in $name case', ({ data }) => {
    // Load the initial DAG from the test data
    const initialDag = loads(JSON.stringify(data)) as GlobalNode;

    // Convert to React Flow and back
    const { nodes, edges } = convertFromDag(initialDag);
    validateReactFlowRepresentation(nodes, edges);
    const finalDag = convertToDag(nodes, edges);

    // Compare the DAGs
    compareDags(initialDag, finalDag);
  });
}); 