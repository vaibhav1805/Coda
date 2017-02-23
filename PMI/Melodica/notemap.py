import math
import sys
freqMap = {
 	"C": 16.35,
 	"C#": 17.32,
 	"D": 18.35,
 	"D#": 19.45,
 	"E": 20.60,
 	"F": 21.83,
 	"F#": 23.12,
 	"G": 24.50,
 	"G#": 25.96,
 	"A": 27.50,
 	"A#": 29.14,
 	"B": 30.87
 }

def getNoteFreq(note, octave):
	if note not in freqMap:
		return 0
	return (freqMap[note]) * pow(2.0, float(octave))

