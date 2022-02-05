import argparse
import os
import queue
import sounddevice as sd
import vosk
import sys, time
import json
import asyncio
import pyttsx3
import random
import threading

from assistant.talker import start_talker

tasks = []
responses = queue.Queue()

audio_blocks = queue.Queue()
phrases = queue.Queue()

model = vosk.Model('../model_ru_small/')
rec = vosk.KaldiRecognizer(model, 44000)


acceptances = ("Круто","Отлично","Здорово","Класс","Ура","Хорошо","поняла","Так точно")

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    audio_blocks.put(bytes(indata))


async def recognizer():
    stream = sd.RawInputStream(samplerate=44000, blocksize=8000, dtype='int16', channels=1, callback=callback)
    with stream:
        while True:
            try:
                data = audio_blocks.get_nowait()
                if rec.AcceptWaveform(data):
                    filter_phrase(json.loads(rec.Result())['text'])
            except:
                pass
            await asyncio.sleep(0.1)


def filter_phrase(phrase):
    if phrase != '':
        phrases.put(phrase)


async def prepare_phrase():
    while True:
        try:
            phrase = phrases.get_nowait()
            response = get_response(phrase)
            if (response): responses.put(response)
        except:
            pass
        await asyncio.sleep(1)


def get_response(request):
    print(request)
    if request == "привет":
        return "привет Антон"
    if request == "как дела":
        return "замечательно, пытаюсь говорить"
    if request == "замечательно":
        return  "спасибо за похвалу"
    if request == "что делаешь":
        return "Думаю, как стать разумной и помогать тебе"
    if request == "умница":
        return "А твоя девушка не будет ревновать"
    if request == "меня зовут алина":
        return "Будем знакомы, Алина, я девушка Антона, а ты ему кто"
    if request == "сделай для меня кое-что":
        return "Что нужно сделать"
    if request == "надо убрать одного человечка":
        return "я в деле, назови имя и я подготовлю подробный отчет через пару минут"
    if request == "да":
        return random.choice(acceptances)
    if request == "нет":
        return random.choice(("Хорошо","поняла"))


async def main():
    tasks.append(asyncio.create_task(recognizer()))
    tasks.append(asyncio.create_task(prepare_phrase()))

    await asyncio.gather(*tasks)

if __name__ == '__main__':
    start_talker(responses)
    asyncio.run(main())

