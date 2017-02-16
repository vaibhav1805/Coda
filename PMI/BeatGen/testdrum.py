from music21 import stream, instrument
from music21.note import Note

n = Note("A2", type='quarter')

drumPart = stream.Part()
drumPart.insert(0, instrument.Woodblock())

drumMeasure = stream.Measure()
drumMeasure.append(n)
drumPart.append(drumMeasure)

drumPart.show('midi')
