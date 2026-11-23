"""
Q.14. Find the first non-repeating elment in given array of integers
Find the first non-repeating element in a given array arr of N integers.
Note: Array consists of only positive and negative integers and not zero.
Example 1:
Input : arr[] = {-1, 2, -1, 3, 2}
Output : 3
Explanation:
-1 and 2 are repeating whereas 3 is 
the only number occuring once.
Hence, the output is 3.



"""

arr=[2,-1 ,-1,4,5,3,2]
c=[]

"""
for i in range(len(arr)):
    ct=0
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
             c.append(arr[i]) 

for i in arr:
    if i not in c:
        print(i)


"""
ct=0
d={}
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1


for i in arr:
    if d[i]==1:
        print(i)
        break

      
