nums = [1,2,3,4,5,6,7] 
num1 = [1,2,3,4,4,5,6,7,7] 

result = [] 
n = len(num1) 
m = len(nums) 
i = 0 
j = 0 

while i <n and j < m : 
    if num1[i] <= nums[j] : 
        if len(result) == 0 or result[-1] != num1[i] : 
            result.append(num1[i]) 
        i = i+1 

    else:
        if len(result) == 0 or result[-1] != nums[j]: 
            result.append(nums[j]) 
        j = j+1 
 

while i < n : 
    if len(result) == 0 or result[i] != num1[i]: 
        result.append(num1[i]) 
    i = i+1

while j  < m : 
    if len(result) == 0 or result[j] != nums[j]:
        result.append(nums[j])
    j = j+1 

print(result)