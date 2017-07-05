# generate a list of strings from '1' to '20'
# points 1
my_list = list(range(1,21))
print([str(x) for x in my_list])
# or
print(list(map(str, my_list)))