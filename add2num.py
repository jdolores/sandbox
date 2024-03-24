print("Write a program to find the sum of two numbers.")
def sum_two_numbers(x, y):
    return x+y

# Test Function
def test(x, y, z):
    if(sum_two_numbers(x,y) == z):
        print("{0} + {1} = {2}".format(x, y, z))
    else:
        print("{0} + {1} = {2} WRONG".format(x, y, z))

# Test Cases
test(1,1,2)
test(2,2,4)
test(-1,-1,-2)
test(-1,1,0)
test(0,0,0)
test(1.1,1.1,2.2)
test(-1.1,-1.1,-2.2)
test(-2,5,3)
test(2,2,5)#WRONG