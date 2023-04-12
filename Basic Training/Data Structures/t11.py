# List Comprehension
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]

# price = list(map(lambda item: item[1] > 9, items))
pricep1 = [item[0] for item in items]
pricep2 = [item[1] for item in items]
print(pricep1) # ['Product1', 'Product2', 'Product3']
print(pricep2) # [10, 9, 12]

# Filter
filteredlist = [item[1] for item in items if item[1] > 9]
print(filteredlist) # [10, 12]
 