# code below produces an error
# points 2
'''
firstname = input("Enter first name: ")
secondname = input("Enter second name: ")
print("Your first name is %s and your second name is %s" % firstname, secondname)
'''
# parameters after % need to be a tuple
firstname = input("Enter first name: ")
secondname = input("Enter second name: ")
print("Your first name is %s and your second name is %s" % (firstname, secondname))