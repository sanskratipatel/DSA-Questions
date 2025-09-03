nums = [1,1,1,2,3,4,5,5,6,7,7,8,9,55,343,554,2224,4534,4534] 
target  =int(input("ENter the number = ")) 
lowerbound =  0
low =  len(nums)
highbound = len(nums)-1 



while(lowerbound <= highbound): 
    mid = (lowerbound + highbound )//2
    if target >= nums[mid]: 
        low =mid 
        highbound = mid -1
        # print("Lower Bound Index is = ",low )
        
    else: 
        lowerbound = mid +1  

print(low)


high = len(nums) 

low1 = 0 
upperbound = high -1

while(low1 <= upperbound):
    mid1 =  (low1+upperbound)//2
    if nums[mid1] > target:
        high = mid1  
        upperbound = mid1 -1
       
    else: 
         low1 = mid1 +1
        
print(high)