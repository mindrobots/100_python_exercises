# generate 26 text files named a.txt, b.txt, etc.
# each file should contain the letter it is named for
# a.txt contains a, etc.
# points 3

from string import ascii_lowercase

# nice touch from instructor - create directory for files

import os
if not os.path.exists("letters"):
    os.makedirs("letters")


for letter in ascii_lowercase:
    filename = letter + '.txt'
    with open("letters/" + filename, 'w') as f:
        f.write(letter + '\n')
