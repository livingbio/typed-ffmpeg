import { FFMpegFilter } from './ffmpeg';

declare module '../config/filters.json' {
  const value: {
    filters: FFMpegFilter[];
  };
  export default value;
}
