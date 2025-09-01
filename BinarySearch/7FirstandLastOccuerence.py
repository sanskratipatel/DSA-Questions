nums = [1,1,1,2,2,2,2,3,4,5,5,5,5,6,6,6,6] 

target = 2 

first = -1 
last = -1 

for i in range(0 ,len(nums)) : 
    if nums[i] == target: 
        if first == -1 : 
            first = i 
            last = i 
        else : 
            last = i 


print(f"First occurence is {first} and last is {last}")