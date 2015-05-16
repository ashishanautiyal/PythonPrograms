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