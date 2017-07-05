# create dictionary 
# points 2
# {'a':[1...10],
#  'b':[11...20],
#  'c':[21...30]}
# then access 3rd value of key b
from pprint import pprint

d = {'a':list(range(1,11)),
    'b':list(range(11,21)),
    'c':list(range(21,31))}
print(d['b'][2])