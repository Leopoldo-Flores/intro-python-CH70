print("Hello world from python!")
print(2)
print(5 + 3)
print(True)

# SHORT CUT  ctrl + s to save 
"""
Everthing in here 
is a comment
"""


name = "Leo"
age = 24
print(name, age)
print(age)

# concatination
print("My name is: " + name + ", and I am " + str(age) + " years old.")

""" 
Mini challenge - 
1. Create 5 variables
2. Concatonate them into a story
3. print the story in the terminal
"""

# f-string
place = "disneyland"
activity = "riding the rollercoasters"
members = 5
print(f"The last time i went to {place}, I had a great time {activity} with {members} of my friends")

print(f""" This is 
            a mutli
line                {members}
           f-string print statement""")

#Type funcion
print(type(name))
print(type(age))
print(type(False))


#Casting (changing data types)
print(20 + int("20"))
print(20 + age)

# Input function
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

# input to int
new_age = int(input("Enter your age: "))
print(age + new_age)


"""
MINI CHALLENGE- pizza calculator
1. Ask how may slices of pizza and how many people (2 input())
2. Use math operators to calculate slices per person ( / )
3. Show the result using f-string
"""





















