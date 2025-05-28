import numpy as np

class SignalProcessor:
    """
    Service class for signal processing and generation.
    
    This class is part of the Model layer in the MVVM architecture.
    """
    
    def __init__(self, window_size=10, sampling_rate=2048):
        """
        Initialize the signal processor.
        
        Args:
            window_size: Size of the time window in seconds
            sampling_rate: Sampling rate in Hz
        """
        self.window_size = window_size
        self.sampling_rate = sampling_rate
        self.points_per_window = window_size * sampling_rate
        
    def generate_test_signal(self, duration=60):
        """
        Generate a test signal (sine wave with noise).
        
        Args:
            duration: Duration of the signal in seconds
            
        Returns:
            tuple: (time_points, signal_data)
        """
        # Generate time points
        time_points = np.linspace(0, duration, int(duration * self.sampling_rate))
        
        # Generate sine wave (1 Hz) with noise
        signal = np.sin(2 * np.pi * time_points) + 0.1 * np.random.randn(len(time_points))
        
        return time_points, signal
        
    def get_window(self, data, start_idx, window_size):
        """
        Get a window of data.
        
        Args:
            data: Full signal data array
            start_idx: Starting index
            window_size: Size of the window in samples
            
        Returns:
            numpy.ndarray: Window of data
        """
        # TODO: Implement window extraction
        # - Extract window of data
        # - Handle end of data case
        pass 