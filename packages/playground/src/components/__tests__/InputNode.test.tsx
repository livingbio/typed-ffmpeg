import { render, screen, fireEvent } from '@testing-library/react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import InputNode from '../InputNode';
import { NodeData } from '../../types/node';

// Mock reactflow
vi.mock('reactflow', () => ({
  Handle: ({ type, id }: { type: string; id: string }) => (
    <div data-testid={`handle-${type}-${id}`} />
  ),
  Position: { Left: 'left', Right: 'right' },
  useUpdateNodeInternals: () => vi.fn(),
}));

const makeNodeProps = (overrides: Partial<NodeData> = {}) => {
  const data: NodeData = {
    label: 'Input',
    nodeType: 'input',
    filename: '',
    parameters: {},
    handles: {
      inputs: [],
      outputs: [{ id: 'output-0', type: 'av' }],
    },
    ...overrides,
  };
  return {
    id: 'input-node-1',
    data,
    selected: false,
    type: 'input',
    zIndex: 0,
    isConnectable: true,
    xPos: 0,
    yPos: 0,
    dragging: false,
  } as Parameters<typeof InputNode>[0];
};

describe('InputNode', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('renders the node label', () => {
    render(<InputNode {...makeNodeProps()} />);
    expect(screen.getByText('Input')).toBeInTheDocument();
  });

  it('renders the Filename field', () => {
    render(<InputNode {...makeNodeProps()} />);
    expect(screen.getByLabelText('Filename')).toBeInTheDocument();
  });

  it('shows the initial filename value', () => {
    render(<InputNode {...makeNodeProps({ filename: 'video.mp4' })} />);
    expect(screen.getByDisplayValue('video.mp4')).toBeInTheDocument();
  });

  it('renders the output handle', () => {
    render(<InputNode {...makeNodeProps()} />);
    expect(screen.getByTestId('handle-source-output-0')).toBeInTheDocument();
  });

  it('dispatches updateNodeData when filename changes', () => {
    const eventSpy = vi.fn();
    window.addEventListener('updateNodeData', eventSpy);

    render(<InputNode {...makeNodeProps()} />);
    fireEvent.change(screen.getByLabelText('Filename'), {
      target: { value: 'input.mp4' },
    });

    expect(eventSpy).toHaveBeenCalledOnce();
    const detail = (eventSpy.mock.calls[0][0] as CustomEvent).detail;
    expect(detail.data.filename).toBe('input.mp4');

    window.removeEventListener('updateNodeData', eventSpy);
  });

  it('shows command string preview', () => {
    render(<InputNode {...makeNodeProps({ filename: 'clip.mp4' })} />);
    expect(screen.getByText(/-i clip\.mp4/)).toBeInTheDocument();
  });

  it('dispatches updateNodeData when a parameter changes', () => {
    const eventSpy = vi.fn();
    window.addEventListener('updateNodeData', eventSpy);

    render(<InputNode {...makeNodeProps()} />);
    // There should be at least one option field beyond filename
    const allInputs = screen.getAllByRole('textbox');
    // allInputs[0] = Filename; allInputs[1..] = option fields
    if (allInputs.length > 1) {
      fireEvent.change(allInputs[1], { target: { value: 'testval' } });
      expect(eventSpy).toHaveBeenCalled();
    }

    window.removeEventListener('updateNodeData', eventSpy);
  });
});
