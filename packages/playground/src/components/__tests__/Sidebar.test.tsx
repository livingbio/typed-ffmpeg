import { render, screen, fireEvent } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import Sidebar from '../Sidebar';
import { NodeMappingManager } from '../../utils/nodeMapping';

describe('Sidebar', () => {
  const onAddFilter = vi.fn();
  const onLoadJson = vi.fn().mockResolvedValue(undefined);
  const onLayout = vi.fn();
  const onPasteCommand = vi.fn();

  beforeEach(() => {
    vi.clearAllMocks();
  });

  function renderSidebar() {
    const manager = new NodeMappingManager();
    return render(
      <Sidebar
        onAddFilter={onAddFilter}
        nodeMappingManager={manager}
        onLoadJson={onLoadJson}
        onLayout={onLayout}
        onPasteCommand={onPasteCommand}
      />,
    );
  }

  it('renders section headers', () => {
    renderSidebar();
    expect(screen.getByText('FFmpeg Flow Editor')).toBeInTheDocument();
    expect(screen.getByText('I/O Nodes')).toBeInTheDocument();
    expect(screen.getByText(/Available Filters/)).toBeInTheDocument();
  });

  it('renders Input Node and Output Node buttons', () => {
    renderSidebar();
    expect(screen.getByText('Input Node')).toBeInTheDocument();
    expect(screen.getByText('Output Node')).toBeInTheDocument();
  });

  it('calls onAddFilter with "input" when Input Node is clicked', async () => {
    renderSidebar();
    await userEvent.click(screen.getByText('Input Node'));
    expect(onAddFilter).toHaveBeenCalledWith('input');
  });

  it('calls onAddFilter with "output" when Output Node is clicked', async () => {
    renderSidebar();
    await userEvent.click(screen.getByText('Output Node'));
    expect(onAddFilter).toHaveBeenCalledWith('output');
  });

  it('renders filter list', () => {
    renderSidebar();
    // Filters should be listed; just check the list is non-empty
    const filterItems = screen.getAllByRole('button', { hidden: true });
    expect(filterItems.length).toBeGreaterThan(0);
  });

  it('filters the list when searching', async () => {
    renderSidebar();
    const searchInput = screen.getByPlaceholderText('Search filters...');
    // Type a specific filter name that should narrow the list
    await userEvent.type(searchInput, 'scale');
    // "scale" filter should still be visible
    expect(screen.getByText('scale')).toBeInTheDocument();
  });

  it('calls onAddFilter with the filter name when a filter item is clicked', async () => {
    renderSidebar();
    // Type "scale" to find exactly the scale filter
    const searchInput = screen.getByPlaceholderText('Search filters...');
    await userEvent.type(searchInput, 'scale');
    await userEvent.click(screen.getByText('scale'));
    expect(onAddFilter).toHaveBeenCalledWith('scale');
  });

  it('calls onPasteCommand when Parse Command is clicked with text', async () => {
    renderSidebar();
    const textarea = screen.getByPlaceholderText('Paste FFmpeg command here...');
    await userEvent.type(textarea, 'ffmpeg -i in.mp4 out.mp4');
    await userEvent.click(screen.getByRole('button', { name: /Parse Command/i }));
    expect(onPasteCommand).toHaveBeenCalledWith('ffmpeg -i in.mp4 out.mp4');
  });

  it('does not call onPasteCommand when command field is empty', async () => {
    renderSidebar();
    await userEvent.click(screen.getByRole('button', { name: /Parse Command/i }));
    expect(onPasteCommand).not.toHaveBeenCalled();
  });

  it('calls onLayout when the layout button is clicked', async () => {
    renderSidebar();
    // The layout button is the AutoGraph icon button (first icon button in header)
    const buttons = screen.getAllByRole('button');
    // Layout button is rendered first in the header box
    const layoutBtn = buttons.find((btn) => btn.querySelector('svg[data-testid="AutoGraphIcon"]'));
    if (layoutBtn) {
      await userEvent.click(layoutBtn);
      expect(onLayout).toHaveBeenCalled();
    } else {
      // fallback: click the first small icon button in the header area
      fireEvent.click(buttons[0]);
      expect(onLayout).toHaveBeenCalled();
    }
  });
});
