list1 = [1,2,3,4,5,6,7,8,9] 
key = 9 
n = len(list1)
low =0
high =n-1

print(high) 
found = False
while(high >= low) : 
    mid = (high+ low) //2 
    if mid == key : 
        found = True 
        print(f"We find {key} at index {mid}") 
        break 
    elif mid > key :  
        high = mid -1 
    
    else: 
        low = mid+1 



    

