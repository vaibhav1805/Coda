from music21.chord import * 
import progressions as pr

def playChords(chord, ctype):
	prog = []
	prog = pr.getChordSeq(chord, ctype)
	c = Chord(prog)
	c.show('midi')
