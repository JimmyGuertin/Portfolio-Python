import wave
import binascii
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from playsound import playsound
from math import pi, sin
from copy import deepcopy
import numpy as np
from scipy.fft import rfft, rfftfreq

def temporal_characteristic(wav: str) -> None:
    """
    Displays the temporal characteristic of an audio file.
    
    Input:
        wav : path to a WAV audio file.
    Output:
        Plots the amplitude over time.
    """
    audio = wave.open(wav, 'r')
    fe = audio.getframerate()
    N = audio.getnframes()
    X = np.linspace(0, 1 / fe * N, N)
    Y = [int(binascii.hexlify(audio.readframes(1)), 16) for _ in range(N)]  # read amplitudes
    plt.plot(X, Y)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Temporal Characteristic of the Audio Signal')
    plt.show()

def echo(wav: str, output_name: str, delay: int) -> None:
    """
    Adds an echo effect to a WAV file.
    
    Inputs:
        wav : path to a WAV audio file.
        output_name : name of the output WAV file.
        delay : echo delay in samples.
    """
    audio = wave.open(wav, 'r')
    Y1 = [int(binascii.hexlify(audio.readframes(1)), 16) for _ in range(audio.getnframes())]
    Y2 = deepcopy(Y1)
    
    for _ in range(delay):
        Y2.insert(0, 0)  # shift for echo
    
    Y3 = [Y1[k] + Y2[k] if k < len(Y1) else Y2[k] for k in range(len(Y2))]  # combine signals
    fe = audio.getframerate()
    scaled = np.int16(np.array(Y3) / np.max(np.abs(Y3)) * (2**15 - 1))
    write(output_name, fe, scaled)

def FFT(X: np.ndarray, Y: np.ndarray, SR: int, dur: float) -> None:
    """
    Computes and displays the Fast Fourier Transform (FFT) of the signal.
    
    Inputs:
        X : sampling instants.
        Y : signal amplitudes.
        SR : sampling rate.
        dur : duration of the sound.
    """
    Y2 = np.int16((Y / Y.max()) * 32767)
    yf = rfft(Y2)
    xf = rfftfreq(dur * SR, 1 / SR)
    plt.plot(xf, np.abs(yf))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Fast Fourier Transform of the Signal')
    plt.show()

def create_sine_wave(N: int, SR: int, dur: float, output_name: str) -> tuple:
    """
    Generates a sine wave from user input and saves it as WAV.
    
    Outputs:
        t : sampling instants.
        y : generated waveform.
    """
    t = np.linspace(0, dur, int(dur * SR))
    y = np.zeros_like(t)
    
    for _ in range(N):
        f = float(input('Frequency of the component: '))
        A = float(input('Amplitude of the component: '))
        y += A * np.sin(2 * pi * f * t)
    
    scaled = np.int16(y / np.max(np.abs(y)) * 32767)
    write(output_name, SR, scaled)
    return t, y

def filtering(N: int, SR: int, dur: float, input_name: str, output_name: str, K: float, tau: float) -> tuple:
    """
    Filters a sine wave using a simple transfer function.
    
    Outputs:
        X : sampling instants.
        Y2 : filtered waveform.
    """
    X, Y = create_sine_wave(N, SR, dur, input_name)
    Y2 = deepcopy(Y)
    T = 1 / SR
    
    for k in range(1, len(Y)):
        Y2[k] = 1 / ((1 + 2 * tau / T) * (K * Y[k] + K * Y[k - 1] + (2 * tau / T - 1) * Y2[k - 1]))
    
    scaled = np.int16(Y2 / np.max(np.abs(Y2)) * 32767)
    write(output_name, SR, scaled)
    return X, Y2

def change_speed(wav: str, new_SR: int, output_name: str) -> None:
    """
    Alters playback speed by changing sampling rate.
    """
    audio = wave.open(wav, 'r')
    Y = [int(binascii.hexlify(audio.readframes(1)), 16) for _ in range(audio.getnframes())]
    scaled = np.int16(np.array(Y) / np.max(np.abs(Y)) * (2**15 - 1))
    write(output_name, new_SR, scaled)

def change_volume(wav: str, output_name: str, coeff: float) -> None:
    """
    Modifies volume by scaling amplitude.
    """
    audio = wave.open(wav, 'r')
    Y = [int(binascii.hexlify(audio.readframes(1)), 16) for _ in range(audio.getnframes())]
    fe = audio.getframerate()
    scaled = np.int16(np.array(Y) / np.max(np.abs(Y)) * (2**15 - 1) * coeff)
    write(output_name, fe, scaled)
