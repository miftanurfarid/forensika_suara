%%Time specifications:
Fs = 100;                      % samples per second
dt = 1/Fs;                     % seconds per sample
StopTime = 1;                  % seconds
t = (0:dt:StopTime-dt)';
N = size(t,1);
%%Sine wave:
Fc = 12;                       % hertz
x = cos(2*pi*Fc*t);
%%Fourier Transform:
[x, Fs] = audioread('fena_0001_cut.wav');
N = length(x)
%X = fftshift(fft(x));
X = fft(x);
%%Frequency specifications:
dF = Fs/N;                      % hertz
f = -Fs/2:dF:Fs/2-dF;           % hertz
%%Plot the spectrum:
figure(2);
plot(f,abs(X)/N);
xlim([0, 500])
xlabel('Frequency (in hertz)');
title('Magnitude Response');