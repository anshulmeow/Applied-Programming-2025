# Live RMS Signal Plotting Exercise

This exercise implements a real-time signal plotting application using the MVVM (Model-View-ViewModel) architecture pattern. The application displays a live plot of a signal's Root Mean Square (RMS) value over time, demonstrating the use of PyQt5 for the UI and VisPy for high-performance plotting.

## Application Overview

The application provides:
- A live plot showing the RMS value of a signal over time
- A control button to start/stop the plotting
- A fixed view range for consistent visualization
- Real-time updates at 30 Hz

## MVVM Architecture

The application follows the MVVM (Model-View-ViewModel) pattern, which separates the application into three main components:

### Model
- Handles data generation and signal processing
- Provides raw signal data and RMS calculations
- Already implemented for you

### View
- Manages the user interface components
- Consists of two main classes:
  1. `MainView`: Main window with plot and controls
  2. `VisPyPlotWidget`: Custom widget for high-performance plotting
- Contains TODOs for UI setup and signal connections

### ViewModel
- Acts as a mediator between Model and View
- Manages the application state and business logic
- Handles data updates and plotting state
- Contains TODOs for signal processing and state management

## Implementation Tasks

### 1. Main Application (`main.py`)
TODOs:
- Import necessary classes (MainView and MainViewModel)
- Create ViewModel instance
- Create View instance with ViewModel
- Show the main window

### 2. View Layer (`view/mainView.py`)
TODOs:
- Connect ViewModel signals to appropriate slots
- Implement plotting toggle functionality

### 3. Plot Widget (`view/plotView.py`)
TODOs:
- Set up the VisPy canvas and layout
- Create and configure the plot view
- Implement the line plot visualization
- Set up fixed view ranges
- Implement data update mechanism

### 4. ViewModel Layer (`viewmodel/mainViewModel.py`)
TODOs:
- Implement the update_data method to:
  - Get current window of data
  - Handle window padding
  - Emit new data
  - Update current index
  - Handle end of data reset

## VisPy Guide

VisPy is a high-performance visualization library that uses OpenGL for efficient plotting. Here's a basic example of how to create a simple line plot with VisPy:

```python
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from vispy import scene
import numpy as np

class SimplePlotWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Create layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Create canvas
        self.canvas = scene.SceneCanvas(keys='interactive', size=(800, 400))
        layout.addWidget(self.canvas.native)
        
        # Create view
        self.view = self.canvas.central_widget.add_view()
        self.view.camera = 'panzoom'
        
        # Create line plot
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        self.line = scene.Line(np.column_stack((x, y)), parent=self.view.scene)
        
        # Set view range
        self.view.camera.set_range(x=(0, 10), y=(-1, 1))
```

Key VisPy concepts:
1. **Canvas**: The main drawing area (SceneCanvas)
2. **View**: A region of the canvas where visuals are drawn
3. **Camera**: Controls how the view is displayed (panzoom for interactive navigation)
4. **Visuals**: Objects that can be drawn (Line, Markers, etc.)
5. **Scene**: The container for all visuals

Common operations:
- Creating a line: `scene.Line(data, parent=view.scene)`
- Updating data: `line.set_data(new_data)`
- Setting view range: `view.camera.set_range(x=(min, max), y=(min, max))`
- Updating canvas: `canvas.update()`

## Technical Details

### Signal Processing
- Window size: 10 seconds
- Sampling rate: 2048 Hz
- Update rate: 30 Hz
- Signal type: Sine wave with added noise

### Dependencies
- PyQt5: For the user interface
- NumPy: For numerical computations
- VisPy: For high-performance OpenGL-based plotting

## Getting Started

1. Review the code structure and TODOs in each file
2. Implement the missing components in the following order:
   - Main application setup
   - Plot widget setup and visualization
   - View signal connections
   - ViewModel data update logic
3. Test the application by running `main.py`

## Tips for Implementation

1. **Main Application**:
   - Import classes from the correct modules
   - Create ViewModel before View
   - Show the window after setup

2. **View Layer**:
   - Use PyQt5's signal-slot mechanism for UI updates
   - Connect all necessary signals to their slots

3. **Plot Widget**:
   - Use VisPy's SceneCanvas for efficient plotting
   - Maintain fixed view ranges for consistent visualization
   - Handle data updates efficiently

4. **ViewModel Layer**:
   - Handle window padding correctly
   - Update the current index properly
   - Reset when reaching the end of data

## Testing

After implementation, verify that:
- The plot updates smoothly in real-time
- The start/stop button works correctly
- The view range remains fixed
- The application handles data updates efficiently 