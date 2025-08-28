nums = [1,21,23,4,1,44,2,13,32,23,7] 
n = len(nums) 

max_profit = 0 

for i in range(0 , n) : 
    for j in range(i+1 , n):  
        if nums[j] > nums[i] : 
            p = nums[j] - nums[i] 
            if p > max_profit : 
                max_profit = p
print(max_profit)