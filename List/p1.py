"""
Q.1 Peak an element

An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
Given an array arr[] of size N, find the index of any one of its peak elements.
Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0.
Example 1:
Input:
N = 3
arr[] = {1,2,3}
Output: 1
Explanation: index 2 is 3.
It is the peak element as it is 
greater than its neighbour 2.
Example 2:
Input:
N = 2
arr[] = {3,4}
Output: 1
Explanation: 4 (at index 1) is the 
peak element as it is greater than 
its only neighbour element 3.
Constraints:
1 ≤ N ≤ 105
1 ≤ A[] ≤ 106
"""
arr=[1,4,3,5,2,1,6]

for peak in range(len(arr)):
     if(peak==0 and arr[peak]>arr[peak+1]):
          print(f"{arr[peak]} is index of {peak}")
     elif peak==len(arr)-1 and arr[peak]>arr[peak-1]:
           print(f"{arr[peak]} is index of {peak}")
     elif arr[peak-1]<arr[peak]>arr[peak+1]:
          print(f"{arr[peak]} is index of {peak}")

