
arr = [0,1,2,13,4,87,98 ,54,56,56 ,75,45]
rate = 0
t=max(arr)

ct = [0] * (t + 1)

for i in arr:
    ct[i] = ct[i] + 1

j=0
for i in range(len(ct)):
    if( ct[i]>=1):
       arr.insert(j,i)
       j+=1

#u=len(arr)-1+len(ct)
#print(arr)

arr=arr[:j]
# del arr[j:u]
print(arr)

