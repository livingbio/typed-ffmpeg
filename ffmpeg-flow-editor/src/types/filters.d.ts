import { FFmpegFilter } from './ffmpeg';

declare module '../config/filters.json' {
  const value: {
    filters: FFmpegFilter[];
  };
  export default value;
}
