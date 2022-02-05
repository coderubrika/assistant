import argparse
import os
import queue
import sounddevice
import vosk
import sys, json

q = queue.Queue()

import pyttsx3
engine = pyttsx3.init()

'''
def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

    device_info = sounddevice.query_devices(None, 'input')
    samplerate = int(device_info['default_samplerate'])

    # загружаем модель по хардкодному имени
    model = vosk.Model("model_ru_small")

    # считывание звука в очередь q
    sounddevice.RawInputStream(samplerate=samplerate, blocksize = 8000, device=None, dtype='int16', channels=1, callback=callback)
    print('#' * 80)
    print('Press Ctrl+C to stop the recording')
    print('#' * 80)

    rec = vosk.KaldiRecognizer(model, samplerate)
    while True:
        data = q.get()
        if not rec.AcceptWaveform(data):
            message = json.loads(rec.PartialResult())['partial']
            print(message)
            engine.say(message)
            engine.runAndWait()




'''