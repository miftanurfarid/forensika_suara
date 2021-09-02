#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 04:02:34 2021

@author: fafa

"""

"""
Simulate a sinusoidal signal with given sampling rate
"""

import numpy as np
import matplotlib.pyplot as plt # library for plotting
from signalgen import sine_wave # import the function

f = 10 #frequency = 10 Hz
overSampRate = 30 #oversammpling rate
fs = f*overSampRate #sampling frequency
phase = 1/3*np.pi #phase shift in radians
nCyl = 5 # desired number of cycles of the sine wave

(t,x) = sine_wave(f,overSampRate,phase,nCyl) #function call

plt.plot(t,x) # plot using pyplot library from matplotlib package
plt.title('Sine wave f='+str(f)+' Hz') # plot title
plt.xlabel('Time (s)') # x-axis label
plt.ylabel('Amplitude') # y-axis label
plt.show() # display the figure

"""
FFT plot – Absolute frequency on the x-axis vs. magnitude on y-axis:
"""

from scipy.fftpack import fft,fftshift

NFFT=1024     
X=fftshift(fft(x,NFFT))

fig4, ax = plt.subplots(nrows=1, ncols=1) #create figure handle

fVals=np.arange(start = -NFFT/2,stop = NFFT/2)*fs/NFFT
ax.plot(fVals,np.abs(X),'b')
ax.set_title('Double Sided FFT - with FFTShift')
ax.set_xlabel('Frequency (Hz)')         
ax.set_ylabel('|DFT Values|')
ax.set_xlim(-50,50)
ax.set_xticks(np.arange(-50, 50+10,10))
fig4.show()