nums = [1,2,3,34,2,4,4,2,5,3] 
key =4

found =False 

for i in range(0 ,len(nums)) : 
    if key == nums[i] : 
        found = True
        print("FOund at = ", i) 
        break 

if found ==False: 
    print("Element not in List")