nums = [2,3,4,5,6,4,2,1,4,6,4] 

for i in range(0 , len(nums)):
    for j in range(0 ,len(nums)-1): 
        if nums[i] < nums[j] : 
            nums[i],nums[j] = nums[j], nums[i]

print(nums)