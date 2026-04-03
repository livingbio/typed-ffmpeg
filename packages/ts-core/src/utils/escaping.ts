/**
 * Utilities for escaping special characters in FFmpeg command arguments.
 */

/**
 * Escape special characters in a string for use in FFmpeg commands.
 *
 * @param text - The text to escape (converted to string if not already)
 * @param chars - Characters that should be escaped (default: "\\'=:")
 * @returns The escaped text
 */
export function escape(text: string | number, chars: string = "\\\\'=:"): string {
  let result = String(text);
  const charList = [...new Set(chars)];

  // Process backslash first to avoid double-escaping
  const backslashIdx = charList.indexOf("\\");
  if (backslashIdx !== -1) {
    charList.splice(backslashIdx, 1);
    charList.unshift("\\");
  }

  for (const ch of charList) {
    result = result.split(ch).join("\\" + ch);
  }

  return result;
}

/**
 * Convert a dictionary to FFmpeg command-line arguments.
 *
 * @param kwargs - Parameter names and values
 * @returns List of FFmpeg CLI arguments
 */
export function convertKwargsToArgs(kwargs: Record<string, unknown>): string[] {
  const args: string[] = [];
  for (const k of Object.keys(kwargs).sort()) {
    const v = kwargs[k];
    if (Array.isArray(v)) {
      for (const value of v) {
        args.push(`-${k}`);
        if (value != null) {
          args.push(String(value));
        }
      }
      continue;
    }
    args.push(`-${k}`);
    if (v != null) {
      args.push(String(v));
    }
  }
  return args;
}
