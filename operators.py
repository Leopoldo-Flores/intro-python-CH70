# Arithmetic (basic math)

x = 1
y = 2
res = 0

res = x + y
print(res)

res = x - y
print(res)

res = x * y # multiplication
print(res)

res = x / y # division
print(res)

res = x % y # MODULUS - remainder after division
print(res)

res = x ** y # EXPONENTATION - to the power of
print(res)

res = x // y # Floor divisoin - divides and drops decimal
print(res)


# ASSIGNMENT OPERATOR - = used to assign values to variables 

x = 5
x += 5
x -= 3
x *= 3
x /= 3
print(x)

# comparison operator - used to compare two values (same as if and else)

# == (equals to), != (not equal), < > (less/greater than), <= >=(less/greter than or equal to)


# Logical operators - uesd to combine conditional statements
# used with True/False value like conditions
# and -> both must be True
# or -> at least one must be True
# not -> flips True to False (vise versa)

x = 3
y = 10
z = 10

print(x == y and y == z) # False, because both conditions are NOT true
print(x == y or y == z)  # True, because y = z
print(not x == y)        # True, because x != y not equal


# Identity operator- used to compare objects, not if they're equal but if they're the same object
# is -> checks if two things are the exact same object in memory
# is not -> checks if they are NOT the same

x = 3
y = 3
print(x is y)      # returns True if both variables are the exact same
print(x is not y)  # returns True if both variables are NOT the exact same


# Membership Operator - used to test if a sequence is presented in an object
# in -> checks if something exists inside a sequence(list, string...)
# not in -> checks if something dose NOT exist inside

x = [1, 2, 3, 4, 5] # this is a list

print(4 in x)      # True, because 4 is inside the list
print(9 not in x)  # True, because 9 is NOT inside the list






















