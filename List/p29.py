"""
29. Suppose a one-dimensional array AR containing integers is arranged in ascending order.
 Write a java program to search for an integer from AR with the help of Binary search method, 

"""
a=[10,20,-303,460,150,-660,70,80]

for i in range(len(a)):
    for j in range(i+1,len(a)):

           if(a[i]>a[j]):
                 a[i],a[j]=a[j],a[i]

print(a)

n =int(input("enter a numbe:"))
g=0
h=len(a)
for i in range(h):
      l=(g+(h-1))//2
      if a[l]==n:
            print(" Element found")
            break
      elif a[l]>n:
            h=l
      else:
            g=l+1


else:
      print("Element not found")
