from functools import reduce

numbers = [20, 55, 10, 90, 30, 80]

largest = reduce(lambda a, b: a if a > b else b, numbers)

print("Largest Number:", largest)