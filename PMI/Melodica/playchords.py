from music21 import stream, instrument
from music21.chord import * 
import progressions as pr

def instr(chord):
	instrumentPart = stream.Part()
	instrumentPart.insert(0, instrument.Guitar())
	instrumentMeasure = stream.Measure()
	instrumentMeasure.append(chord)
	instrumentPart.append(instrumentMeasure)
	instrumentPart.show('midi')


def playChords(chord, ctype):
	prog = []
	prog = pr.getChordSeq(chord, ctype)
	c = Chord(prog)
	instr(c)