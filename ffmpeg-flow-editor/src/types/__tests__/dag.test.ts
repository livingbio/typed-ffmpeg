import { readFileSync, readdirSync } from "node:fs";
import { join } from "node:path";
import { beforeAll, describe, expect, it } from "vitest";
import { clearClassRegistry, loads, registerClasses } from "../../utils/serialize";
import { Serializable } from "../../utils/serialize";

// Import all DAG classes to register them
import {
  AVStream,
  AudioStream,
  FilterNode,
  FilterableStream,
  GlobalNode,
  GlobalStream,
  InputNode,
  OutputNode,
  OutputStream,
  StreamType,
  VideoStream,
} from "../dag";

// Clear and register classes before tests
beforeAll(() => {
  clearClassRegistry();

  // Register all classes explicitly
  registerClasses({
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
  });
});

// Get all JSON files from the test data directory
const testDataDir = join(__dirname, "__testdata__");
const testFiles = readdirSync(testDataDir)
  .filter((file) => file.endsWith(".json"))
  .map((file) => ({
    name: file.replace(".json", ""),
    data: JSON.parse(readFileSync(join(testDataDir, file), "utf-8")),
  }));

describe("DAG Serialization", () => {
  it.each(testFiles)("should handle $name case", ({ data }) => {
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
