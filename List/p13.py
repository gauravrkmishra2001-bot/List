"""
 Q.12
Find common elements in three sorted arrays.
Given three arrays sorted in increasing order. Find the elements that are common in all three arrays.
Note: can you take care of the duplicates without using any additional Data Structure?
Example 1:
Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C.


"""
n1 = 6
a = [1, 5, 10, 20, 40, 80,80]
n2 = 5
b = [6, 7, 20, 80,80, 100]
n3 = 8
c = [3, 4, 15, 20, 30, 70, 80,80, 120]
t=0
"""
c=[]
for i in A:
    for j in B:
        for k in C:
            if i==j==k:
              if(t!=i):
                t=i
                c.append(i)

print(c)

"""
i=0;j=0;k=0
d=[]

while i<len(a)and j<len(b) and k<len(c):

      if a[i]==b[j]==c[k]:
         d.append(a[i])
         j+=1;i+=1;k+=1

      if a[i]<b[j]:
           i+=1
      elif b[j]<c[k]:
           j+=1
      else:
           k+=1
print(d)      




    



