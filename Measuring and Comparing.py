import pyaudio, wave, numpy as np, matplotlib.pyplot as plt
import speech_recognition as sr

RATE = 16000
CHUNK = 1024

def record():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE,
                    input=True, frames_per_buffer=CHUNK)
    print("Recording...... Press Enter to stop")
    frames = []
    input_thread = input
    import threading

    stop = False

    def wait():
        nonlocal stop
        input()
        stop = True
        input()
        stop = True

    threading.Thread(target=wait).start()

    while not stop:
        frames.append(stream.read(CHUNK))

    stream.stop_stream()
    stream.close()
    p.terminate()

    return b''.join(frames)

def save(data, filename="recording.wav"):
    with wave.open(filename, 'wb') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(RATE)
        f.setframerate(RATE)
        f.writeframes(data)
    print("Saved:", filename)

def transcribe(data):
    r = sr.Recognizer()
    try:
        text = r.recognize_google(sr.AudioData(data, RATE, 2))
        print(text)
    except:
        print("Could not transcribe")

def plot(data):
    samples = np.frombuffer(data, dtype=np.int16)
    plt.plot(samples)
    plt.title("waveform")
    plt.show()
audio = record()
save(audio)
transcribe(audio)
plot(audio)