import numpy
from scipy.fftpack import fft
from scipy.io import wavfile

def FFT(f):
	fs, data = wavfile.read(f)
	ch1 = data.T[0] # this is a two channel soundtrack, get the first track
	b=[(ele/2**8.)*2-1 for ele in ch1] # this is 8-bit track, b is now normalized on [-1,1)
	res = fft(b) # calculate fourier transform (complex numbers list)
	fftlen = len(res)/2  
	print numpy.where(res==max(res))
	return abs(res[:(fftlen-1)])

