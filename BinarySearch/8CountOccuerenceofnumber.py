nums = [1,1,2,2,2,2,3,4,5,6,7,8] 

target = 2 
count = 0

for i in range(0,len(nums)) : 
    if nums[i] == target: 
        count = count+1 

if count == 0 : 
   print("Not exists in array ") 
else: 
    print(f"Exists {count } this much time in arrray")
