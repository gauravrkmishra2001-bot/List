n = 8
arr=[1, -1, 3, 2, -7, -5, 11, 6]


pos_list=[arr[i] for i in range(len(arr)) if arr[i]>0]
neg_list=[arr[i] for i in range(len(arr)) if arr[i]<0]

arr=pos_list+neg_list
print(arr)