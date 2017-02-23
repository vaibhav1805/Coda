import sys

notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
types= {
	"maj": [0, 4, 7],
	"min": [0, 3, 7]
}


def getChodSeq(chord, type):
	nts =[]
	seq = types[type]
	for i in seq:
		nts.append(notes[(notes.index(chord)+i)%12])
	print nts

#getChodSeq(sys.argv[1], "min")