def record_audio(duration, samplerate, file):
    print(f"Recording for {duration} seconds...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait() 
    print("Recording ")
    wavio.write(file, recording, samplerate, sampwidth=2)
    print(f"Saved to ")

if __name__ == "__main__":
    duration = 10 
    samplerate = 44100 
    file = "recorded and audio" 

    record_audio(duration, samplerate, file)
