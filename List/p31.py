
"""
31. Suppose X. Y, Z are arrays of integers of size M, N, and M + N respectively. 
The numbers in array X and Y appear in descending order. 
Write a java program to produce third array Z by merging arrays X and Y in descending order. 
"""

a=[1,2,3,4,5]
b=[10,8,7,6]

m=len(a)
n=len(b)

c=m+n
c1=[]

for i in range(c):
    if(i<=n-1):
       # c1.insert(i,a[i])
       c1.append(b[i])
    else:
        c1.append(a[(c-1)-i])
        

print(c1)