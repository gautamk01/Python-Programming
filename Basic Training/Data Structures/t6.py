# finding the index of a value in a list

letters = ["a", "b", "c"]
print(letters.index("b"))  # 1
# inside the bracket of index if we given a value which is not in the list
# then there will be an error
if "d" in letters:
    print(letters.index("d"))
