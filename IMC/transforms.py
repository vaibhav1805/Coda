import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.fftpack import fft
import numpy
from pylab import *
import stft

def FFT(f):
	fs, data = wavfile.read(f)
	print data.dtype
	ch1 = data.T[0] # this is a two channel soundtrack, get the first track
	b=[(ele/2**8.)*2-1 for ele in ch1] # this is 8-bit track, b is now normalized on [-1,1)
	res = fft(b) # calculate fourier transform (complex numbers list)
	fftlen = len(res)/2  
	print numpy.where(res==max(res))
	return abs(res[:(fftlen-1)])

def FFT2(f):
	freq, snd = wavfile.read(f)
	snd = snd / (2.**15)
	sh = snd.shape
	dur = sh[0]/freq
	s1 = snd[:,0]
	timeArray = arange(0, sh[0], 1)
	timeArray = timeArray / freq
	timeArray = timeArray * 1000  #scale to milliseconds
	plot(timeArray, s1, color='k')
	ylabel('Amplitude')
	xlabel('Time (ms)')
	n = len(s1) 
	p = fft(s1) # take the fourier transform 
	nUniquePts = int(ceil((n+1)/2.0))
	p = p[0:nUniquePts]
	p = abs(p)
	p = p / float(n)
	p = p**2
	if n % 2 > 0:
		p[1:len(p)] = p[1:len(p)] * 2
	else:
		p[1:len(p) -1] = p[1:len(p) - 1] * 2 
	freqArray = arange(0, nUniquePts, 1.0) * (freq / n);
	plot(freqArray/1000, 10*log10(p), color='k')
	print freqArray[numpy.where(p==max(p))[0][0]]
	xlabel('Frequency (kHz)')
	ylabel('Power (dB)')
	show()

def STFT(f):
	fs, audio = wavfile.read(f)
	specgram = stft.spectrogram(audio)
	output = stft.ispectrogram(specgram)
	print output


def promFreq(f):
	res = FFT(f)
	l = list(res)
	print max(l)
	return  l.index(max(l))
