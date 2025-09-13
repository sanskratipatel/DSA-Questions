nums =  153
count = 0 
num2 = nums 
num3 = nums
while(nums> 0 ):  
    n = nums%10
    count = count+1  
    nums = nums//10  
print(count)
arm = 0 
while(num2>0) : 
    arm = arm + (num2%10) **count  
    num2 = num2 // 10 
print(arm) 

if num3 == arm : 
    print("Yayyyyyyyyyy")