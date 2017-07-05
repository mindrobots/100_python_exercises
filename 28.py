# no code required - fix error in:
# points 2
'''
def foo(a, b):
    print(a + b)
 
x = foo(2, 3) * 10
'''
# foo returns an implicit None since there is no return in function
# this will cause an exception when script tries multiplying None * 10
# to fix, make foo return a value --> return A + b