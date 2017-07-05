# generate a file where all letters of alphabet are listed three to a line:
# abc
# def
# ghi
# points 3

from string import ascii_lowercase

# GOTCHA add a blank on the end so letters id evenly disible by 3
letters = ascii_lowercase + ' '

letters1 = letters[::3]
letters2 = letters[1::3]
letters3 = letters[2::3]
with open('letter_pairs2.txt','w') as f:
    for a, b, c in zip(letters1, letters2, letters3):
        s = a+b+c+'\n'
        f.write(s)
 