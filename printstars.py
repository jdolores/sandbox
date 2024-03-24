#Printing *
#Print a triangle made of asterisks (‘*’) separated by spaces.
#The triangle should consist of n rows, where n is a given positive integer,
#and consecutive rows should contain 1, 2, . . . , n asterisks.
#For example, for n = 4 the triangle should appear as follows
#*
#**
#***
#****
#We need to use two loops, one inside the other:
# the outer loop should print one row in each step
# and the inner loop should print one asterisk in each step.
n = 4
for i in range(1, n + 1):
    for j in range(0, i):
        print("*", end='')#python 3 automatically prints new line unless this parameter is passed.
    print("")