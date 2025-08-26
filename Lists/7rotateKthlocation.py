nums = [1,2,3,4,5,6,7,8,9] 

k = 14 
if k > len(nums):
    k = k % len(nums) 
   
print(k)
for i in range(0 , k): 
    e = nums.pop()
    nums.insert(0,e) 
print(nums)