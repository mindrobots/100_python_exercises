# take a text file as input and returns the # of words it contains
# split on ' ' or ','
# insterted .replace(',',' ') into the function chain from 36.py
# points 3

def words_in_file(file):
    with open(file, 'r') as f:
        return(len(f.read().replace(',',' ').split()))

print(words_in_file('./words2.txt'))