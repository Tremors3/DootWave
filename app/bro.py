# https://docs.python.org/3/library/wave.html
# https://www.youtube.com/watch?v=aOv9c60KrJQ

import wave
import numpy as np
import sys
import matplotlib.pyplot as plt

FILE_NAME = "suoni_antichi.wav"
wav = wave.open(f"audio/{FILE_NAME}", mode='rb')

framerate = wav.getframerate()
frames_num = wav.getnframes()
lenght = frames_num/float(framerate) # Lunghezza video
duration = 1/framerate # Passo video

print("File name: ", FILE_NAME)
print("Number of channels: ", wav.getnchannels())
print("Framerate ", framerate)
print("Frames Number: ", frames_num)
print("Video lenght: ", round(lenght, 2), "s")

data = wav.readframes(frames_num) # Prende i dati da tutti i canali
print(data)
w_data = np.frombuffer(data, np.int16) # Converte l'esadecimale in intero
w_data.shape = frames_num, 2 # Divide i dati dai 2 canali
w_data = w_data.T

t_seq = np.arange(0, lenght, duration)
#w_data.flags.writable = True
#w_data.setflags(write=True)
#print("\n\n\n",w_data.flags, type(w_data.flags),  "\n\n\n")

# lista = []
# for number in w_data[0]:
#     lista.append(number)

# for i in range(100, 1000):
#     lista[i] = 10000+i if i%2 == 0 else -10000-i

# plt.plot(t_seq, lista)
# plt.show()


