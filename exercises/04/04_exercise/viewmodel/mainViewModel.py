from PyQt5.QtCore import QObject, pyqtSignal, QTimer
import numpy as np
from services.signal_processor import SignalProcessor

class MainViewModel(QObject):
    """
    ViewModel class that connects the signal data with the visualization.
    
    This class is part of the ViewModel layer in the MVVM architecture.
    """
    
    # Signal for the view to connect to
    data_updated = pyqtSignal(np.ndarray, np.ndarray)  # time, data
    
    def __init__(self):
        """
        Initialize the ViewModel with signal processor and timer.
        
        Sets up:
        - Signal processor with 10s window and 2048 Hz sampling
        - Timer for 30 Hz updates
        - Initial data generation
        - Fixed time window for display
        """
        super().__init__()
        self.signal_processor = SignalProcessor(window_size=10, sampling_rate=2048)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        
        # Initialize data
        self.time_points, self.raw_data = self.signal_processor.generate_test_signal(duration=60)
        self.current_index = 0
        self.is_plotting = False
        
        # Create fixed time window (0 to 10 seconds)
        self.fixed_time_window = np.linspace(0, 10, self.signal_processor.points_per_window)
        
        # Set update interval to 30 Hz
        self.timer.setInterval(33)  # 1000ms/30Hz ≈ 33ms
        
    def start_plotting(self):
        """
        Start the live plotting.
        
        This method:
        - Sets the plotting state to active
        - Starts the update timer
        """
        if not self.is_plotting:
            self.is_plotting = True
            self.timer.start()
            
    def stop_plotting(self):
        """
        Stop the live plotting.
        
        This method:
        - Sets the plotting state to inactive
        - Stops the update timer
        """
        if self.is_plotting:
            self.is_plotting = False
            self.timer.stop()
            
    def update_data(self):
        """
        Update the data window and emit new data.
        
        This method is called by the timer at 30 Hz. You need to:
        1. Get the current window of data:
           - Use self.signal_processor.points_per_window to get the window size
           - Calculate end_idx as min(self.current_index + window_size, len(self.time_points))
           - Get data_window from self.raw_data[self.current_index:end_idx]
        
        2. Handle window padding if needed:
           - If len(data_window) < window_size, pad with zeros using np.pad
           - The padding should be (0, window_size - len(data_window))
        
        3. Emit the new data:
           - Use self.data_updated.emit() with self.fixed_time_window and data_window
        
        4. Update the current index:
           - Move by 1/30th of a second worth of samples
           - Use self.signal_processor.sampling_rate // 30
        
        5. Handle end of data reset:
           - If current_index >= len(self.time_points) - window_size
           - Reset current_index to 0
        
        Available variables:
        - self.signal_processor.points_per_window: Number of points in the window
        - self.signal_processor.sampling_rate: Samples per second (2048 Hz)
        - self.time_points: Full array of time points
        - self.raw_data: Full array of signal data
        - self.current_index: Current position in the data
        - self.fixed_time_window: Fixed time window for display (0 to 10 seconds)
        """
        # TODO: Implement the data update logic as described above
        pass
            
