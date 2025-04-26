import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { FFmpegFilter } from '../types/ffmpeg';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const CACHE_DIR = path.join(__dirname, '../../../src/scripts/cache/FFMpegFilter');

function readCacheFiles(): string[] {
  return fs
    .readdirSync(CACHE_DIR)
    .filter((file: string) => file.endsWith('.json'))
    .map((file: string) => path.join(CACHE_DIR, file));
}

function parseFilterFile(filePath: string): FFmpegFilter | null {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    // Replace NaN with null in the JSON string
    const sanitizedContent = content.replace(/:\s*NaN/g, ': null');
    const filterData = JSON.parse(sanitizedContent);

    return {
      __class__: 'FFMpegFilter',
      id: filterData.id,
      name: filterData.name,
      description: filterData.description,
      ref: filterData.ref,
      is_support_slice_threading: filterData.is_support_slice_threading,
      is_support_timeline: filterData.is_support_timeline,
      is_support_framesync: filterData.is_support_framesync,
      is_support_command: filterData.is_support_command,
      is_filter_sink: filterData.is_filter_sink,
      is_filter_source: filterData.is_filter_source,
      is_dynamic_input: filterData.is_dynamic_input,
      is_dynamic_output: filterData.is_dynamic_output,
      stream_typings_input: filterData.stream_typings_input,
      stream_typings_output: filterData.stream_typings_output,
      formula_typings_input: filterData.formula_typings_input,
      formula_typings_output: filterData.formula_typings_output,
      pre: filterData.pre,
      options: filterData.options,
    };
  } catch (error) {
    console.error(`Error parsing filter file ${filePath}:`, error);
    return null;
  }
}

function generateFiltersJson(): void {
  const files = readCacheFiles();
  const filters = files
    .map(parseFilterFile)
    .filter((filter): filter is FFmpegFilter => filter !== null);

  const output = {
    filters,
  };

  const outputPath = path.join(__dirname, '../config/filters.json');
  fs.writeFileSync(outputPath, JSON.stringify(output, null, 2));

  console.log(`Generated ${filters.length} filters in ${outputPath}`);
}

generateFiltersJson();
