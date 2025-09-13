arr = [1,2,3,4,5,1] 
is_asending =True 
is_desc = True 

for i in range(0 , len(arr)-1) :  
    if arr[i] >arr[i+1]: 
        is_desc = False 
    if arr[i] <arr[i+1] : 
        is_asending = False 
if is_asending == True:
    print("sorted in asec")
elif is_desc == True:
    print("Desv") 
else: 
    print("not sorted")