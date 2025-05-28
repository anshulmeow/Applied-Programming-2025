from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from .plotView import VisPyPlotWidget

# TODO: Import the PlotView class from plotView

class MainView(QMainWindow):
    """
    Main application window that combines the plot widget and controls.
    
    This class is part of the View layer in the MVVM architecture. It:
    - Creates and manages the main window layout
    - Contains the plot widget and control buttons
    - Connects the ViewModel signals to the View
    - Handles user interactions
    
    The window provides a simple interface with:
    - A plot widget showing the live signal
    - A button to start/stop the plotting
    """
    
    def __init__(self, view_model):
        """
        Initialize the main window with plot widget and controls.
        
        Args:
            view_model: The ViewModel that manages the data and plotting state
        """
        super().__init__()
        self.view_model = view_model
        
        # Set up the main window
        self.setWindowTitle("Live RMS Plot")
        self.setGeometry(100, 100, 800, 500)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create plot widget
        self.plot_widget = VisPyPlotWidget()
        layout.addWidget(self.plot_widget)
        
        # Create control button
        self.control_button = QPushButton("Start Plotting")
        self.control_button.clicked.connect(self.toggle_plotting)
        layout.addWidget(self.control_button)
        
        # TODO: Connect view model signals
        # In MVVM, the View needs to connect to the ViewModel's signals to receive updates
        # The ViewModel has a signal called 'data_updated' that emits new data
        # You need to connect this signal to the plot widget's update_data method
        # This is how the ViewModel communicates new data to the View
        # Hint: Use the connect() method on the signal, similar to how the button's clicked signal is connected
        
    def toggle_plotting(self):
        """
        Toggle the plotting state and update button text.
        """
        # TODO: Implement plotting toggle
        # This method is called when the control button is clicked
        # You need to:
        # 1. Check the current plotting state using view_model.is_plotting
        # 2. If plotting is active:
        #    - Update button text to "Start Plotting"
        #    - Call view_model.stop_plotting() to stop the data flow
        # 3. If plotting is inactive:
        #    - Update button text to "Stop Plotting"
        #    - Call view_model.start_plotting() to start the data flow
        # This method demonstrates the View's role in handling user input and updating the UI
        pass 