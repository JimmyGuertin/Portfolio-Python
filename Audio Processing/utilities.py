import binascii
import wave
import numpy as np
from scipy.io.wavfile import write
from playsound import playsound
import matplotlib.pyplot as plt

def temporal_characteristic(wav: str) -> None:
    """
    Displays the temporal characteristic of a WAV audio file.
    
    Input:
        wav : path to a WAV audio file.
    Output:
        Plots amplitude over time.
    """
    audio = wave.open(wav, 'r')  # open audio file
    fe = audio.getframerate()     # sampling frequency
    N = audio.getnframes()        # number of samples
    X = np.linspace(0, 1 / fe * N, N)
    # read amplitudes from the audio file
    Y = [int(binascii.hexlify(audio.readframes(1)), 16) for _ in range(N)]
    plt.plot(X, Y)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Temporal Characteristic of the Audio Signal')
    plt.show()

def change_speed(wav: str, new_SR: int, output_name: str) -> None:
    """
    Changes playback speed by altering the sampling rate of a WAV file.
    
    Inputs:
        wav : path to the WAV audio file.
        new_SR : new sampling rate.
        output_name : name of the output WAV file.
    """
    audio = wave.open(wav, 'r')
    Y = [int(binascii.hexlify(audio.readframes(1)), 16) for _ in range(audio.getnframes())]
    # normalize and save with new sampling rate
    scaled = np.int16(np.array(Y) / np.max(np.abs(Y)) * (2**15 - 1))
    write(output_name, new_SR, scaled)
    playsound(output_name)

def change_volume(wav: str, output_name: str, coeff: float) -> None:
    """
    Modifies the volume of a WAV file by scaling amplitude.
    
    Inputs:
        wav : path to the WAV audio file.
        output_name : name of the output WAV file.
        coeff : volume scaling factor.
    """
    audio = wave.open(wav, 'r')
    Y = [int(binascii.hexlify(audio.readframes(1)), 16) for _ in range(audio.getnframes())]
    fe = audio.getframerate()
    # normalize, scale, and save
    scaled = np.int16(np.array(Y) / np.max(np.abs(Y)) * (2**15 - 1) * coeff)
    write(output_name, fe, scaled)
    playsound(output_name)
