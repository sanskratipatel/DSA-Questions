nums = [1,2,3,4,6,7,8,9] 

target = 6 

for i in range(0 , len(nums)) : 
    if nums[i] == target : 
        print(f"{target} is the index of {i}") 
        break
    elif nums[i] > target : 
        print(f"{target} should come in index {i}") 
        break 

