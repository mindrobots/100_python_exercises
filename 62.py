# print 'hello' at increasing second intervals, forever
# points 2
from time import sleep

delay = 0

while True:
    sleep(delay)
    print('Hello')
    delay += 1