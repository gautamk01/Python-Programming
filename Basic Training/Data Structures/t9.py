# Map function
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
    ("Product4", 1)
]

price = []
for item in items:
    price.append(item[1])
print(price)  # [10, 9, 12, 1]

# using map function
x = map(lambda item: item[1], items)
print(x)
# <map object at 0x0000020E1D1B0D30>
# we can convert the map object to list
print(list(x))  # [10, 9, 12, 1]
# or we can convert this into a loop
for item in x:
    print(item)
# 10
# 9
# 12
# 1
