from functools import reduce
num = [23,45,65,2,47,55]

max = reduce(lambda x, y : x if x >= y else y, num)

print(max)
 