import sys

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
types= {
	"maj": [0, 4, 7],
	"min": [0, 3, 7]
}

scales={
	"maj": [0, 2, 4, 5, 7, 9, 11, 12],
	"min": [0, 2, 3, 5, 7, 8, 10, 12]
}


def getChordSeq(chord, ctype):
	nts =[]
	seq = types[ctype]
	for i in seq:
		nts.append(notes[(notes.index(chord)+i)%12])
	return nts

def getScale(root, ctype):
	nts =[]
	seq = scales[ctype]
	for i in seq:
		nts.append(notes[(notes.index(root)+i)%12])
	return nts
