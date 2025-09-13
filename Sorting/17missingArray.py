nums = [0,1,2,4] 
sum = 0 
realsum = 0 

for i in range(0 , len(nums)+1) : 
    realsum = realsum +i 
    if i < len(nums): 
        sum = sum + nums[i]
print(realsum ,sum , realsum-sum ) 