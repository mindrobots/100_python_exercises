# code below produces an error
# points 2
'''
age = input("What's your age? ")
age_last_year = age - 1
print("Last year you were %s." % age_last_year)
'''
# input returns a string, need to convert
# string to int using int()
age = input("What's your age? ")
age_last_year = int(age) - 1
print("Last year you were %s." % age_last_year)