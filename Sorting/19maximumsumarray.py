nums = [-2,1,-3,4,-1,2,1,-5,4] 

maxi = float("-inf") 

for i in range(0 , len(nums)) :  
    sum = 0 
    for j in range(i , len(nums)): 
        sum = sum +nums[j] 
        if sum > maxi : 
            maxi = sum 

print(maxi)
          
