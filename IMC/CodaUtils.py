from pydub import AudioSegment

def mp3Towav(src, dest):
	AudioSegment.from_mp3(src).export(dest, format="wav")
	return dest

#Finds highest amplitude of any sample in the AudioSegment.
def maxAmpSegment(track):
	if ".mp3" in track:
		sound = AudioSegment.from_file(track, format="mp3")
	if ".wav" in track:
		sound = AudioSegment.from_file(track, format="wav")
	return sound.max

#Returns Returns the loudness of the AudioSegment in dBFS 
def dBFSegment(track):
	if ".mp3" in track:
		sound = AudioSegment.from_file(track, format="mp3")
	if ".wav" in track:
		sound = AudioSegment.from_file(track, format="wav")
	return sound.dBFS

