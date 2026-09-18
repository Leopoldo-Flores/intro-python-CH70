"""
A while loop repeats a block of code as long as a condition is True.
Be careful - if the condition never becomes False, you'll get an INFINITE loop!

while condition:
    # Code block runs as long as the condition is True
"""

count = 1

while count <= 5:
    print("Count is: ", count)
    count += 1

print("----------------------------")

# Using BREAK to stop the loop
number = 0

while True: # infinite loop
    print(number)
    number += 1
    if number == 5:
        break # stop the loop when number reaches 5

print("----------------------------")

# using CONTINUE to skip an iteration
count = 0
while count < 5:
    count += 1 
    if count == 3:
        continue # skip 3
    print(count)

'''
Mini Challenge: password checker
1. Ask the user to enter a password
2. check if its correct (password: "secret123")
3. If its wrong, print "Wrong. try again!" and ask again
3. When they enter the correct password, print "access Granted"
'''

password = "secret123"                   # start empty
while password != "secret123":  # Keep looping while its wrong
    password = input("Enter password: ")
    if password != "secret123": # if wrong
        print("Wrong Try again")
    elif password == "secret123":
        print("access")


password = ""                   # start empty
while password != "secret123":  # Keep looping while its wrong
    password = input("Enter password: ")
    if password != "secret123": # if wrong
        print("Wrong Try again")

print("access granted")




































