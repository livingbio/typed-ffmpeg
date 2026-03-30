import { render, screen, fireEvent } from '@testing-library/react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import FilterNode from '../FilterNode';
import { NodeData } from '../../types/node';

// Mock reactflow – Handle is just a no-op div, hooks return stubs
vi.mock('reactflow', () => ({
  Handle: ({ type, position, id }: { type: string; position: string; id: string }) => (
    <div data-testid={`handle-${type}-${id}`} data-position={position} />
  ),
  Position: { Left: 'left', Right: 'right' },
  useUpdateNodeInternals: () => vi.fn(),
}));

const makeNodeProps = (overrides: Partial<NodeData> = {}) => {
  const data: NodeData = {
    label: 'scale',
    nodeType: 'filter',
    filterName: 'scale',
    parameters: {},
    handles: {
      inputs: [{ id: 'input-0', type: 'video' }],
      outputs: [{ id: 'output-0', type: 'video' }],
    },
    filter: {
      __class__: 'FFMpegFilter',
      id: null,
      name: 'scale',
      description: 'Scale the input video size and/or convert the image format.',
      ref: '',
      is_support_slice_threading: true,
      is_support_timeline: false,
      is_support_framesync: false,
      is_support_command: false,
      is_filter_sink: false,
      is_filter_source: false,
      is_dynamic_input: false,
      is_dynamic_output: false,
      stream_typings_input: [],
      stream_typings_output: [],
      formula_typings_input: null,
      formula_typings_output: null,
      pre: [],
      options: [
        {
          __class__: 'FFMpegFilterOption',
          name: 'w',
          alias: ['width'],
          description: 'Output video width',
          type: { __class__: 'FFMpegFilterOptionType', value: 'string' },
          min: null,
          max: null,
          default: 'iw',
          required: false,
          choices: [],
          flags: '',
        },
        {
          __class__: 'FFMpegFilterOption',
          name: 'h',
          alias: ['height'],
          description: 'Output video height',
          type: { __class__: 'FFMpegFilterOptionType', value: 'string' },
          min: null,
          max: null,
          default: 'ih',
          required: false,
          choices: [],
          flags: '',
        },
        {
          __class__: 'FFMpegFilterOption',
          name: 'flags',
          alias: [],
          description: 'Scaling flags',
          type: { __class__: 'FFMpegFilterOptionType', value: 'string' },
          min: null,
          max: null,
          default: '',
          required: false,
          choices: [],
          flags: '',
        },
        {
          __class__: 'FFMpegFilterOption',
          name: 'interl',
          alias: [],
          description: 'Set the interlacing mode',
          type: { __class__: 'FFMpegFilterOptionType', value: 'int' },
          min: '-1',
          max: '1',
          default: '0',
          required: false,
          choices: [],
          flags: '',
        },
      ],
    },
    ...overrides,
  };
  return {
    id: 'node-1',
    data,
    selected: false,
    type: 'filter',
    zIndex: 0,
    isConnectable: true,
    xPos: 0,
    yPos: 0,
    dragging: false,
  } as Parameters<typeof FilterNode>[0];
};

describe('FilterNode', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('renders the filter label', () => {
    render(<FilterNode {...makeNodeProps()} />);
    expect(screen.getByRole('heading', { name: 'scale' })).toBeInTheDocument();
  });

  it('renders filter description', () => {
    render(<FilterNode {...makeNodeProps()} />);
    expect(
      screen.getByText(/Scale the input video size/),
    ).toBeInTheDocument();
  });

  it('renders input and output handles', () => {
    render(<FilterNode {...makeNodeProps()} />);
    expect(screen.getByTestId('handle-target-input-0')).toBeInTheDocument();
    expect(screen.getByTestId('handle-source-output-0')).toBeInTheDocument();
  });

  it('shows first 3 options by default', () => {
    render(<FilterNode {...makeNodeProps()} />);
    expect(screen.getByLabelText('w')).toBeInTheDocument();
    expect(screen.getByLabelText('h')).toBeInTheDocument();
    expect(screen.getByLabelText('flags')).toBeInTheDocument();
    // 4th option should not be visible
    expect(screen.queryByLabelText('interl')).not.toBeInTheDocument();
  });

  it('shows More button when options exceed 3', () => {
    render(<FilterNode {...makeNodeProps()} />);
    expect(screen.getByRole('button', { name: /More/i })).toBeInTheDocument();
  });

  it('expands to show all options when More is clicked', () => {
    render(<FilterNode {...makeNodeProps()} />);
    fireEvent.click(screen.getByRole('button', { name: /More/i }));
    expect(screen.getByLabelText('interl')).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Less/i })).toBeInTheDocument();
  });

  it('collapses back when Less is clicked', () => {
    render(<FilterNode {...makeNodeProps()} />);
    fireEvent.click(screen.getByRole('button', { name: /More/i }));
    fireEvent.click(screen.getByRole('button', { name: /Less/i }));
    expect(screen.queryByLabelText('interl')).not.toBeInTheDocument();
  });

  it('dispatches updateNodeData event when a parameter is changed', () => {
    const eventSpy = vi.fn();
    window.addEventListener('updateNodeData', eventSpy);

    render(<FilterNode {...makeNodeProps()} />);
    fireEvent.change(screen.getByLabelText('w'), { target: { value: '1280' } });

    expect(eventSpy).toHaveBeenCalledOnce();
    const detail = (eventSpy.mock.calls[0][0] as CustomEvent).detail;
    expect(detail.data.parameters.w).toBe('1280');

    window.removeEventListener('updateNodeData', eventSpy);
  });

  it('shows a validation error for out-of-range numeric value', () => {
    render(<FilterNode {...makeNodeProps()} />);
    // Expand to see interl
    fireEvent.click(screen.getByRole('button', { name: /More/i }));
    // interl has min=-1, max=1; enter 99 to trigger max error
    fireEvent.change(screen.getByLabelText('interl'), { target: { value: '99' } });
    expect(screen.getByText(/Must be at most 1/)).toBeInTheDocument();
  });

  it('shows a validation error for non-numeric value in int field', () => {
    render(<FilterNode {...makeNodeProps()} />);
    fireEvent.click(screen.getByRole('button', { name: /More/i }));
    fireEvent.change(screen.getByLabelText('interl'), { target: { value: 'abc' } });
    expect(screen.getByText(/Must be a number/)).toBeInTheDocument();
  });
});
