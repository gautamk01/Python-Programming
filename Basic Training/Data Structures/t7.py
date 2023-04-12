# soring the list
numbers = [42, 426, 7, 4, 646, 43]
numbers.sort()
print(numbers)  # [4, 7, 42, 43, 426, 646]
numbers.sort(reverse=True)
print(numbers)  # [646, 426, 43, 42, 7, 4]

# sorted function
# now the original list is change
# by using the sorted function we can sort the list without changing the original list
numbers = [42, 426, 7, 4, 646, 43]
print(sorted(numbers))  # [4, 7, 42, 43, 426, 646]
print(numbers)  # [42, 426, 7, 4, 646, 43]

# change to reverse
print(sorted(numbers, reverse=True))  # [646, 426, 43, 42, 7, 4]


# consider an senario where the list with product name and price is given
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]
# we want to sort the list by price
items.sort()
print(items)  # [('Product1', 10), ('Product2', 9), ('Product3', 12)]
# no change to make the sort by price


def sort_item(item):
    return item[1]


# this will help the sort function to sort the list by price
items.sort(key=sort_item)
print(items)  # [('Product2', 9), ('Product1', 10), ('Product3', 12)]
