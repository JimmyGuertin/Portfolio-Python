from audio_processing import *
from utilities import *

def main():
    # Parameters for audio file and effects
    audio_file = 'caramba.wav'  # Path to the input audio file
    echo_file = 'echo.wav'  # Path to save the audio with echo effect
    sine_wave_file = 'sine_wave.wav'  # Path to save the generated sine wave audio
    filtered_file = 'filtered_signal.wav'  # Path to save the filtered signal audio
    speed_changed_file = 'speed_changed.wav'  # Path to save the speed-changed audio
    volume_changed_file = 'volume_changed.wav'  # Path to save the volume-changed audio
    
    # Echo parameters
    echo_delay = 1000  # Delay for the echo effect
    
    # Filtering parameters
    num_components = 2  # Number of components for sine wave
    sampling_rate = 44100  # Sampling rate (Hz)
    duration = 2  # Duration of the sine wave (seconds)
    filter_cutoff = 1 / (2 * pi * 1000)  # Filter cutoff frequency
    
    # Volume change parameter
    volume_coefficient = 0.5  # Coefficient for changing volume (0.5 for reduction, 2 for increase)

    # Example usage of the functions
    print("1. Temporal Characteristic")
    temporal_characteristic(audio_file)  # Visualize the temporal characteristic of the audio file

    print("2. Echo Effect")
    echo(audio_file, echo_file, echo_delay)  # Apply echo effect to the audio file

    print("3. FFT of Audio")
    X, Y = create_sine_wave(num_components, sampling_rate, duration, sine_wave_file)  # Generate a sine wave audio file
    FFT(X, Y, sampling_rate, duration)  # Visualize the FFT of the generated sine wave

    print("4. Filtering the Signal")
    filtering(num_components, sampling_rate, duration, sine_wave_file, filtered_file, 1, filter_cutoff)  # Apply filter to the signal

    print("5. Change Speed")
    change_speed(audio_file, 5000, speed_changed_file)  # Change the speed of the audio

    print("6. Change Volume")
    change_volume(audio_file, volume_changed_file, volume_coefficient)  # Change the volume of the audio

    print("Created and modified files have been saved in the folder.")

if __name__ == "__main__":
    main()

