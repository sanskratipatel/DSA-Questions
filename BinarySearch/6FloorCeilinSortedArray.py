nums = [3,4,5,6,7,8,9,11,12,14,15] 

floor = -1 
ceil = -1 
target = 10 
low = 0 
high  = len(nums)-1  

while(low <= high ) : 
    mid = (low + high) //2 
    if nums[mid ]== target : 
        floor = nums[mid] 
        ceil = nums[mid] 
    elif nums[mid] > target : 
        ceil = nums[mid]
        high = mid -1  
    else : 
        floor = nums[mid] 
        low = mid+1 
print(f"Floor value is {floor} and ceil is {ceil}")

