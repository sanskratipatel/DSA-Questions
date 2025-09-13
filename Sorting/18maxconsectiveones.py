nums = [0,1,0,1,1,0,1,1,0,0,1,1,1,1,1] 

largest = 0 
count = 0
for i in range(0 ,len(nums)): 
    if nums[i] ==1 : 
          count = count+1 
    else:  
        if largest < count:
          largest = count 
        count = 0  
    if largest < count:
          largest = count 
print(largest)