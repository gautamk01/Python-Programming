# Lambda Function
# make a list of 4 items with it's price
items = [("Product1", 10), ("Product2", 9), ("Product3", 12), ("Product4", 1)]

items.sort(key=lambda item: item[1])
# [('Product4', 1), ('Product2', 9), ('Product1', 10), ('Product3', 12)]
print(items)
