list1 = [1,2,3,4,5,6,7,8,19] 
key = 19 
n = len(list1)
low =0
high =n-1


found = False
while(high >= low) : 
    mid = (high+ low) //2 
    if list1[mid] == key : 
        found = True 
        print(f"We find {key} at index {mid}") 
        break 
    elif list1[mid] > key :  
        high = mid -1 
    
    else: 
        low = mid+1 



    

