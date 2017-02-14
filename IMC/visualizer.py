import sys
from pylab import *
import wave
import CodaUtils as CD

def plot_waveform(track):
    track = CD.mp3Towav(track)
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

plot_waveform("../Samples/Piano/203458__tesabob2001__a3.mp3")

