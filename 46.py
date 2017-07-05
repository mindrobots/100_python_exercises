# extract the letters from the 26 text files and put the letters in a list
# points 2 - I saw the solution when the video started - total 3 points possible
# instructor solution does not sort list but glob does not guarantee any order

import glob

letters = []

file_list = glob.glob('letters/*.txt')

for filename in file_list:
    with open(filename,'r') as f:
        l = f.readline().strip()
        letters.append(l)
letters.sort()

print(letters)