
"""
30. Suppose A, B, C are arrays of integers of size M, N, and M + N respectively. 
The numbers in array A appear in ascending order while the numbers in array B appear in descending order.
 Write a java progtam to produce third array C by merging arrays A and B in ascending order.

"""

a=[1,2,3,4,5]
b=[10,8,7,6]

m=len(a)
n=len(b)

c=m+n
c1=[]

for i in range(c):
    if(i<=m-1):
       # c1.insert(i,a[i])
       c1.append(a[i])
    else:
        c1.append(b[(c-1)-i])

print(c1)