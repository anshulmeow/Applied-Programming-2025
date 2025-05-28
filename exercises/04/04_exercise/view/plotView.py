from PyQt5.QtWidgets import QWidget, QVBoxLayout
from vispy import app, scene
import numpy as np

class VisPyPlotWidget(QWidget):
    """
    A widget that displays live plotting using VisPy.
    
    This class is part of the View layer in the MVVM architecture. It:
    - Creates and manages the VisPy canvas
    - Handles the visualization of the signal
    - Maintains a fixed view range
    - Updates the plot with new data
    
    The widget uses VisPy for high-performance OpenGL-based plotting,
    which is essential for smooth real-time updates.
    """
    
    def __init__(self, parent=None):
        """
        Initialize the plot widget with VisPy canvas and view.
        
        Args:
            parent: Parent widget (optional)
        """
        super().__init__(parent)
        
        # TODO: Set up the widget
        # First, create a QVBoxLayout to organize the widget's contents
        # Then, set this layout as the widget's layout using setLayout()
        # This layout will hold the VisPy canvas
        
        # TODO: Create VisPy canvas
        # Create a SceneCanvas with size (800, 400) for the plot
        # The canvas is the main drawing area for VisPy
        # Add the canvas to the layout using addWidget(canvas.native)
        # The .native property is needed because VisPy's canvas needs to be converted to a Qt widget
        
        # TODO: Create view
        # Add a view to the canvas's central widget
        # Set the camera to 'panzoom' to allow interactive navigation
        # The view is where we'll add our plot elements
        
        # TODO: Create line plot
        # Create a Line visual with initial data [[0, 0]]
        # Add this line to the view's scene
        # This line will be updated with new data points
        
        # TODO: Set up view range
        # Set a fixed range for the x-axis (0 to 10 seconds)
        # Set a fixed range for the y-axis (-10 to 10 for RMS values)
        # This ensures the plot maintains a consistent view
        
    def update_data(self, time_points, data):
        """
        Update the plot with new data.
        
        This method is called whenever new data is available. It:
        - Creates a new line data array from time and signal data
        - Updates the plot with the new data
        - Maintains the fixed view range
        
        Args:
            time_points (np.ndarray): Array of time values
            data (np.ndarray): Array of signal values
        """
        # TODO: Update plot data
        # 1. Create the line data by stacking time_points and data arrays
        #    Use np.column_stack() to combine them into a 2D array
        #    Each row will be [time, value] pair
        # 2. Update the line visual with the new data using set_data()
        # 3. Keep the view range fixed by setting the camera range again
        # 4. Update the canvas to show the changes
        # This method is called by the ViewModel when new data is available
        pass 