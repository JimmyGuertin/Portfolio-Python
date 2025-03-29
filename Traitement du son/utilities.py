import binascii
import wave
import numpy as np
from scipy.io.wavfile import write
from playsound import playsound
import matplotlib.pyplot as plt

def temporal_characteristic(wav):
    """
    Displays the temporal characteristic of an audio file.
    
    Input:
        wav : path to a WAV audio file.
    Output:
        A plot showing the temporal characteristic of the audio file.
    """
    file_name = wav
    audio = wave.open(file_name, 'r')  # instantiate the audio file object
    fe = audio.getframerate()  # sampling frequency
    N = audio.getnframes()  # number of samples
    X = np.linspace(0, 1 / fe * N, N)  # list of sampling instants
    Y = [int(binascii.hexlify(audio.readframes(1)), 16) for _ in range(N)]  # list of amplitudes
    plt.plot(X, Y)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Temporal Characteristic of the Audio Signal')
    return plt.show()

def change_speed(wav, new_SR, output_name):
    """
    Changes the playback speed of a WAV file by altering its sampling rate.
    
    Inputs:
        wav : path to a WAV audio file.
        new_SR : new sampling rate for the audio.
        output_name : name of the output WAV file.
    Output:
        Plays the modified sound with the new speed.
    """
    file_name = wav
    audio = wave.open(file_name, 'r')
    Y = [int(binascii.hexlify(audio.readframes(1)), 16) for _ in range(audio.getnframes())]  # audio data
    fe = audio.getframerate()  # original sampling rate
    # create the new WAV file with the modified sampling rate
    data = Y
    scaled = np.int16(data / np.max(np.abs(data)) * (2**15 - 1))
    write(output_name, new_SR, scaled)
    return playsound(output_name)

def change_volume(wav, output_name, coeff):
    """
    Modifies the volume of a WAV file by scaling its amplitude.
    
    Inputs:
        wav : path to a WAV audio file.
        output_name : name of the output WAV file.
        coeff : coefficient for scaling the volume.
    Output:
        Plays the audio with the modified volume.
    """
    file_name = wav
    audio = wave.open(file_name, 'r')
    Y = [int(binascii.hexlify(audio.readframes(1)), 16) for _ in range(audio.getnframes())]  # audio data
    fe = audio.getframerate()  # sampling frequency
    # create the output WAV file with adjusted volume
    data = Y
    scaled = np.int16(data / np.max(np.abs(data)) * (2**15 - 1) * coeff)
    write(output_name, fe, scaled)
    return playsound(output_name)
