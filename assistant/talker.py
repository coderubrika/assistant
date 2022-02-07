import pyttsx3
import queue
import threading
import random
import time

class Talker:
    def __call__(self):
        self.engine = pyttsx3.init()
        self.trhead_check_queue.start()

    def check_queue(self):
        while True:
            try:
                sentence = self.sentences.get_nowait()
                self.engine.startLoop(False)
                self.engine.iterate()
                self.engine.say(sentence)
                self.engine.endLoop()

            except Exception as e:
                print(e)
            print(self.sentences.qsize())
            time.sleep(1)

    def __init__(self):
        self.sentences = queue.Queue()
        self.trhead_check_queue = threading.Thread(target=self.check_queue)



def start_talker(queue):
    talking = Talker()
    talking.sentences = queue
    thread_talking = threading.Thread(target=talking)
    thread_talking.start()