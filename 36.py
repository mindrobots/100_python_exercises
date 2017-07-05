# take a text file as input and returns the # of words it contains
# points 2

def words_in_file(file):
    with open(file, 'r') as f:
        return(len(f.read().split()))

print(words_in_file('./words1.txt'))