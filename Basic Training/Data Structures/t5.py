# adding or removing elements from a list

lettes = ["a", "b", "c"]

# add
lettes.append("d")
print(lettes)  # ['a', 'b', 'c', 'd']
lettes.insert(0, "-")
print(lettes)  # ['-', 'a', 'b', 'c', 'd']

# remove
lettes.pop()
print(lettes)  # ['-', 'a', 'b', 'c']
lettes.pop(2)
print(lettes)  # ['-', 'a', 'c']
lettes.remove("-")
print(lettes)  # ['a', 'c']

# alternative methord
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[0:4]
print(numbers)  # [5, 6, 7, 8, 9]

# clear
numbers.clear()
print(numbers)  # []
