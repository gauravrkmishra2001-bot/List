
"""
34. Write a java program to implement linear search
"""
a=[10,20,30,40,50,60,70,80]
n=int(input("enter a value:"))
for i in a:
    if i==n:
        print(i,": Element Found")
        break
else:
    print("Element not found")