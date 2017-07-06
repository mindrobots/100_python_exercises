# from this array:
a = [1, 2, 3]
# create this output:
'''
Item 1 has index 0
Item 2 has index 1
Item 3 has index 2
'''
# points 2

for i,v in enumerate(a):
    print('Item {1} has index {0}'.format(i,v))
