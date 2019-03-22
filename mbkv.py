import pyaudio
import numpy as np
import os

# Number of data points to read at a time
CHUNK = 2**11

# Time seolution of the recording device (Hz)
RATE = 44100

# Start the PyAudio class
p=pyaudio.PyAudio()

# Uses the default input device
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)


while True:
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(np.abs(data))*2
    
    v = int(50*peak/2**16)

    # Just printing the value of v so that I can make this script
    # more accurate. 
    print(v)
    
    if v == 0:
        os.system("kbdlight set 0")
    
    elif v < 8 and v > 0:
        os.system("kbdlight set 127")

    else:
        os.system("kbdlight max")

stream.stop_stream()
stream.close()
p.terminate()
