nums = [1,2,3,4,6,7,9,11,13,14]
floor = -1 
ceil = -1 

target = 123

for i in range(0 , len(nums)) : 
    if nums[i] == target : 
        floor = nums[i] 
        ceil = nums[i] 
        break
    elif nums[i] > target: 
         ceil = nums[i] 
         break
    else : 
        floor = nums[i] 

print(f"{floor} floor is  and {ceil}  ceil is ")