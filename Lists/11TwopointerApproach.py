nums = [11,12,3,4,8,9,1] 
target =10 

for i in range(0 , len(nums)-1) : 
    for j in range(i+1 , len(nums)) : 
        if nums[i] + nums[j] == target : 
            print(f"{i} and {j} Index sum = {target}") 
            break