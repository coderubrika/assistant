from inspect import getgeneratorstate

def average():
    count = 0
    sum = 0
    avr = None
    while True:
        try:
            x = yield avr
        except StopIteration:
            print('Done')
        else:
            sum += x
            count += 1
            avr = round(sum / count, 2)

g = average()
g.send(None)
print(g.send(43))
print(g.send(43))
print(g.send(43))
print(g.send(43))
print(g.send(43))


