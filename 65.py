# change program below so it prints out Hello repeatedly and never 'Hi'
# points 2
'''
while True:
    print('Hello')
    if 2 > 1:
        break
    print('Hi')
'''
while True:
    print('Hello')
    if 2 > 1:
        continue        # was a break
    print('Hi')