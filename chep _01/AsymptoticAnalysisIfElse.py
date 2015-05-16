"""
3 if then else statement : Worst case running time 
"""
n=100
if (n ==1):
    print('wrong value')
else:
    for i in range (1,n):
         print ('current number is :' , i)


#Total time = c0  + c1 *n = O(n)