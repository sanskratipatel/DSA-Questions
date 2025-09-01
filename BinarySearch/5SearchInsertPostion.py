nums = [1,2,3,4,6,7,8,9] 
# if target exists retun index if not then insert correct postion 

target = 8
low = 0 
high = len(nums)-1 
lowerbound = len(nums) 

while(low <= high) : 
    mid = (low +high)//2  
    if nums[mid] >= target :  
        lowerbound = mid 
        high = mid -1 
    else : 
        low = mid +1  
print(lowerbound)