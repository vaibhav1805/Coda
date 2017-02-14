import sys, os
sys.path.insert(0, os.path.abspath('../..'))
import IMC.visualizer as codav
import IMC.CodaUtils as cdutil

f = "../../Samples/Piano/203458__tesabob2001__a3.mp3"
dest = "../../IMC/gen/file.wav"
codav.plot_waveform(f, dest)
print cdutil.maxAmpSegment(f)
print cdutil.dBFSegment(f)