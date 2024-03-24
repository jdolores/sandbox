# Credit https://www.learnpython.org/en/Hello,_World!
# Hello World
print("Hello World")

# Credit https://www.learnpython.org/en/Variables_and_Types
# Assignment and conditional
x = 1
if x == 2:
    print("x is 2.")
else:
    print("x is not 2 it is {0}.".format(x))

# Datatypes
myfloat = 7.0
print(myfloat)

#Cast an into to a float
myfloat = float(7)
print(myfloat)

#addition
one = 1
two = 2
three = one + two
print(three)

#string concatenation
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

#multiple assignment
a, b = 3, 4
print(a, b)

# Set Variables
mystring = "hello"
myfloat = 10.0
myint = 20

# Instance Check & Casting to specific formats for an instance
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)