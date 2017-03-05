from midiutil.MidiFile import MIDIFile
import notemap as nm
import progressions as pg
import math

def initMIDI(track=0, channel=0, time=0, duration=0, tempo=60, volume=100):
	codaMIDI = MIDIFile(1)
	codaMIDI.addTempo(track, time, tempo)
	return codaMIDI

def midiToPitch(p):
	pitch = pow(2.0, ((p-69))/12.0)*440
	return round(pitch, 1)

def noteToMidi(p, octave):
	p = nm.getNoteFreq(p, octave)
	midi = (math.log(float(p/440), 2)*12) + 69
	return int(round(midi))



degrees  = [60, 62, 64, 65, 67, 69, 71, 72] # MIDI note number
track    = 0
channel  = 0
time     = 0   # In beats
duration = 1   # In beats
tempo    = 60  # In BPM
volume   = 100 # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1) # One track, defaults to format 1 (tempo track
                     # automatically created)
MyMIDI.addTempo(track,time, tempo)

# for pitch in degrees:
#     MyMIDI.addNote(track, channel, pitch, time, duration, volume)
#     time = time + 1

def playScale(root, octave, mood):
	midi = noteToMidi(root, octave)
	t = time
	for i in pg.scales[mood]:
		MyMIDI.addNote(track, channel, midi+i, t, duration, volume)
		t = t +1

def playChord(root, octave, mood):
	midi = noteToMidi(root, octave)
	t = time
	for i in pg.types[mood]:
		MyMIDI.addNote(track, channel, midi+i, t, duration, volume)
	t=t+1

#playChord("A", 2, "min")
# with open("major-scale.mid", "wb") as output_file:
#     MyMIDI.writeFile(output_file)
