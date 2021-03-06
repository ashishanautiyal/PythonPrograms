#guideLines for Asymptotic Analysis
"""
1 Loops
"""

n = 10
# outer loop executed n times
for i in range(1, n):
    # inner loop executes n times
    for j in range(1, n):
        print ('i value %d and j value %d' % (i, j))  # constant time

# total time = c  X n X n = cn2  = 0(n2)

"""
2. Consecutive Statement : Add the complexities of each statements

"""

n = 100
for i in range (0,n):
    print ('current numnber is :',i)
for i in range (0,n):
    # inner loop will execute n times
    for j in range (0,n):
        print ('i value is :  %d and J value is : %d' %(i,j))

# total time = c0 + c1n +c2n2 = o(n2)