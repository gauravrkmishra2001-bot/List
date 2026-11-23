"""
35. Write a java program to implement selection sort algoritm

"""

a=[10,30,12,14,8,9]


for i in range(len(a)):
   
   m=i
   for j in range(i+1,len(a)):
       if(a[m]>a[j]):
           m=j

   a[i],a[m]=a[m],a[i]

print(a)