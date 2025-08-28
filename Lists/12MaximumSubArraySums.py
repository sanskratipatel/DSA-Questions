nums = [-1,2,3,1,-2,-5,2] 

total = 0 
maxi = float("-inf") 

for i in range(0 , len(nums)) :  
    total = 0 
    for j in range(i , len(nums)) :
        total  = total +nums[j] 
        if total > maxi : 
            maxi = total 
print("Maxi answer = " ,maxi )
    
