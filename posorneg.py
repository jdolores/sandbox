print("Write a program to find the given number is positive or negative.")
def is_positive_or_negative(x):
    if(x >= 0):
        return 0 #positive
    else:
        return 1 #negative

# Test Function
def test(x):
    if(is_positive_or_negative(x) == 0):
        print("%s is positive" % x)
    else:
        print("%s is negative" % x)

# Test Cases
test(1)
test(2)
test(0)
test(-1)
test(-2)
test(1.1)
test(-1.1)
test(-2)