#Q.2 Find minimum and maximum element in array
arr=[1,4,3,52,6,8]

max=arr[0]
min=arr[0]
for i in arr:
    if(min>i):
        min=i
    if(max<i):
        max=i
print(f"max is {max} or minimum is {min}")