print("Write a program to find if the given number is prime or not.")
# A prime number is only divisible by itself and 1.
# First find the midpoint, m, between 1 and n, if none of the numbers between 2 and m are divisors, the number is prime.
# O(n)

def is_prime(n):
    #print(n)
    m = n // 2
    #print(m)
    divisor = 1
    for i in range(2, m + 1): #inclusive of midpoint
        #print(i)
        if(n % i) == 0:
            divisor = i
            break
    #print(divisor)
    if divisor > 1:
        return False #found a divisor, so is not prime
    else:
        return True # did not find a divisor so is prime

# Test Function
def test(n, ans):
    output = is_prime(n)
    if(output ==  ans):
        if(ans):
            print("{0} is prime".format(n))
        else:
            print("{0} is not prime".format(n))
    else:
        print("FAIL")

# Test Cases
#test(1, True)
#test(2, True)
#test(4, False)
#test(5, True)
#test(9, False)
#test(51, False)
#test(53, True)
test(2717, True)

# Others to try: 2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729
# Credit https://en.wikipedia.org/wiki/List_of_prime_numbers