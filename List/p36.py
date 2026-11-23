"""
36. Write a java program to implement bubble sort algorithm
"""

a=[10,23,21,103,41,2]


for i in range(len(a)):
    for j in range(len(a)-i-1):

        if(a[j]>a[j+1]):
            a[j],a[j+1]=a[j+1],a[j]

print(a)