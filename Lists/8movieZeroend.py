nums = [1,0,1,2,9,0,1,0,2,0,5,0] 

result = [] 
n = len(nums)
print(n)
for i in range(0 , n): 
    if nums[i] != 0 : 
        result.append(nums[i]) 
n2 = len(result) 

for i in range(0,n2) : 
    nums[i] = result[i] 

for j in range(n2,n):  
    nums[j] = 0 

print(nums) 

# num3 = [1,2,0,0,2,3,5,0] 

