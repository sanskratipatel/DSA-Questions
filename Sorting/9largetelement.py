arr = [1,2,3,4,4,3,2,1] 
largest = arr[0]
for i in range(0,len(arr)): 
    if largest < arr[i] :
        largest = i  

print(largest)