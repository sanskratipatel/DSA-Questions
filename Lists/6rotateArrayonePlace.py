nums = [1,2,3,4,5,6,7,8,9,0,3]  

nums1= [nums[-1]] + nums[0 : len(nums)-1] 

print(nums1)
temp = nums[len(nums) -1]
result = []
for i in range(len(nums)-2 ,-1,-1) :  
    nums[i+1] = nums[i] 
nums[0] = temp
    
print(nums)