import { describe, it, expect, beforeAll } from 'vitest';
import { loads, clearClassRegistry } from '../../utils/serialize';
import { Serializable } from '../../utils/serialize';
import { readdirSync, readFileSync } from 'fs';
import { join } from 'path';

// Import all DAG classes to register them
import {
  StreamType,
  FilterNode,
  InputNode,
  OutputNode,
  GlobalNode,
  FilterableStream,
  VideoStream,
  AudioStream,
  AVStream,
  OutputStream,
  GlobalStream,
} from '../dag';
import { FFmpegFilter, FFmpegIOType } from '../ffmpeg';

// Clear and re-register all classes before tests
beforeAll(() => {
  clearClassRegistry();
  // Create instances to trigger registration
  new StreamType('audio');
  new StreamType('video');
  const testFilter: FFmpegFilter = {
    __class__: 'FFMpegFilter',
    id: 'test',
    name: 'test',
    description: 'test',
    ref: 'test',
    is_support_slice_threading: false,
    is_support_timeline: false,
    is_support_framesync: false,
    is_support_command: false,
    is_filter_sink: false,
    is_filter_source: false,
    is_dynamic_input: false,
    is_dynamic_output: false,
    stream_typings_input: [],
    stream_typings_output: [],
    formula_typings_input: null,
    formula_typings_output: null,
    pre: [],
    options: [],
  };
  const inputNode = new InputNode('test');
  const outputNode = new OutputNode('test', []);
  new FilterNode('test', [], [StreamType.audio], [StreamType.audio], testFilter);
  new InputNode('test');
  new OutputNode('test', []);
  new GlobalNode([]);
  new FilterableStream(inputNode, 0);
  new VideoStream(inputNode, 0);
  new AudioStream(inputNode, 0);
  new AVStream(inputNode, 0);
  new OutputStream(outputNode, 0);
  new GlobalStream(new GlobalNode([]), 0);
});

// Get all JSON files from the test data directory
const testDataDir = join(__dirname, '__testdata__');
const testFiles = readdirSync(testDataDir)
  .filter((file) => file.endsWith('.json'))
  .map((file) => ({
    name: file.replace('.json', ''),
    data: JSON.parse(readFileSync(join(testDataDir, file), 'utf-8')),
  }));

describe('DAG Serialization', () => {
  it.each(testFiles)('should handle $name case', ({ data }) => {
    // Convert to string for deserialization
    const jsonString = JSON.stringify(data);

    // Deserialize
    const deserialized = loads(jsonString);

    // Verify it's a Serializable instance
    expect(deserialized).toBeInstanceOf(Serializable);

    // Serialize back using toJSON
    const serialized = JSON.stringify((deserialized as Serializable).toJSON());

    // Parse both for comparison
    const original = JSON.parse(jsonString);
    const roundTrip = JSON.parse(serialized);

    // Compare the structures
    expect(roundTrip).toEqual(original);
  });
});
