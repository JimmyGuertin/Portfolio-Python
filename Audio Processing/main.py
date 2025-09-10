from audio_processing import *
from utilities import *

def main():
    """
    Demonstrates audio processing functions: visualization, echo, FFT, filtering,
    speed change, and volume adjustment.
    """
    # Input and output files
    audio_file = 'caramba.wav'  
    echo_file = 'echo.wav'  
    sine_wave_file = 'sine_wave.wav'  
    filtered_file = 'filtered_signal.wav'  
    speed_changed_file = 'speed_changed.wav'  
    volume_changed_file = 'volume_changed.wav'  
    
    # Echo effect parameter
    echo_delay = 1000  
    
    # Sine wave and filtering parameters
    num_components = 2  
    sampling_rate = 44100  
    duration = 2  
    filter_cutoff = 1 / (2 * pi * 1000)  
    
    # Volume change
    volume_coefficient = 0.5  

    # 1. Temporal characteristic visualization
    print("1. Temporal Characteristic")
    temporal_characteristic(audio_file)

    # 2. Echo effect
    print("2. Echo Effect")
    echo(audio_file, echo_file, echo_delay)

    # 3. Generate sine wave and visualize FFT
    print("3. FFT of Audio")
    X, Y = create_sine_wave(num_components, sampling_rate, duration, sine_wave_file)
    FFT(X, Y, sampling_rate, duration)

    # 4. Filtering the sine wave
    print("4. Filtering the Signal")
    filtering(num_components, sampling_rate, duration, sine_wave_file, filtered_file, 1, filter_cutoff)

    # 5. Change playback speed
    print("5. Change Speed")
    change_speed(audio_file, 5000, speed_changed_file)

    # 6. Adjust volume
    print("6. Change Volume")
    change_volume(audio_file, volume_changed_file, volume_coefficient)

    print("Created and modified files have been saved in the folder.")

if __name__ == "__main__":
    main()
