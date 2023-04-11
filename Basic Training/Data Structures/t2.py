# Accessing Items
letters = ["a", "b", "c"]
print(letters)  # ['a', 'b', 'c']
letters[0] = "A"
print(letters)  # ['A', 'b', 'c']
numbers = list(range(20))
print(numbers[0:3])  # [0, 1, 2]
print(numbers[:5])  # [0, 1, 2, 3, 4]
print(numbers[::2])  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(numbers[:])  # print the complete list
# [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(numbers[3:])
print(numbers[-1])  # 19
print(numbers[::-1])  # return the reverse of the list
