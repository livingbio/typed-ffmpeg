import { describe, it, expect } from 'vitest';
import { convertFromDag } from '../convertFromDag';
import {
  GlobalNode,
  InputNode,
  OutputNode,
  FilterNode,
  VideoStream,
  AudioStream,
  OutputStream,
  StreamType,
} from '../../types/dag';

describe('convertFromDag', () => {
  it('should convert a simple input-output DAG to React Flow nodes and edges', () => {
    // Create a simple DAG: Input -> Output
    const inputNode = new InputNode('input.mp4');
    const outputNode = new OutputNode('output.mp4', [new VideoStream(inputNode)]);
    const dag = new GlobalNode([new OutputStream(outputNode)]);

    const result = convertFromDag(dag);
    expect(result).toMatchSnapshot();
  });

  it('should convert a DAG with filter nodes to React Flow nodes and edges', () => {
    // Create a DAG: Input -> Filter -> Output
    const inputNode = new InputNode('input.mp4');
    const filterNode = new FilterNode(
      'reverse',
      [new VideoStream(inputNode)],
      [new StreamType('video')],
      [new StreamType('video')]
    );
    const outputNode = new OutputNode('output.mp4', [new VideoStream(filterNode)]);
    const dag = new GlobalNode([new OutputStream(outputNode)]);

    const result = convertFromDag(dag);
    expect(result).toMatchSnapshot();
  });

  it('should handle multiple output nodes', () => {
    // Create a DAG with multiple outputs: Input -> Filter -> Output1, Output2
    const inputNode = new InputNode('input.mp4');
    const filterNode = new FilterNode(
      'split',
      [new VideoStream(inputNode)],
      [new StreamType('video')],
      [new StreamType('video'), new StreamType('video')]
    );
    const outputNode1 = new OutputNode('output1.mp4', [new VideoStream(filterNode, 0)]);
    const outputNode2 = new OutputNode('output2.mp4', [new VideoStream(filterNode, 1)]);
    const dag = new GlobalNode([
      new OutputStream(outputNode1),
      new OutputStream(outputNode2),
    ]);

    const result = convertFromDag(dag);
    expect(result).toMatchSnapshot();
  });

  it('should handle audio and video streams correctly', () => {
    // Create a DAG with both audio and video streams
    const inputNode = new InputNode('input.mp4');
    const videoFilter = new FilterNode(
      'reverse',
      [new VideoStream(inputNode)],
      [new StreamType('video')],
      [new StreamType('video')]
    );
    const audioFilter = new FilterNode(
      'areverse',
      [new AudioStream(inputNode)],
      [new StreamType('audio')],
      [new StreamType('audio')]
    );
    const outputNode = new OutputNode('output.mp4', [
      new VideoStream(videoFilter),
      new AudioStream(audioFilter),
    ]);
    const dag = new GlobalNode([new OutputStream(outputNode)]);

    const result = convertFromDag(dag);
    expect(result).toMatchSnapshot();
  });

  it('should preserve filter parameters', () => {
    // Create a DAG with a filter that has parameters
    const inputNode = new InputNode('input.mp4');
    const filterNode = new FilterNode(
      'scale',
      [new VideoStream(inputNode)],
      [new StreamType('video')],
      [new StreamType('video')],
      { width: 1920, height: 1080 }
    );
    const outputNode = new OutputNode('output.mp4', [new VideoStream(filterNode)]);
    const dag = new GlobalNode([new OutputStream(outputNode)]);

    const result = convertFromDag(dag);
    expect(result).toMatchSnapshot();
  });
}); 