# print 'hello' immed, 1 sec, 2 sec, 3 sec then stop
# points 3
from time import sleep

delay = 0

while True:
    sleep(delay)
    print('Hello')
    if delay == 3:
        break
    delay += 1
print('End of loop')