nums = [1,0,1,23,1,1,1,0,1,2,3,4,1,1,1,1,1] 
counter = 0 
max_counter= 0 

for i in range(0 , len(nums)) : 
    if nums[i] == 1 : 
        counter = counter+1 
    else : 
        if max_counter < counter: 
            max_counter = counter
            counter = 0 
if max_counter < counter : 
    max_counter = counter 
print(max_counter)
