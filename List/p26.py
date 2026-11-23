
"""
25. Write a Java program to reverse the element of an integer 1-D array. 

"""
a=[1,2,3,4,5,6,7,8,9]
for i in range(len(a)//2):

    a[i],a[len(a)-(i+1)]=a[len(a)-(i+1)],a[i]

print(a)

#____________________________________________________________#

#using while loop

a=[1,2,3,4,5,6,7,8,9]

i=0
j=len(a)-1

while i<=j:
     temp=a[i]
     a[i]=a[j]
     a[j]=temp

     # a[i],a[len(a)-(i+1)]=a[len(a)-(i+1)],a[i]

     i+=1
     j-=1
print(a)    