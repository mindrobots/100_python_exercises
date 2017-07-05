# Mental exercise
# points 2
# Script below throws a NameError
'''
def foo(): 
    c = 1 
    return c 
foo() 
print(c)
'''
# because c exists in function foo's namespace but not in global namespace
# fix - make c global
'''
def foo():
    global c
    c = 1 
    return c 
foo() 
print(c)
'''