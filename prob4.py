lst1 = [1, 2, 5]
lst2 = [2, 4, 5]

intersection = list(filter(lambda x:x in lst1, lst2))

print(intersection)