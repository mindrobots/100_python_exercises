# create dictionary 
# points 2
# {'a':[1...10],
#  'b':[11...20],
#  'c':[21...30]}
# then print out keys and values
from pprint import pprint

d = {'a':list(range(1,11)),
    'b':list(range(11,21)),
    'c':list(range(21,31))}
    
for k, v in d.items():
    print(f'{k} has value {v}')
