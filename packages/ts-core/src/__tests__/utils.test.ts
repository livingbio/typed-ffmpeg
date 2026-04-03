import { describe, it, expect } from "vitest";
import { Default, Auto, isDefault, isAuto } from "../utils/types.js";
import { merge, ignoreDefault } from "../utils/frozenRecord.js";
import { escape } from "../utils/escaping.js";
import { isDAG } from "../dag/utils.js";

describe("Default and Auto", () => {
  it("Default holds a value", () => {
    const d = new Default("23");
    expect(d.value).toBe("23");
    expect(d.toString()).toBe("23");
    expect(isDefault(d)).toBe(true);
    expect(isAuto(d)).toBe(false);
  });

  it("Auto extends Default", () => {
    const a = new Auto("len(streams)");
    expect(a.value).toBe("len(streams)");
    expect(isDefault(a)).toBe(true);
    expect(isAuto(a)).toBe(true);
  });

  it("non-Default values are not detected", () => {
    expect(isDefault("hello")).toBe(false);
    expect(isDefault(42)).toBe(false);
    expect(isDefault(null)).toBe(false);
  });
});

describe("merge", () => {
  it("merges multiple records", () => {
    const result = merge({ a: 1 }, { b: "two" }, { c: true });
    expect(result).toEqual({ a: 1, b: "two", c: true });
  });

  it("skips null/undefined maps", () => {
    const result = merge({ a: 1 }, null, undefined, { b: 2 });
    expect(result).toEqual({ a: 1, b: 2 });
  });

  it("skips null/undefined values", () => {
    const result = merge({ a: 1, b: null, c: undefined } as Record<string, unknown>);
    expect(result).toEqual({ a: 1 });
  });

  it("skips Default values", () => {
    const result = merge({ a: 1, b: new Default("x") } as Record<string, unknown>);
    expect(result).toEqual({ a: 1 });
  });

  it("later values override earlier", () => {
    const result = merge({ a: 1 }, { a: 2 });
    expect(result).toEqual({ a: 2 });
  });

  it("returns frozen object", () => {
    const result = merge({ a: 1 });
    expect(Object.isFrozen(result)).toBe(true);
  });
});

describe("ignoreDefault", () => {
  it("removes Default values", () => {
    const result = ignoreDefault({ a: 1, b: new Default("x"), c: "hello" });
    expect(result).toEqual({ a: 1, c: "hello" });
  });
});

describe("escape", () => {
  it("escapes special characters", () => {
    expect(escape("a=b")).toContain("\\=");
    expect(escape("a:b")).toContain("\\:");
  });

  it("handles numeric input", () => {
    expect(escape(42)).toBe("42");
  });
});

describe("isDAG", () => {
  it("returns true for a simple DAG", () => {
    expect(
      isDAG({ A: new Set(["B"]), B: new Set(["C"]), C: new Set() }),
    ).toBe(true);
  });

  it("returns false for a cycle", () => {
    expect(
      isDAG({ A: new Set(["B"]), B: new Set(["C"]), C: new Set(["A"]) }),
    ).toBe(false);
  });

  it("returns true for a single node", () => {
    expect(isDAG({ A: new Set() })).toBe(true);
  });
});
