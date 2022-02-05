import pyttsx3
import queue
import threading
import random
import time

q = queue.Queue()

with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read()


engine = pyttsx3.init()


phrases = []

def on_start(name):
    print('on_start', name)


def on_word(name, location, length):
    print('on_word', name, location, length)


def on_end(name, completed):
    print('on_end', name, completed)
    check_queue()


engine.connect('started-utterance', on_start)
engine.connect('started-word', on_word)
engine.connect('finished-utterance', on_end)


def check_queue():
    print('adasdas')
    engine.say(q.get_nowait())
    engine.iterate()



def external_loop():

    engine.startLoop(True)

def put_queue():
    while True:
        if (q.qsize() < 3):
            q.put(random.choice(phrases))
        time.sleep(2)

#external_loop_thread = threading.Thread(target=external_loop)
put_queue_thread = threading.Thread(target=put_queue)

def init():
    words = text.split(' ')
    phrase = ''
    n = 0
    for i in words:
        n += 1
        phrase += i + ' '
        if n == 6:
            phrases.append(phrase)
            n = 0
            phrase = ''


if __name__ == '__main__':
    init()
    put_queue_thread.start()
    engine.say(random.choice(phrases))
    external_loop()

"""

итак, что у нас есть, мои слова, на мои слова должен быть и ответ и для начала, я сделаю тектовый ответ на мои слова

"""