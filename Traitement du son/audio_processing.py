import wave
import binascii
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from playsound import playsound
from math import pi, sin
from copy import deepcopy
import numpy as np
from scipy.fft import rfft, rfftfreq

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

def echo(wav, output_name, delay):
    """
    Adds an echo effect to a WAV file.
    
    Inputs:
        wav : path to a WAV audio file.
        output_name : name of the output WAV file.
        delay : delay for the echo effect, typically around 1000.
    Output:
        Plays the original sound with an echo.
    """
    file_name = wav
    audio = wave.open(file_name, 'r')
    Y1 = [int(binascii.hexlify(audio.readframes(1)), 16) for _ in range(audio.getnframes())]  # audio data
    Y2 = deepcopy(Y1)  # create a copy for delayed version
    for _ in range(delay):
        Y2.insert(0, 0)  # shift the data in Y2 by inserting zeros at the start
    Y3 = []
    for k in range(len(Y2)):
        if k < len(Y1):  # ensure Y1[k] is defined
            Y3.append(Y1[k] + Y2[k])  # sum the two lists
        else:
            Y3.append(Y2[k])  # only add Y2[k] if Y1[k] is not available
    fe = audio.getframerate()  # sampling frequency
    # create the output WAV file
    data = Y3
    scaled = np.int16(data / np.max(np.abs(data)) * (2**15 - 1))
    write(output_name, fe, scaled)
    #return playsound(output_name)

def FFT(X, Y, SR, dur):
    """
    Computes and displays the Fast Fourier Transform (FFT) of the signal.
    
    Inputs:
        X : list of sampling instants.
        Y : signal data.
        SR : sampling rate (Hz).
        dur : duration of the sound (s).
    Output:
        A plot of the FFT of the signal.
    """
    Y2 = np.int16((Y / Y.max()) * 32767)
    yf = rfft(Y2)
    xf = rfftfreq(dur * SR, 1 / SR)
    plt.plot(xf, np.abs(yf))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude of the Component')
    plt.title('Fast Fourier Transform of the Signal')
    return plt.show()

def create_sine_wave(N, SR, dur, output_name):
    """
    Creates a sine wave based on user input for its components and saves it as a WAV file.
    
    Inputs:
        N : number of components (sine waves).
        SR : sampling rate (Hz).
        dur : duration of the sound (s).
        output_name : name of the output WAV file.
    Output:
        The generated sine wave is saved as a WAV file, and it is played.
    """
    t = np.linspace(0, dur, int(dur * SR))  # sampling instants
    y = 0 * t  # initialize with zero
    for _ in range(N):
        f = float(input('Frequency of the component: '))
        A = float(input('Amplitude of the component: '))
        omega = 2 * pi * f  # angular frequency
        y += A * np.sin(omega * t)
    # create the output WAV file
    data = y
    scaled = np.int16(data / np.max(np.abs(data)) * 32767)
    write(output_name, SR, scaled)
    #playsound(output_name)
    return t, y

def filtering(N, SR, dur, input_name, output_name, K, tau):
    """
    Applies a filter on a sine wave signal based on a transfer function.
    
    Inputs:
        N : number of components (sine waves).
        SR : sampling rate (Hz).
        dur : duration of the sound (s).
        input_name : name of the pre-filtered WAV file.
        output_name : name of the post-filtered WAV file.
        K : gain of the transfer function.
        tau : time constant of the transfer function.
    Output:
        Plays the filtered sound and saves it as a new WAV file.
    """
    X, Y = create_sine_wave(N, SR, dur, input_name)  # get the input sine wave signal
    Y2 = deepcopy(Y)  # create a copy of the signal for the output
    T = 1 / SR  # time step
    for k in range(1, len(Y)):
        Y2[k] = 1 / ((1 + 2 * tau / T) * (K * Y[k] + K * Y[k - 1] + (2 * tau / T - 1) * Y2[k - 1]))  # filtering equation
    # create the output WAV file
    data = Y2
    scaled = np.int16(data / np.max(np.abs(data)) * 32767)
    write(output_name, SR, scaled)
    #playsound(output_name)
    return X, Y2

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
    #return playsound(output_name)

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
    #return playsound(output_name)
