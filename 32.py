# mental exercise
# points 2
# script returns 3 because you change global variable c to 3 before you execute foo
'''
c = 1
def foo():
    return c
c = 3
print(foo())
'''
