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
from scipy.fftpack import fft,fftshift

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

"""
1. Plotting raw values of DFT:
"""
NFFT=1024 #NFFT-point DFT      
X=fft(x,NFFT) #compute DFT using FFT    

fig1, ax = plt.subplots(nrows=1, ncols=1) #create figure handle
nVals = np.arange(start = 0,stop = NFFT) # raw index for FFT plot
ax.plot(nVals,np.abs(X))      
ax.set_title('Fig 1. Double Sided FFT - without FFTShift')
ax.set_xlabel('Sample points (N-point DFT)')        
ax.set_ylabel('DFT Values')

"""
2. FFT plot – plotting raw values against normalized frequency axis:
"""
NFFT=1024 #NFFT-point DFT  
X=fft(x,NFFT) #compute DFT using FFT     

fig2, ax = plt.subplots(nrows=1, ncols=1) #create figure handle
   
nVals=np.arange(start = 0,stop = NFFT)/NFFT #Normalized DFT Sample points         
ax.plot(nVals,np.abs(X))     
ax.set_title('Fig 2. Double Sided FFT - without FFTShift')        
ax.set_xlabel('Normalized Frequency')
ax.set_ylabel('DFT Values')

"""
3. FFT plot – plotting raw values against normalized frequency
   (positive & negative frequencies):
"""
NFFT=1024 #NFFT-point DFT      
X=fftshift(fft(x,NFFT)) #compute DFT using FFT  

fig3, ax = plt.subplots(nrows=1, ncols=1) #create figure handle
    
fVals=np.arange(start = -NFFT/2,stop = NFFT/2)/NFFT #DFT Sample points        
ax.plot(fVals,np.abs(X))
ax.set_title('Fig 3. Double Sided FFT - with FFTShift')
ax.set_xlabel('Normalized Frequency')
ax.set_ylabel('DFT Values');
ax.autoscale(enable=True, axis='x', tight=True)
ax.set_xticks(np.arange(-0.5, 0.5+0.1,0.1))

"""
4. FFT plot – Absolute frequency on the x-axis vs. magnitude on y-axis:
"""
NFFT=1024     
X=fftshift(fft(x,NFFT))

fig4, ax = plt.subplots(nrows=1, ncols=1) #create figure handle

fVals=np.arange(start = -NFFT/2,stop = NFFT/2)*fs/NFFT
ax.plot(fVals,np.abs(X),'b')
ax.set_title('Fig 4. Double Sided FFT - with FFTShift')
ax.set_xlabel('Frequency (Hz)')         
ax.set_ylabel('|DFT Values|')
ax.set_xlim(-50,50)
ax.set_xticks(np.arange(-50, 50+10,10))

"""
5. FFT plot - From another ref.
"""
X = fftshift(fft(x))
N = len(x)
dF = fs/N
f = np.arange(-fs/2,fs/2,dF)
fig, ax = plt.subplots() #create figure handle
ax.plot(f, np.abs(X)/N)
ax.set_xlim(0, 100)
display(max(X))