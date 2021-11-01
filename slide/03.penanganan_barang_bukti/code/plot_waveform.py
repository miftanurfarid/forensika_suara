#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 09:03:15 2021

@author: mifta nur farid

Plot waveform dari file wav
"""

import librosa
import librosa.display
import matplotlib.pyplot as plt

filename = 'fena_0001.wav'

y, sr = librosa.load(filename)

fig, ax = plt.subplots(nrows=1, sharex=True)

librosa.display.waveshow(y, sr)