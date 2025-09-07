nums = [1,3,43,2,54,21,4,5,3] 
# Selection Sort 


for i in range(0 , len(nums)): 
    mininmum = i 
    for j in range( i+1 ,len(nums)) : 
        if nums[j] < nums[mininmum]: 
            mininmum = j
    nums[mininmum],nums[i] = nums[i] ,nums[mininmum] 
print("Minimum index = " , nums)