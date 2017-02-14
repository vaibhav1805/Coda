from pydub import AudioSegment

def mp3Towav(src):
	dest = "./gen/file.wav"
	AudioSegment.from_mp3(src).export(dest, format="wav")
	return dest