import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import FilterNode from '../FilterNode';
import { predefinedFilters } from '../../types/ffmpeg';

// Mock the CustomEvent
class MockCustomEvent extends Event {
  detail: unknown;
  constructor(type: string, eventInitDict?: CustomEventInit) {
    super(type, eventInitDict);
    this.detail = eventInitDict?.detail;
  }
}

// Mock the window.CustomEvent
Object.defineProperty(window, 'CustomEvent', {
  value: MockCustomEvent,
});

describe('FilterNode', () => {
  const mockNodeProps = {
    id: 'test-node',
    data: {
      label: 'Test Filter',
      filterType: 'filter' as const,
      filterName: 'test_filter',
      parameters: {},
    },
    selected: false,
    dragging: false,
    zIndex: 0,
    type: 'filter',
    position: { x: 0, y: 0 },
    width: 200,
    height: 100,
    isConnectable: true,
    xPos: 0,
    yPos: 0,
  };

  it('should render with static input/output streams', () => {
    render(<FilterNode {...mockNodeProps} />);
    expect(screen.getByText('Test Filter')).toBeInTheDocument();
  });

  it('should handle dynamic input streams', () => {
    // Find a filter with dynamic inputs
    const dynamicFilter = predefinedFilters.find((f) => f.is_dynamic_input);
    if (!dynamicFilter) {
      throw new Error('No dynamic input filter found in predefined filters');
    }

    const props = {
      ...mockNodeProps,
      data: {
        ...mockNodeProps.data,
        filterName: dynamicFilter.name,
        parameters: { inputs: '2' },
      },
    };

    render(<FilterNode {...props} />);

    // Check if the input handles are rendered correctly
    const inputHandles = screen.getAllByTestId('input-handle');
    expect(inputHandles).toHaveLength(2);
  });

  it('should handle dynamic output streams', () => {
    // Find a filter with dynamic outputs
    const dynamicFilter = predefinedFilters.find((f) => f.is_dynamic_output);
    if (!dynamicFilter) {
      throw new Error('No dynamic output filter found in predefined filters');
    }

    const props = {
      ...mockNodeProps,
      data: {
        ...mockNodeProps.data,
        filterName: dynamicFilter.name,
        parameters: { outputs: '2' },
      },
    };

    render(<FilterNode {...props} />);

    // Check if the output handles are rendered correctly
    const outputHandles = screen.getAllByTestId('output-handle');
    expect(outputHandles).toHaveLength(2);
  });

  it('should update streams when parameters change', () => {
    // Find a filter with dynamic inputs
    const dynamicFilter = predefinedFilters.find((f) => f.is_dynamic_input);
    if (!dynamicFilter) {
      throw new Error('No dynamic input filter found in predefined filters');
    }

    const props = {
      ...mockNodeProps,
      data: {
        ...mockNodeProps.data,
        filterName: dynamicFilter.name,
        parameters: { inputs: '1' },
      },
    };

    render(<FilterNode {...props} />);

    // Initial number of input handles
    let inputHandles = screen.getAllByTestId('input-handle');
    expect(inputHandles).toHaveLength(1);

    // Update the parameter
    const inputField = screen.getByLabelText('inputs');
    fireEvent.change(inputField, { target: { value: '3' } });

    // Check if the input handles are updated
    inputHandles = screen.getAllByTestId('input-handle');
    expect(inputHandles).toHaveLength(3);
  });

  it('should validate parameters', () => {
    const props = {
      ...mockNodeProps,
      data: {
        ...mockNodeProps.data,
        parameters: { width: 'invalid' },
      },
    };

    render(<FilterNode {...props} />);

    // Check if error message is displayed
    const errorMessage = screen.getByText('Must be a number');
    expect(errorMessage).toBeInTheDocument();
  });

  it('should handle parameter changes', () => {
    const handleNodeDataUpdate = jest.fn();
    window.addEventListener('updateNodeData', handleNodeDataUpdate);

    render(<FilterNode {...mockNodeProps} />);

    // Change a parameter
    const inputField = screen.getByLabelText('width');
    fireEvent.change(inputField, { target: { value: '1920' } });

    // Check if the event was dispatched
    expect(handleNodeDataUpdate).toHaveBeenCalled();

    window.removeEventListener('updateNodeData', handleNodeDataUpdate);
  });
});
