# Print out in each line, the sum of matching items of the two sequences:
# a = [1, 2, 3]
# b = [4, 5, 6]
# should print 5, 7, 9 on separate lines
# points 2

a = [1, 2, 3]
b = [4, 5, 6]

for x, y in zip(a,b):
    print(x + y)
