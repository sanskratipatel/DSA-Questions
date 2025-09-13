arr = [1,0,2,0,3,0,4,0,6] 

list1 = []
list2 = [] 

for i in range(0 , len(arr)) : 
    if arr[i] == 0 : 
        list1.append(arr[i]) 
    else: 
        list2.append(arr[i])

print(list1 , list2) 
 
arr = list2 + list1 
print(arr)