nums = [2,1,3,4,5] 

sums = 0 
realsum = 0 

for i in range(0 , len(nums)+1) : 
    sums = i + sums 
    if i != len(nums):
        realsum = realsum + nums[i] 
missing_number = sums -realsum
print("Sums ==" ,sums) 
print("Real Sum = ",realsum)
print("Missing number === ",missing_number)
