
"""
26. Write a Java program to find the largest and smallest element of an array.


"""

a=[11,34,12,15 ,36,78,21,23]

a1=a[0]
a2=a[0]
for i in range(1,len(a)):

      if a1>a[i]:
            a1=a[i]

      if a2<a[i]:
            a2=a[i]

print(f"Biggest element is: {a2} \nSmallest element is: {a1}")