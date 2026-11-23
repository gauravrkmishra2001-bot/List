"""
Q.9 Find the Union and Intersaction of two sorted array.
Given two arrays a[] and b[] of size n and m respectively. The task is to find union between these two arrays. 
Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in the union.
Example 1:
Input:
5 3
1 2 3 4 5
1 2 3
Output: 
5
Explanation: 
1, 2, 3, 4 and 5 are the
elements which comes in the union set
of both arrays. So count is 5.
Example 2:
Input:
6 2 
85 25 1 32 54 6
85 2 
Output: 
7
Explanation: 
85, 25, 1, 32, 54, 6, and
2 are the elements which comes in the
union set of both arrays. So count is 7.

"""

"""


n=int(input("enter a size of first array:"))
m=int(input("enter a size of Second array:"))
a= list(map(int, input(f"Enter {n} numbers: ").split()))
b= list(map(int, input(f"Enter {m} numbers: ").split()))
c=[]

count=0
for i in range(n):
    for j in range(m):
        if(a[i]==b[j]):
             c.append(a[i])
             count+=1

for x in a:
    if x not in b:
        c.append(x)


for x in b:
    if x not in a:
        c.append(x)


print(n+m-count)
print(c)


"""

arr1=[5,8,9,10,12]
arr2=[3,6,10,13,15]

i=0 
j=0

union=[]
tre=[]


while i<len(arr1) and j<len(arr1):

     if arr1[i]==arr2[j]:
          if not union or union[-1]!=arr1[i]:
             union.append(arr1[i])
             tre.append(arr1[i])
             i+=1
             j+=1
             
     elif arr1[i]<arr2[j]:
          if not union or union[-1]!=arr1[i]:
             union.append(arr1[i])
             i+=1
            
     else:
          if not union or union[-1]!=arr2[j]:
            union.append(arr2[j])
            j+=1
           
           

while i<len(arr1):
     union.append(arr1[i])
     i+=1

while j<len(arr2):
     union.append(arr2[j])
     j+=1
          

print(union)
print(tre)