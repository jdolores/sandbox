# Credit: https://www.prepbytes.com/blog/python/top-20-coding-questions-for-basic-python-programming/

print("Write a program to print the given number is odd or even.")

# Algorithm: use the modulus operator to check if the integer is divsible by 2.
# If it is exactly divisible by 2, modulus returns 0, then it is even.
def is_odd_or_even(x):
    if(x % 2 == 0):
        return 0 #even
    else:
        return 1 #odd

# Test Function
def test(x):
    if(is_odd_or_even(x) == 0):
        print("%s is even" % x)
    else:
        print("%s is odd" % x)

# Test Cases
test(1)
test(2)
test(0)
test(-1)
test(-2)
test(1.1)
test(-1.2)
test(-2)