"""
A conditional control structure that lets you decide which block of code to run
depending on whether a condition is True or False

if condition:
    - Code block runs if condition is True
elif another_condition:
    - Code block runs if the first condition is False
    - and this condition is True
else: 
    - Code block runs if none of the above conditoins are True
"""

x = 8

if x > 0:
    print("x is a positive number")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Short hand if statements
if x > 5 : print("x is greater than 5")

# short hand if..else
print("Even") if x % 2 == 0 else print("odd")

# Nested If Statements
if x > 0:
    if x < 20:
        print("x is a positive number less than 20")

# Combining conditions
age = 18

if age >= 15 and age <= 21:
    print("You are between 15 and 21")

"""
Mini challenge

1. Ask the user to enter a number from 0-100 and store it in a variable called "score". (input())
2. If the score is 90 or above, print "Grade: A".
3. If the score is between 80-89, print "Grade: B".
4. If the score is between 70-79, print "Grade: C".
5. Otherwise, print "Grade: F".

6. Create a variable "passed" — set it to True if score >= 70, otherwise False.
 BONUS: If passed is True, print "Congratulations!", otherwise print "Try again!"
"""










































