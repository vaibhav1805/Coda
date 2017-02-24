from music21 import stream, instrument
from music21.note import * 
import progressions as pr

def instr(note):
	instrumentPart = stream.Part()
	''' Instruments class may be changed as per requirements refer to music21/instrument.py'''
	instrumentPart.insert(0, instrument.Piano()) 
	instrumentMeasure = stream.Measure()
	instrumentMeasure.append(note)
	instrumentPart.append(instrumentMeasure)
	instrumentPart.show('midi')


def playNotes(note, measure):
	n = Note(note, type= measure)
	instr(n)