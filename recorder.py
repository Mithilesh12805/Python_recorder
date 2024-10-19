#Simple Voice Recorder in terminal

import pyaudio
import wave
#this both libraries are helps to record and save audio 

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

frames = []

try:
    print("Recording... Press Ctrl+C to stop.")
    while True:
        data = stream.read(1024)
        frames.append(data)
        
except KeyboardInterrupt:
    print("Recording stopped.")
    pass

stream.stop_stream()
stream.close()
audio.terminate()

sound_file = wave.open("myrecording.wav", "wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframes(b''.join(frames))
sound_file.close()
print("Recording saved as 'myrecording.wav'")


#~~~commands~~~

#C:\Users\mithi\pyenv\Scripts\activate
#cd C:\Users\mithi\OneDrive\Desktop\Python_Programs
#python recorder.py
