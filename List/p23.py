
"""
Q.22) Java program to find nearest lesser and greater element in array
Given an array of N elements and we have to find nearest lesser and nearest greater element using C program.
Example:
    Input:
    Enter the number of elements for the arrray : 3  
 
    Enter the elements for array_1.. 
    array_1[0] : 1   
    array_1[1] : 2   
    array_1[2] : 3   
 
    Enter the number : 2 
 
    Output:
    Element lesser than 2 is : 1 
    Element greater than 2 is : 3


"""
a=[1,12,14,15,16,2,3,4]

n=3

for i in range(len(a)):
    for j in range(i+1,len(a)):

        if(a[i]>a[j]):
            a[i],a[j]=a[j],a[i]

print(a)

for i in range(len(a)):
    if(n==a[i]):
        print(f" a[{i-1}]:{a[i-1]} \n a[{i}]:{a[i]} \n a[{i+1}]:{a[i+1]}")
 
