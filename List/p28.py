
"""
28. P is one-dimensional array of integers.
Write a Java program search for a data VAL from P. 
If VAL is present in the array then “element found ” otherwise “element not found” should be displayed. 2

"""

arr = [10, 20, 30, 40, 50]

n=int(input("Enter a value:"))

for i in arr:
    if i==n:
        print("element found")
        break
else:
    print("element not found")


#------------------------------#
#using 
 
if n in arr:
    print("element found")
else:
    print("element not found")
