# in code below, the error is that foo - 1 is not a proper function call
'''
def foo(a=1, b=2):
    return a + b
 
x = foo - 1
'''
# should be foo() at a minimum 