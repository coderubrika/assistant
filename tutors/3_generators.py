from time import time

def gen1(s):
    for i in s:
        yield i

def gen2(n):
    for i in range(n):
        yield i

def gen_filename():
    while True:
        pattern = 'file-{}.jpg'
        t = int(time() * 1000)
        yield pattern.format(str(t))

tasks = [gen1("adasd"), gen2(4)]

while tasks:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass