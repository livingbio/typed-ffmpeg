import { describe, it, expect, beforeEach } from 'vitest';
import { Node, Edge } from 'reactflow';
import { convertToDag } from '../convertToDag';
import { setupPyodideMock } from './testUtils';
import { runPython } from '../pyodide';
import { dumps } from '../serialize';

const VERIFY_DAG_PYTHON_CODE = (jsonStr: string) => `
from ffmpeg.common.serialize import loads, dumps
import json
import base64

encoded = '''${Buffer.from(jsonStr).toString('base64')}'''
decoded = base64.b64decode(encoded).decode('utf-8')
dag = loads(decoded)
result = dumps(dag)
result
`;

describe('convertToDag', () => {
  beforeEach(async () => {
    setupPyodideMock();
  });

  it('should convert simple input-output chain', async () => {
    const nodes: Node[] = [
      {
        id: 'input1',
        type: 'default',
        position: { x: 0, y: 0 },
        data: { filterType: 'input' },
      },
      {
        id: 'output1',
        type: 'default',
        position: { x: 200, y: 0 },
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

    const dag = convertToDag(nodes, edges);
    expect(dag).not.toBeNull();

    const jsonStr = dumps(dag);
    console.log('JSON string:', jsonStr);
    const result = await runPython(VERIFY_DAG_PYTHON_CODE(jsonStr));
    console.log('Python result:', result);
    const parsedResult = JSON.parse(result);
    expect(parsedResult).toMatchSnapshot();
  });

  it('should convert filter chain with multiple nodes', async () => {
    const nodes: Node[] = [
      {
        id: 'input1',
        type: 'default',
        position: { x: 0, y: 0 },
        data: { filterType: 'input' },
      },
      {
        id: 'filter1',
        type: 'default',
        position: { x: 200, y: 0 },
        data: {
          filterType: 'filter',
          filterName: 'scale',
          parameters: { w: 640, h: 480 },
        },
      },
      {
        id: 'output1',
        type: 'default',
        position: { x: 400, y: 0 },
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

    const dag = convertToDag(nodes, edges);
    expect(dag).not.toBeNull();

    const jsonStr = dumps(dag);
    console.log('JSON string:', jsonStr);
    const result = await runPython(VERIFY_DAG_PYTHON_CODE(jsonStr));
    console.log('Python result:', result);
    const parsedResult = JSON.parse(result);
    expect(parsedResult).toMatchSnapshot();
  });

  it('should handle multiple input and output nodes', async () => {
    const nodes: Node[] = [
      {
        id: 'input1',
        type: 'default',
        position: { x: 0, y: 0 },
        data: { filterType: 'input' },
      },
      {
        id: 'input2',
        type: 'default',
        position: { x: 0, y: 100 },
        data: { filterType: 'input' },
      },
      {
        id: 'output1',
        type: 'default',
        position: { x: 200, y: 0 },
        data: { filterType: 'output' },
      },
      {
        id: 'output2',
        type: 'default',
        position: { x: 200, y: 100 },
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

    const dag = convertToDag(nodes, edges);
    expect(dag).not.toBeNull();

    const jsonStr = dumps(dag);
    console.log('JSON string:', jsonStr);
    const result = await runPython(VERIFY_DAG_PYTHON_CODE(jsonStr));
    console.log('Python result:', result);
    const parsedResult = JSON.parse(result);
    expect(parsedResult).toMatchSnapshot();
  });

  it('should handle audio and video streams', async () => {
    const nodes: Node[] = [
      {
        id: 'input1',
        type: 'default',
        position: { x: 0, y: 0 },
        data: { filterType: 'input' },
      },
      {
        id: 'output1',
        type: 'default',
        position: { x: 200, y: 0 },
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
        source: 'input1',
        target: 'output1',
        data: { type: 'audio' },
      },
    ];

    const dag = convertToDag(nodes, edges);
    expect(dag).not.toBeNull();

    const jsonStr = dumps(dag);
    console.log('JSON string:', jsonStr);
    const result = await runPython(VERIFY_DAG_PYTHON_CODE(jsonStr));
    console.log('Python result:', result);
    const parsedResult = JSON.parse(result);
    expect(parsedResult).toMatchSnapshot();
  });

  it('should return null for empty graph', () => {
    const nodes: Node[] = [];
    const edges: Edge[] = [];
    const dag = convertToDag(nodes, edges);
    expect(dag).toBeNull();
  });
});
