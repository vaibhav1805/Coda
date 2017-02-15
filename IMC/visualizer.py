import sys
from pylab import *
import wave
import matplotlib.pyplot as plt
import CodaUtils as CD
import transforms as tf

#Plots a waveform for Audio File.
def plot_waveform(track, dest):
    track = CD.mp3Towav(track, dest)
    spf = wave.open(track,'r')
    sound_info = spf.readframes(-1)
    sound_info = fromstring(sound_info, 'Int16')
    f = spf.getframerate()
    
    subplot(211)
    plot(sound_info)
    title('Wave from and spectrogram of %s' % track)

    subplot(212)
    spectrogram = specgram(sound_info, Fs = f, scale_by_freq=True,sides='default')
    
    show()
    spf.close()

def plotFFT(track):
    res = tf.FFT(track)
    l  =list(res)
    print l.index(max(l))
    plt.plot(res, 'r')
    plt.show()


