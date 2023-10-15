

"""enumerate(): This function is used to loop over an iterable and get both the index and value of each item. """

items = ['apple', 'banana', 'cherry']
for index, value in enumerate(items):
    print(f"Index: {index}, Value: {value}")


"""zip(): It combines multiple iterables into tuples. Useful for iterating over multiple lists in parallel."""

names = ['Alice', 'Bob', 'Charlie']
scores = [95, 88, 72]
for name, score in zip(names, scores):
    print(f"Name: {name}, Score: {score}")

"""all() and any(): These functions return True if all or any elements in an iterable are True."""

nums = [True, False, True, True]
print(all(nums))  # False
print(any(nums))  # True


"""max() and min() with custom key functions: You can provide a key function to find the maximum or minimum values based on a specific criteria."""

words = ['apple', 'banana', 'cherry']
longest_word = max(words, key=len)
print(longest_word)  # 'banana'

"""round(): Besides rounding to a specified number of decimal places, you can also round to the nearest multiple."""

value = 17
rounded_value = round(value, -1)  # Round to the nearest multiple of 10
print(rounded_value)  # 20

""" slice(): It allows you to create a slice object that can be used for slicing sequences like lists or strings."""

data = [0, 1, 2, 3, 4, 5]
my_slice = slice(2, 5)
print(data[my_slice])  # [2, 3, 4]

