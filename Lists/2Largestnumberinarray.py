nums = [12,32,342,1,32,543,123,4]
largest = nums[0] 

for i in range(0,len(nums)):
    if largest <nums[i] :
        largest = nums[i] 
    
print("Largest = ",largest)
