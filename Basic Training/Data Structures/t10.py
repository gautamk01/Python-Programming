
# lIST fILTERING Function
items = [("Product1", 10), ("Product2", 9), ("Product3", 12), ("Product4", 1)]

x = filter(lambda item: item[1] >= 10, items)
print(x)
k = list(x)
print(k)
