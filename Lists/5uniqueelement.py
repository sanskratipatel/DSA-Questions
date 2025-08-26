nums =  [1,2,3,4,5,66,34,4,2,4,43,2,21,1,22,5,322,3] 

freq_map = {}

for i in range(0 , len(nums)):
    if nums[i] not in freq_map: 
        freq_map[nums[i]] = 0  

print(freq_map) 

j = 0 

for key in freq_map: 
    nums[j] = key 
    j = j+1 

print(nums)