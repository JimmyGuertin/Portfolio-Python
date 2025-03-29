Sound Processing Project 🎵
This project allows you to analyze and modify .wav audio files.
It includes functions to:

Visualize the waveform and frequency spectrum (FFT)

Modify volume, speed, and apply an echo effect

Play the original and modified versions of the sound

📌 Installation
Install dependencies:

bash
Copier
Modifier
pip install numpy scipy matplotlib playsound
📝 Usage
To run the program, start by launching the main.py script. You will be prompted to choose between two audio files (e.g., "trumpet.wav" or "caramba.wav").

Here’s how it works:

Choosing the File:

At the beginning of the main() function, you will be asked to select an audio file (trumpet.wav or caramba.wav).

Setting Parameters:

You can then specify parameters to create a new sound, such as frequency and number of components (sine waves).

This allows you to generate a sound with custom frequencies and amplitudes based on your input.

File Creation:

After entering the desired parameters, the new sound is created and saved in a folder.

Listening to the Sound:

Once the new file is created, you will have to open manually the audio filesto listen to them.
