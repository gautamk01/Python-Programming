# List Unpacking
numbers = [1, "This is cool...", 'A']
first, second, third = numbers
print(first)  # 1
print(second)  # This is cool...
print(third)  # A

multi = [1, 2, 4, 52, 53, 53, 5, 235, 5, 6]
first, second, *other = multi
print(other)  # [4, 52, 53, 53, 5, 235, 5, 6]
