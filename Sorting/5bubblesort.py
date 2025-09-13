arr = [4,3,2,1,5,3] 

for i in range(0 , len(arr)) : 
    for j in range(i+1 , len(arr)) : 
        if arr[i] > arr[j] : 
            arr[i],arr[j] = arr[j],arr[i] 

print(arr)