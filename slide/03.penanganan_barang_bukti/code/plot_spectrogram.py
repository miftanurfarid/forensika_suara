#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 09:03:34 2021

@author: mifta nur farid
"""
import librosa
import numpy as np
import matplotlib.pyplot as plt

filename = 'fena_0001.wav'

y, sr = librosa.load(filename)

fig, ax = plt.subplots(nrows=1, ncols=1, sharex=True)

D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

img = librosa.display.specshow(D, y_axis='linear', x_axis='time',

                               sr=sr)

ax.set(title='Linear-frequency power spectrogram')

ax.label_outer()