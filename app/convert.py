from pydub import AudioSegment
sound = AudioSegment.from_mp3("audio/doot.mp3")
sound.export("audio/doot.wav", format="wav")




