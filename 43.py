# generate a file where all letters of alphabet are listed two to a line:
# ab
# cd
# ef
# points 

from string import ascii_lowercase

evens = ascii_lowercase[::2]
odds = ascii_lowercase[1::2]
with open('letter_pairs.txt','w') as f:
    for a, b in zip(evens, odds):
        s = a+b+'\n'
        f.write(s)
 