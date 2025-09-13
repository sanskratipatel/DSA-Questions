nums = [1,2,3,4,5,6,7] 
key = 3 
# if nums%key 
rotate = key % len(nums) 


for i in range(0 , key) :
       e = nums.pop() 
       nums.insert(0,e) 

print(nums)