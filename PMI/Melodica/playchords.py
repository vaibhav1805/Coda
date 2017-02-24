from music21.chord import * 
import progressions as pr

def playChords(chord, ctype):
	prog = []
	prog = pr.getChordSeq(chord, ctype)
	print prog
	print type(prog)
	c = Chord(prog)
	c.show('midi')

playChords('A','maj')
