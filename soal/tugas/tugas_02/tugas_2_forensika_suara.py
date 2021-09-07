import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftshift
import scipy.io.wavfile as wav
import math
import operator

filename = 'fena_0001_cut.wav'
fs, x = wav.read(filename)
#x = x[:,0]
x = (x - min(x)) / (max(x) - min(x)) * 2 - 1
x = x - np.mean(x)
t = np.arange(0, len(x)/fs, 1/fs)

# Plot waveform
plt.plot(t, x)
plt.xlabel('Waktu (detik')
plt.ylabel('Amplitudo')
plt.title('Waveform dari suara ' + filename)
plt.savefig('waveform.svg', format='svg', dpi=1200)

# Plot spectrum
nfft = 2 ** math.ceil(math.log(len(x),2))
X = fftshift(fft(x, nfft))
f = np.arange(-nfft/2, nfft/2) * fs / nfft
plt.plot(f, np.abs(X))
plt.title('Spektrum dari suara ' + filename)
plt.xlabel('Frekuensi (Hz)')
plt.ylabel('Amplitudo')
plt.xlim(0, 2000)
plt.savefig('spektrum.svg', format='svg', dpi=1200)
lowlim = int(len(X)/2)
uplim = int(len(X)/2)+200
index, value = max(enumerate(abs(X[lowlim:uplim])), key=operator.itemgetter(1))
f0 = f[lowlim+index]
print(f"Frekuensi dasar dari {filename} = {round(f0)} Hz")