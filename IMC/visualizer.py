import sys
from pylab import *
import wave

from pydub import AudioSegment
sound = AudioSegment.from_mp3("203458__tesabob2001__a3.mp3")
sound.export("gen", format="wav")

def show_wave_n_spec(speech):
    spf = wave.open(speech,'r')
    sound_info = spf.readframes(-1)
    sound_info = fromstring(sound_info, 'Int16')
    f = spf.getframerate()
    
    subplot(211)
    plot(sound_info)
    title('Wave from and spectrogram of %s' % sys.argv[1])

    subplot(212)
    spectrogram = specgram(sound_info, Fs = f, scale_by_freq=True,sides='default')
    
    show()
    spf.close()

fil = sys.argv[1]
#show_wave_n_spec(fil)

