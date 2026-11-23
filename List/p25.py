
"""
24. Write a Java program to swap first and last element of an integer 1-d array.

"""

a=[1,12,14,5]
a[0],a[-1]=a[-1],a[0]
print(a)
#----------------------------------------------------------
print("-"*50)
n=2
for i in range(n):
    a[0],a[-1]=a[-1],a[0]
    print(a)
