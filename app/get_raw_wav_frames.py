# https://docs.python.org/3/library/wave.html
# https://www.youtube.com/watch?v=aOv9c60KrJQ

import wave
import sys
import numpy as np

file_name = "audio/music.wav" #sys.argv[0]
wav = wave.open(file_name, mode='rb')

framerate = wav.getframerate()
frames_num = wav.getnframes()
lenght = frames_num/float(framerate) # Lunghezza video
duration = 1/framerate # Passo video

print("File name: ", file_name)
print("Number of channels: ", wav.getnchannels())
print("Framerate ", framerate)
print("Frames Number: ", frames_num)
print("Video lenght: ", round(lenght, 2), "s")

data = wav.readframes(frames_num) # Prende i dati da tutti i canali

with open(file_name + "-raw", "w") as f:
    f.write(str(data))
    
wav.close()