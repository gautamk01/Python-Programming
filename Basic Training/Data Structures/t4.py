letter = ["a", "b", "c"]
for letter in enumerate(letter):
    print(letter)
# Output :
# (0, 'a')
# (1, 'b')
# (2, 'c')

for letter in enumerate(letter):
    print(letter[0], letter[1])

# output
# 0 a
# 1 b
# 2 c

for index, letter in enumerate(letter):
    print(index, letter)

# output
# 0 a
# 1 b
# 2 c
