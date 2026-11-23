"""
Q.7 Sub array with given sum
Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

Example 1:
Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.

Example 2:
Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements 
from 1st position to 5th position
is 15.
1 <= N <= 105
1 <= Ai <= 109

"""

arr=[1,2,3,4,6,6]



target = 13
current_sum = 0
left = 0
right = 0

while left<right or right==left:
   # print(right,len(arr),left)

    current_sum = current_sum + arr[right]

    while current_sum > target and left < right:
        current_sum = current_sum - arr[left]
        left += 1
        print("left:",left)


    if current_sum == target:
        print(f"{arr[left]},{arr[right]}")
        break
    right+=1
    #print("rigth",right)
    if(right==len(arr)):
        print("target is not found")
        break
   
#print(current_sum)



