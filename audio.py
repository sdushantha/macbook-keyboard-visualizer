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


# Need to read the blog post about the audio recording with python and then I have to try
# to try to understand the the algorithm on how line 15 to 18 works. It would also be inice if you could try to make
# sensor a littl emore sensitive to the mic so that the the lights change more frquently and with more light difference :)
while True:
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(np.abs(data))*2
    #print(peak)
    v = int(50*peak/2**16)

    print(v)
    
    if v == 0:
        os.system("kbdlight set 0")
    elif v < 8 and v > 0:
        os.system("kbdlight set 127")

    else:
        os.system("kbdlight max")
    #print("%04d %05d %s"%(i,peak,bars))

stream.stop_stream()
stream.close()
p.terminate()
