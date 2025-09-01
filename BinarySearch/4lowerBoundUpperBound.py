nums = [0,1,1,1,2,3,4,4,5,6,7,7,8,9,9,9,12,34,65,767,7654] 

lowerbound = len(nums)
target = 9 
low = 0 
high = len(nums) -1


while(low <= high): 
    mid = (low + high)//2 
    if nums[mid] >= target :
        lowerbound = mid  
        high = mid -1 
    else : 
        low = mid +1 

print(lowerbound) 


upperbound =len(nums) 
low1 = 0 
high1 = len(nums)-1 

while(low1 <=high1) : 
    mid = (low1+high1) //2 
    if nums[mid] > target : 
        upperbound = mid 
        high1 = mid -1 
    else: 
        low1 = mid +1 

print(upperbound)