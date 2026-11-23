#Q.6 Sort the array of 0s , 1s and 2s.

arr=[1,0,2,0,1,0,2]

low=0
mid=0
high=len(arr)-1

while mid<high:
    if(arr[mid]==0):
        arr[low],arr[mid]=arr[mid],arr[low]
        low=low+1
        mid+=1
    elif(arr[mid]==1):
        mid+=1
    else:
        arr[high],arr[mid]=arr[mid],arr[high]
        high-=1



print(arr)