import { render, screen, act, fireEvent } from '@testing-library/react';
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest';
import PreviewPanel from '../PreviewPanel';
import { NodeMappingManager } from '../../utils/nodeMapping';

vi.mock('../../utils/generateFFmpegCommand', () => ({
  generateFFmpegCommand: vi.fn(),
}));

import { generateFFmpegCommand } from '../../utils/generateFFmpegCommand';
const mockGenerate = generateFFmpegCommand as ReturnType<typeof vi.fn>;

describe('PreviewPanel', () => {
  beforeEach(() => {
    vi.useFakeTimers();
    // clipboard is a getter-only property in jsdom; use defineProperty to stub it
    Object.defineProperty(navigator, 'clipboard', {
      value: { writeText: vi.fn().mockResolvedValue(undefined) },
      configurable: true,
      writable: true,
    });
  });

  afterEach(() => {
    vi.useRealTimers();
    vi.clearAllMocks();
  });

  it('shows placeholder before any command is generated', () => {
    mockGenerate.mockResolvedValue({ result: '', error: null });
    const manager = new NodeMappingManager();
    render(<PreviewPanel nodeMappingManager={manager} />);

    // Debounce has not fired yet — placeholder text should be visible
    expect(
      screen.getByText(/Connect an input and output to generate a command/),
    ).toBeInTheDocument();
  });

  it('shows loading indicator while generating', async () => {
    let resolve: (v: unknown) => void;
    mockGenerate.mockReturnValue(new Promise((r) => (resolve = r)));
    const manager = new NodeMappingManager();
    render(<PreviewPanel nodeMappingManager={manager} />);

    await act(async () => {
      await vi.advanceTimersByTimeAsync(800);
    });

    expect(screen.getByText(/Generating FFmpeg command/)).toBeInTheDocument();
    // Clean up the hanging promise
    resolve!({ result: '', error: null });
  });

  it('displays the generated FFmpeg command', async () => {
    mockGenerate.mockResolvedValue({
      result: 'ffmpeg -i input.mp4 output.mp4',
      error: null,
    });
    const manager = new NodeMappingManager();
    render(<PreviewPanel nodeMappingManager={manager} />);

    await act(async () => {
      await vi.advanceTimersByTimeAsync(800);
    });

    expect(
      screen.getByText('ffmpeg -i input.mp4 output.mp4'),
    ).toBeInTheDocument();
  });

  it('displays an error message when generation fails', async () => {
    mockGenerate.mockResolvedValue({
      result: '',
      error: 'No output connected to global',
    });
    const manager = new NodeMappingManager();
    render(<PreviewPanel nodeMappingManager={manager} />);

    await act(async () => {
      await vi.advanceTimersByTimeAsync(800);
    });

    expect(
      screen.getByText(/Error generating FFmpeg command/),
    ).toBeInTheDocument();
    expect(
      screen.getByText(/No output connected to global/),
    ).toBeInTheDocument();
  });

  it('copy button is disabled when there is no command', async () => {
    mockGenerate.mockResolvedValue({ result: '', error: 'No input' });
    const manager = new NodeMappingManager();
    render(<PreviewPanel nodeMappingManager={manager} />);

    await act(async () => {
      await vi.advanceTimersByTimeAsync(800);
    });

    expect(screen.getByRole('button', { name: /copy/i })).toBeDisabled();
  });

  it('copy button is enabled and copies to clipboard when command is present', async () => {
    mockGenerate.mockResolvedValue({
      result: 'ffmpeg -i in.mp4 out.mp4',
      error: null,
    });
    const manager = new NodeMappingManager();
    render(<PreviewPanel nodeMappingManager={manager} />);

    await act(async () => {
      await vi.advanceTimersByTimeAsync(800);
    });

    expect(screen.getByText('ffmpeg -i in.mp4 out.mp4')).toBeInTheDocument();

    const copyBtn = screen.getByRole('button', { name: /copy/i });
    expect(copyBtn).not.toBeDisabled();
    fireEvent.click(copyBtn);
    expect(navigator.clipboard.writeText).toHaveBeenCalledWith(
      'ffmpeg -i in.mp4 out.mp4',
    );
  });

  it('regenerates command when manager emits an update', async () => {
    mockGenerate
      .mockResolvedValueOnce({ result: 'ffmpeg -i a.mp4 out.mp4', error: null })
      .mockResolvedValueOnce({ result: 'ffmpeg -i b.mp4 out.mp4', error: null });

    const manager = new NodeMappingManager();
    render(<PreviewPanel nodeMappingManager={manager} />);

    await act(async () => {
      await vi.advanceTimersByTimeAsync(800);
    });

    expect(screen.getByText('ffmpeg -i a.mp4 out.mp4')).toBeInTheDocument();

    // Trigger a second update by adding a node (emits 'update')
    await act(async () => {
      await manager.addNode({ type: 'input', filename: 'b.mp4' });
      await vi.advanceTimersByTimeAsync(800);
    });

    expect(screen.getByText('ffmpeg -i b.mp4 out.mp4')).toBeInTheDocument();
  });
});
