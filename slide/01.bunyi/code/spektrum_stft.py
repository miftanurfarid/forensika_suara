#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 04:54:04 2021

@author: fafa
"""

from scipy import signal
import numpy as np
import matplotlib.pyplot as plt # library for plotting
import scipy.io.wavfile as wav

filename = 'a.wav'
fs, x = wav.read(filename)
x = x[:,0]
x = (x - min(x)) / (max(x) - min(x)) * 2 - 1
x = x - np.mean(x)
t = np.arange(0, len(x)/fs, 1/fs)

f, t, Zxx = signal.stft(x, fs, nperseg=1024)

plt.pcolormesh(t, f, np.abs(Zxx))

plt.title('STFT Magnitude')

plt.ylabel('Frequency [Hz]')

plt.xlabel('Time [sec]')

plt.show()