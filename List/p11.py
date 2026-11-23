#Q.10.Write a program to cyclically rotate array by one.

arr=[1,2,3,4,5]
n=5

for i in range(n):
 t=arr[len(arr)-1]
 m=0
 j=0
 for i in range(len(arr)-1):
    m=j
    j=arr[i+1]
    if i==0:
     arr[i+1]=arr[i]
    else:
       arr[i+1]=m

 arr[0]=t

print(arr)



"""

arr=[10,20,30,40,50]

temp=arr[-1]
for i in range( len(arr)-1,0,-1):
     temp=arr[-1]
     for j in range(len(arr)):
          arr[j-1]=arr[j]
     arr[len(arr)-2]=temp
     print(arr)
     
"""

