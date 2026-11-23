"""
32. Given two arrays of integers A and B of sizes M and N respectively. Write a Write a java program, which will produce a third array named C. such that the following sequence is followed. 
All even numbers of A from left to right are copied into C from left to right. 
All odd numbers of A from left to right are copied into C from right to left. 
All even numbers of B from left to right are copied into C from left to right. 
All old numbers of B from left to right are copied into C from right to left.
e.g., A is {3, 2, 1, 7, 6, 3} and B is {9, 3, 5, 6, 2, 8, 10} the resultant array C is {2, 6, 6, 2, 8, 10, 5, 3, 9, 3, 7, 1, 3} 
33. Write a java program to impelment binary search algorithm

"""
a=[3, 2, 1, 7, 6, 3]
b=[9, 3, 5, 6, 2, 8, 10]
c1=[]
m=len(a)-1
n=len(b)-1

t=m+n+1
for i in range(t):
          if ( i<=m ):
                if(a[i]%2==0):
                  c1.append(a[i])
                    
          elif( b[i-(len(a)-1)]%2==0):
                  c1.append(b[i-(len(a)-1)])
                  


for i in range(t ,-1,-1):
          if ( i>n-1 ):
                if(b[i-(m+1)]%2==1):
                  c1.append(b[i-(m+1)])
                    
          elif( a[i]%2==1):
                  c1.append(a[i])
                  
print(c1)

