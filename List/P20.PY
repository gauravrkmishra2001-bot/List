'''
Q.19) Find Maximum product contigeous sub array 

Given an array Arr[] that contains N integers (may be positive, negative or zero). Find the product of the maximum product subarray.
Example 1:
Input:
N = 5
Arr[] = {6, -3, -10, 0, 2}
Output: 180
Explanation: Subarray with maximum product
is [6, -3, -10] which gives product as 180.
Example 2:
Input:
N = 6
Arr[] = {2, 3, 4, 5, -1, 0}
Output: 120
Explanation: Subarray with maximum product
is [2, 3, 4, 5] which gives product as 120.
'''

"""
arr = [6, -3, -10, 0, 2]
maxproduct=1
for i in range(len(arr)):
    product=1
    for j in range(i,len(arr)):
        product*=arr[j]
        if(product>maxproduct):
            maxproduct=product

print(maxproduct)

"""
#arr = [6, -3, -10, 0, 2]
arr = [2, 3, 4, 5,-9,7]

k=0
maxproduct=1
product=1
lister=[]
m=0
n=0
for i in range(len(arr)):
        
        product*=arr[i]
        if(product>maxproduct):
            maxproduct=product
            k=i
        if(i<len(arr)-2 and arr[i+1]==0 ):
              n=maxproduct
        if(arr[i]==0):
              product=1
              maxproduct=1
              m=i+1


if(n>maxproduct):
   maxproduct=n
   m=0

for i in range(m,k+1):
     lister.append(arr[i])   

print(maxproduct)
print(lister)