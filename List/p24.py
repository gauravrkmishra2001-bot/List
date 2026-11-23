"""
23. Write a Java program to find the sum and average of one dimensional integer array. 

"""
a=[1,12,14,5]
sum=0
avg=0
for i in range(len(a)):
     sum=sum+a[i]
     
avg=sum/i
print(f"sum is :{sum}")
print(f"avg is :{avg:.2f}")
print("{:.2f}".format(avg))