arr= [1,2,1,3,4,5,4,3,2,1,4] 

my_dict = {} 

for i in range(0 ,len(arr)) : 
    if arr[i] not in my_dict: 
        my_dict[arr[i]] = 0 
    
j = 0 

for keys in my_dict : 
    arr[j] = keys 
    j = j+1 

print(arr) 
print(j)