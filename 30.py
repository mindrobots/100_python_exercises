# why do you get and error and how to fix it
# points 1

'''
def foo(a = 2, b):
    return a + b

'''
# you can't put default arguments before non-default arguments
# needs to be:
'''
def foo(b, a=2):
    return a + b
