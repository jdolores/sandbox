# Credit: https://www.reddit.com/r/cscareerquestions/comments/cxja6r/how_to_crack_codility_test_with_a_week_preparation/
# Credit: https://drive.google.com/file/d/1-WTr1adkjwvOhnnZNjKOnMXC8GcPMFBV/view?usp=drive_link
#For Loops
sum = 0 #must initialize sum outside of for loop!
for i in range(1, 100+1): #Important to add 1 if you want 100 to be included in set of i
    sum += i #same as sum = sum + i
    print("i: {0} sum: {1}".format(i, sum))
print("Yay Gauss in the Haus!")

#Factorial
factorial = 1
n = 10
for i in range(1, n + 1):
    factorial *= i
    print("i: {0} sum: {1}".format(i, factorial))
print("Factorial from 1 to n: {0}".format(n))