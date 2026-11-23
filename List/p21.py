"""
Q.20 Longest consecutive sequence.
Given an array of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
 
Example 1:
Input:
N = 7
a[] = {2,6,1,9,4,5,3}
Output:
6
Explanation:
The consecutive numbers here
are 1, 2, 3, 4, 5, 6. These 6 
numbers form the longest consecutive
subsquence.
Example 2:
Input:
N = 7
a[] = {1,9,3,10,4,20,2}
Output:
4
Explanation:
1, 2, 3, 4 is the longest
consecutive subsequence.

"""

arr= [1,2,3,4,8,6,7,10,11,12,14,15]


rate = 0
t=max(arr)

ct = [0] * (t + 1)

for i in arr:
    ct[i] = ct[i] + 1

j=0
for i in range(len(ct)):
    if( ct[i]>=1):
       arr.insert(j,i)
       j+=1

#u=len(arr)-1+len(ct)
#print(arr)

arr=arr[:j]
# del arr[j:u]
print(arr)

#________________________________________________________________________________#

t=len(ct)+1
ct.append(0)
ct.append(1)
ar=arr[0]


m=0
k=0
h=0
hg=0
cts=0

for p in range(len(ct)):
    if(ct[p]==1 ):
        cts+=1
        
        if(h==0 and k!=m):
            hg=p
            #print("hg",hg)
        h+=1
    else:
        h=0
        k=m
        if(m<cts):
            m=cts   
        cts=0


for i in range(len(ct)):
       if(i>=hg-(m+1) and i<=hg-1  and ct[i]==1):
           print(i,end=" ")

         


      
          

