import tkinter as tk
from tkinter import ttk
import sounddevice as sd
from scipy.io import wavfile
from PIL import Image, ImageTk
import numpy as np
from numpy import random

Fs = 44100 # sampling frequency

def create_sine():
   freq_hz = 440.0 # Frequency / pitch
   duration_s = 1.0 # Duration
   atten = 0.3 # Attenuation so the sound is reasonable

   # Create sinusoidal signal
   each_sample_number = np.arange(duration_s * Fs)
   waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / Fs)
   return waveform * atten

#data = create_sine()

Fs, r_data_1 = wavfile.read('r_data_1.wav')
Fs, r_data_2 = wavfile.read('r_data_2.wav')
Fs, r_data_3 = wavfile.read('r_data_3.wav')
Fs, r_data_4 = wavfile.read('r_data_4.wav')

Fs, l_data_1 = wavfile.read('l_data_1.wav')
Fs, l_data_2 = wavfile.read('l_data_2.wav')
Fs, l_data_3 = wavfile.read('l_data_3.wav')
Fs, l_data_4 = wavfile.read('l_data_4.wav')

right_sounds = [r_data_1, r_data_2, r_data_3, r_data_4]
left_sounds = [l_data_1, l_data_2, l_data_3, l_data_4]

bytespersample = 4
maxampl = 2**( bytespersample * 8 - 1) - 1

def normalize(data):
   return data / maxampl

for n, data in enumerate(right_sounds):
   right_sounds[n] = normalize(data)

for n, data in enumerate(left_sounds):
   left_sounds[n] = normalize(data)
 
win = tk.Tk() # Create an instance of tkinter frame or window
win.resizable(False, False) #Make window not resizable
win.geometry("500x500") # Set the size of the window
bg = ImageTk.PhotoImage(file="AI_generated.png") # Add a background image
label = tk.Label(win, image=bg)
label.place(x=0, y=0)

globalvar = {'side': 'left'}

# Define a function to play the music
def play_sound():
   if globalvar['side'] == 'left':
      left_sounds_length = len(left_sounds)
      n = random.randint(left_sounds_length)
      random_sound = left_sounds[n]
      globalvar['side'] = 'right'
   else:
      right_sounds_length = len(right_sounds)
      n = random.randint(right_sounds_length)
      random_sound = right_sounds[n]
      globalvar['side'] = 'left'

   att = v2.get() / 100
   sd.play(att * random_sound, Fs)

# Add a Button widget
b1 = tk.Button(win, text="Play",
 command=play_sound,
 bg="green",
 fg="white")
b1.pack(pady=60)

# Add a slider widget
v2 = tk.DoubleVar()
    
s2 = tk.Scale( win, variable = v2,
   from_ = 100, to = 0,
   orient = tk.VERTICAL,
   bg="green",
   fg="white") 
  
s2.pack(anchor = tk.CENTER) 


win.mainloop()
