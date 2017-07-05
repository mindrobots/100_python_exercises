# generate a text file with all letters of the alphabet
# one letter per lin
# points 2

from string import ascii_lowercase

with open('alphabet.txt','w') as f:
    for l in ascii_lowercase:
        f.write(l = '\n')
