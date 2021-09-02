# Tugas 2 - Forensika Suara

[x, fs] = audioread('fena_0001_cut.wav');
X = fft(x);
plot(abs(X));