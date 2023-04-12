# Zip Function
list1 = [1, 2, 3, 5, 6]
list2 = [10, 20, 30, 50, 60]

x = zip(list1, list2)
print(x)  # <zip object at 0x0000020B1B1B5C48>
print(list(x))  # [(1, 10), (2, 20), (3, 30), (5, 50), (6, 60)]

# [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
print(list(zip("abc", list1, list2)))
