"""
Store mutiple items in a variable.
Lists are created with [ ]
"""

my_list = [10, 20, 30, 40, 50]
print(my_list)

# Lists can contain different data types
mix_list = [1, "apple", 3.5, True]
print(mix_list)

# Accessing items by index - (indexing starts at 0)
fruits = ["apple", "banana", "cherry"]
print(fruits[1]) # Second item (banana)
print(fruits[0]) # First item (apple)

# You can also use Negative indexes to count in reverse
print(fruits[-1]) # Last item (cherry)

# Slicing a list
# Slicing lets you grab a RANGE of items using [start:stop:step] (skip)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])
print(numbers[:4])
print(numbers[6:])
print(numbers[-3:])
print(numbers[::2])  # skips every 2nd item

# Modifying lists items
fruits[1] = "mango"
print(fruits)

# Adding Items
fruits.append("orange") # adds ONE item to the END
print(fruits)

fruits.insert(1, "kiwi") # adds at a SPECIFIC position (intex 1)
print(fruits)

fruits.extend(["grape", "pear", "water"]) # adds MULTIPLE items to the end
print(fruits)                             

# REMOVE items
fruits.remove("apple") # Removes by VALUE (the first match it finds)
print(fruits)

fruits.pop()  # Removes the LAST item and returns it
print(fruits)

fruits.pop(3) # remoes the item at a SPECIFIC index
print(fruits)

#fruits.clear() # REMOVES EVERYTHING leaving an empty list
#print(fruits)

# Looping through a list
for items in fruits:
    print(items)

# Check if item exists
if "mango" in fruits:
    print("Yes, mango is in the list")

# List length
print(len(fruits)) # Numbers of items in the list

# useful list methods
numbers = [4, 2, 9, 1, 7, 2, 2]
print(numbers.count(2)) # how many times 2 appears in the list
print(numbers.index(9)) # the INDEX # of the item

numbers.sort()  # Sorts the list in order(small to large)
print(numbers)

numbers.sort(reverse=True)  # sort large to small (flips order)
print(numbers)

numbers.reverse()  # flips current list order
print(numbers)


# List comprehensions (a quicker way to build a list)
#

squares = []
for x in range(1, 6):
    #squares.append(x)
    squares.append(x * x)
print(squares)

"""
# -------------------------------
#  MINI CHALLENGE: THE GROCERY LIST
# -------------------------------
# You're building a grocery list app.

1. Create a list called "groceries" with at least 5 items.
2. Print the first and last item using indexing.
3. Use slicing to print just the first 3 items.
4. Add "eggs" to the end of the list using append().
5. Insert "milk" at the very beginning of the list.
6. Remove one item using remove().
7. Check if "bread" is in the list — print a message either way.
8. Sort the list alphabetically and print it.
9. Print how many items are in the final list.
"""





