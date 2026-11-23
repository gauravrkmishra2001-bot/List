#Q.3 Write a program to reverse the array.

arr=[6,3,4.8,8,0]
i=0
j=len(arr)-1

for i in range(len(arr)):
    if(i==j):
        break
    else:
        arr[i],arr[j]=arr[j],arr[i]
print(arr)