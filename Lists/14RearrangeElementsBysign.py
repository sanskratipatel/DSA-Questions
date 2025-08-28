nums = [1,-1,2,3-4,-5,1,-7] 

posititve = [] 
negative = [] 

for i in range(0 , len(nums)) : 
    if nums[i] > 0 : 
        posititve.append(nums[i]) 
    else: 
        negative.append(nums[i]) 

result = []

for i in range(0 ,len(posititve)) : 
    # if len(result) == 0 : 
    #     result.append(posititve[i]) 
    # elif result[-1] > 0 : 
    #     result.append(negative[i]) 
    # elif result[-1] <0 : 
    #     result.append(posititve[i]) 
    result[(2*i)] = posititve[i] 
    result[(2*i) +1] = negative[i]

print(result)