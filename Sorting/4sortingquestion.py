arr = [2,3,4,5,2,5,5,6,7] 
# minmum = arr[0] 

for i in range(0 , len(arr)) :  
    minmum = i
    for j in range(i+1 , len(arr)) :  
        if arr[j] < arr[minmum]: 
            minmum = j  
        arr[i] ,arr[minmum] = arr[minmum],arr[i]
print(arr)

