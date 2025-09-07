nums = [1,2,3,2,4,3,5,4,5,4,2,1,3,5] 
new_dict = {}
for i in range(0,len(nums)):
    if nums[i] in new_dict: 
        new_dict[nums[i]] +=1
    else : 
        new_dict[nums[i]] = 1
print(new_dict)
print(new_dict[4])