#Q.5 Find the kth largest and kth smallest element in array.
arr=[4,5,3,2,1,6,7]

n=int(input("Enter the value that larget number you want:"))

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            arr[i],arr[j]=arr[j],arr[i]
print(arr)
print(f" {n} largest number is:{arr[len(arr)-(n)]} or smallest number is:{arr[n-1]} ")
