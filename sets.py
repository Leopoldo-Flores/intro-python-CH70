"""
Sets are UNORDERED, UNINDEXED, and have NO DUPLICATES
created with {}
"""

# RANDOMIZED
fruits = {"apple", "banana", "cherry"}
print(fruits)

# NO DUPLICATES ALLOWED
fruits = {"apple", "banana", "apple"}
print(fruits)

# Check if item exists
print("banana" in fruits)

# Add Items
fruits.add("orange")
print(fruits)

# Adding multiple items
fruits.update(["kiwi", "mango"])
print(fruits)

# Removing Items
fruits.remove("banana") # Removes item (must exist in the set)
print(fruits)

# If you aren't sure an item exists, use .discard() to avoid errors
fruits.discard("papaya")
print(fruits)

# Set Operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))        # Combine both (no duplicates)
print(set1.intersection(set2)) # Common elements
print(set1.difference(set2))   # What's unique in set1
print(set1.symmetric_difference(set2)) # Everything EXCEPT whats shared

"""
-------------------------------
MINI CHALLENGE: STUDY GROUPS
-------------------------------
Two study groups are preparing for an exam.
1. Create two sets:
    - group_a = {"Leo", "Sam", "Alex", "Nina"}
    - group_b = {"Nina", "Jordan", "Sam", "Taylor"}
2. Print:
    - All students participating in either group (union)
    - Students who are in BOTH groups (intersection)
    - Students who are only in group_a (difference)
3. Add "Maya" to group_a.
4. Remove "Jordan" from group_b.
5. Print the total number of unique students across both groups.
6. If "Nina" is in both groups,
      print("Nina is helping both groups!")
   Otherwise,
      print("Nina is only in one group.")
7. Print the final version of both sets.
"""
























