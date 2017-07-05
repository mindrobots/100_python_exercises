# mental exercise
# points 2
# script returns 2 because it has a loval variable c which you return from inside the function
'''
c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())
'''