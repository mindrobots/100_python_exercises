# '+' is addition (for two numbers)
# or concatenation for two strings
# but it can't add a number and a string
# points 1
a = "1"
b = 2
# print(a + b) # original, this will give error
print(int(a) + b) # this will get rid of error
print(a + str(b)) # this will get rid of error
