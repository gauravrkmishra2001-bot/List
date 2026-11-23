"""
33. Write a java program to impelment binary search algorithm

"""

arr=[1,2,3,4,5,6,7,8,9,10]
n=int(input("enter a number:"))
low=0
high=len(arr)-1

while low<=high:

    mid =(low+high)//2

    if arr[mid]==n:
        print("element found")
        break
    elif arr[mid]>n:
        high=mid-1
    else:
        low=mid+1
else:
    print("element not found")