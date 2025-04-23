import { readdirSync, readFileSync, writeFileSync } from 'fs';
import { join, basename, dirname } from 'path';
import { fileURLToPath } from 'url';
import { FFmpegFilter, FilterParameter } from '@/types/ffmpeg';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const CACHE_DIR = join(__dirname, '../../../src/scripts/cache/FFMpegFilter');

function readCacheFiles(): string[] {
  return readdirSync(CACHE_DIR)
    .filter((file: string) => file.endsWith('.json'))
    .map((file: string) => join(CACHE_DIR, file));
}

function mapOptionToParameter(option: any): FilterParameter {
  const validation: { min?: number; max?: number; pattern?: string } = {};

  if (option.type.value === 'int' || option.type.value === 'float') {
    if (option.min !== null) validation.min = parseFloat(option.min);
    if (option.max !== null) validation.max = parseFloat(option.max);
  }

  return {
    name: option.name,
    type: option.type.value === 'int' || option.type.value === 'float' ? 'number' :
          option.type.value === 'boolean' ? 'boolean' : 'string',
    description: option.description,
    required: option.required,
    default: option.default === 'auto' || option.default === null ? undefined :
            option.type.value === 'int' ? parseInt(option.default) :
            option.type.value === 'float' ? parseFloat(option.default) :
            option.default,
    validation: Object.keys(validation).length > 0 ? validation : undefined
  };
}

function parseFilterFile(filePath: string): FFmpegFilter | null {
  try {
    const content = readFileSync(filePath, 'utf-8');
    // Replace NaN with null in the JSON string
    const sanitizedContent = content.replace(/:\s*NaN/g, ': null');
    const filterData = JSON.parse(sanitizedContent);

    return {
      name: filterData.name,
      label: filterData.name.charAt(0).toUpperCase() + filterData.name.slice(1),
      description: filterData.description,
      parameters: filterData.options?.map(mapOptionToParameter) || [],
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

  const outputPath = join(__dirname, '../config/filters.json');
  writeFileSync(outputPath, JSON.stringify(output, null, 2));

  console.log(`Generated ${filters.length} filters in ${outputPath}`);
}

generateFiltersJson();
