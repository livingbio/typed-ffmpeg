import { describe, it, expect } from "vitest";
import { commandLine, run, runAsync, runAwaitable } from "../utils/run.js";
import { FFMpegExecuteError } from "../exceptions.js";
import { convertKwargsToArgs } from "../utils/escaping.js";

// ─── commandLine ────────────────────────────────────────────────────────────

describe("commandLine", () => {
  it("joins simple args with spaces", () => {
    expect(commandLine(["-i", "input.mp4", "output.mp4"])).toBe(
      "-i input.mp4 output.mp4",
    );
  });

  it("does not quote args with only alphanumeric, =, and : characters", () => {
    // = and : are in the allowed set [a-zA-Z0-9_\-/.=:]
    const result = commandLine(["scale=w=1280:h=720"]);
    expect(result).toBe("scale=w=1280:h=720");
  });

  it("quotes args with spaces", () => {
    const result = commandLine(["file name.mp4"]);
    expect(result).toMatch(/^'.+'$/);
    expect(result).toContain("file name.mp4");
  });

  it("handles empty arg list", () => {
    expect(commandLine([])).toBe("");
  });

  it("does not quote simple alphanumeric args", () => {
    expect(commandLine(["ffmpeg", "-y", "output.mp4"])).toBe(
      "ffmpeg -y output.mp4",
    );
  });
});

// ─── run ────────────────────────────────────────────────────────────────────

describe("run", () => {
  it("returns stdout for a successful command", () => {
    const result = run(["hello"], "echo");
    expect(result.stdout.toString().trim()).toBe("hello");
  });

  it("throws FFMpegExecuteError on non-zero exit", () => {
    expect(() => run([], "false")).toThrow(FFMpegExecuteError);
  });

  it("FFMpegExecuteError contains cmd and retcode", () => {
    try {
      run([], "false");
    } catch (e) {
      expect(e).toBeInstanceOf(FFMpegExecuteError);
      const err = e as FFMpegExecuteError;
      expect(err.retcode).not.toBeNull();
      expect(err.cmd).toContain("false");
    }
  });
});

// ─── runAsync ───────────────────────────────────────────────────────────────

describe("runAsync", () => {
  it("returns a ChildProcess handle", () => {
    const proc = runAsync(["hello"], "echo");
    expect(proc).toBeDefined();
    expect(typeof proc.pid).toBe("number");
    proc.kill();
  });
});

// ─── runAwaitable ───────────────────────────────────────────────────────────

describe("runAwaitable", () => {
  it("resolves with stdout for a successful command", async () => {
    const result = await runAwaitable(["hello"], "echo");
    expect(result.stdout.toString().trim()).toBe("hello");
    expect(result.stderr).toBeDefined();
  });

  it("rejects with FFMpegExecuteError on non-zero exit", async () => {
    await expect(runAwaitable([], "false")).rejects.toBeInstanceOf(FFMpegExecuteError);
  });

  it("rejects when binary does not exist", async () => {
    await expect(runAwaitable([], "nonexistent-binary-xyz")).rejects.toThrow();
  });
});

// ─── convertKwargsToArgs ────────────────────────────────────────────────────

describe("convertKwargsToArgs", () => {
  it("converts key-value pairs to -k v pairs, sorted by key", () => {
    const result = convertKwargsToArgs({ b: "128k", a: "libmp3lame" });
    expect(result).toEqual(["-a", "libmp3lame", "-b", "128k"]);
  });

  it("handles array values by repeating the flag", () => {
    const result = convertKwargsToArgs({ map: ["0:v", "0:a"] });
    expect(result).toEqual(["-map", "0:v", "-map", "0:a"]);
  });

  it("handles array with null value (flag only)", () => {
    const result = convertKwargsToArgs({ map: [null] });
    expect(result).toEqual(["-map"]);
  });

  it("omits the value when it is null", () => {
    const result = convertKwargsToArgs({ flag: null });
    expect(result).toEqual(["-flag"]);
  });

  it("handles numeric values", () => {
    const result = convertKwargsToArgs({ crf: 23 });
    expect(result).toEqual(["-crf", "23"]);
  });
});
