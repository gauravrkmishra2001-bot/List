#Q.5 Find occurance of an integer number in array.

arr=[1,2,"hello","rat","2",3,"welcome"]
count=0
for i in arr:
    if(type(i)==int):
        count+=1

if(count>0):
    print(f"occurance of integer is :{count} times")