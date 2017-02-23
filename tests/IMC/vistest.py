import sys, os
sys.path.insert(0, os.path.abspath('../..'))
import IMC.visualizer as codav
import IMC.CodaUtils as cdutil
import IMC.transforms as tf

f = "../../Samples/Piano/203"+sys.argv[1]+"__tesabob2001__"+sys.argv[2]+".mp3"
dest = "../../IMC/gen/file.wav"
#dest = "440_sine.wav"
#codav.plot_waveform(f, dest)
cdutil.mp3Towav(f, dest)
#print cdutil.maxAmpSegment(f)
#print cdutil.dBFSegment(f)
print tf.promFreq(dest)
#codav.plotFFT(dest)
tf.FFT2(dest)