"""
Dictionaries store data in KEY: VALUE pairs
Written with { }
"""

students = {
    "name": "Leo",
    "age": 24,
    "major": "Computer Science"
}

print(students)

# ACCESSING items
print(students["name"])
print(students.get("major"))

# Adding new items
students["graduation_year"] = 2025
print(students)

# Changing values
students["age"] = 13
print(students)

# removing items
students.pop("major") # removes "major"
print(students)

# Check if KEY exists
if "name" in students:
    print("Yes, 'name' is in the dictionary")

# Nested Dictionary
student = {
    "student1": {"name": "Leo" , "age": 23},
    "student2": {"name": "Alex" , "age": 26}
}
print(student["student1"])

# Looping through a dictionary
# .keys() -> just the keys
# .values() -> just the values
# .items() -> key/value pairs together

for key in students.keys():
    print(key)

for value in students.values():
    print(value)

for key, value in students.items():
    print(f"{key}: {value}")


"""
 ------------------------------- 
MINI CHALLENGE: STUDENT REPORT CARD
-------------------------------
You need to store and analyze a student's grades.

1. Create a dictionary called "report_card" with keys:
    -"name"
    - "subject"
    - "grades" (use a tuple with 3 numbers)
Example: {"name": "Leo", "subject": "Math", "grades": (90, 85, 88)}
2. Print the student's name and subject.
3. Calculate the average of the 3 grades (HINT: use sum() and len()).
4. Add a new key called "average" with the calculated result.
5. If the average is 90 or above → print "Excellent!"
    If between 70 and 89 → print "Good job!"
    Otherwise → print "Needs improvement!"
6. Remove the "subject" key and print the updated dictionary.
"""













