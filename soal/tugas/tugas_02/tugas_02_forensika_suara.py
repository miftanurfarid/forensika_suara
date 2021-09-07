#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 04:42:34 2021

Tugas 2 Forensika Suara

@author: Mifta Nur Farid
"""

import numpy as np
import matplotlib.pyplot as plt # library untuk plotting
import scipy.io.wavfile as wav # library untuk baca file wav
from scipy.fftpack import fft,fftshift
from scipy.signal import resample

percobaan = 3

#filename = 'fena_0001_cut.wav' # nama file
filename = 'i.wav' # nama file
#fs = 16000
fs, x = wav.read(filename) # membaca file wav
if x.ndim >= 2: # cek mono atau stereo
    x = x[:,0]
x = (x - min(x)) / (max(x) - min(x)) * 2 - 1 # normalisasi ke dalam range -1 hingga 1
x = x - np.mean(x)
#x = resample(x,int(len(x)*fs/Fs))
t = np.arange(0,len(x)/fs,1/fs) # data waktu berdasarkan panjang data file wav
plt.plot(t,x) # plot menggunakan library pyplot dari matplotlib package
plt.title('Waveform dari '+ filename) # plot judul
plt.xlabel('Waktu (detik)') # label sumbu x
plt.ylabel('Amplitudo') # label sumbu y
plt.show() # menampilkan gambar hasil plot

if percobaan == 1:    
    NFFT=2048 #NFFT-point DFT      
    X=fft(x,NFFT) #compute DFT using FFT    
    
    fig1, ax = plt.subplots(nrows=1, ncols=1) #create figure handle
    nVals = np.arange(start = 0,stop = NFFT) # raw index for FFT plot
    ax.plot(nVals,np.abs(X))      
    ax.set_title('Double Sided FFT - without FFTShift')
    ax.set_xlabel('Sample points (N-point DFT)')        
    ax.set_ylabel('DFT Values')
    ax.set_xlim(0,100)
    fig1.show()
elif percobaan == 2:
    fft_out = fft(x)
    fig, ax = plt.subplots()
    ax.plot(x, np.abs(fft_out))
    ax.set_xlim(-0.25,0.25)
elif percobaan == 3:
    X = fftshift(fft(x))
    N = len(x)
    dF = fs/N
    f = np.arange(-fs/2,fs/2,dF)
    fig, ax = plt.subplots() #create figure handle
    ax.plot(f, np.abs(X)/N)
    ax.set_xlim(0, 100)