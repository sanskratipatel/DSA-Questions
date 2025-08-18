nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]  
low =0
n = len(nums)
high = n-1

find = False
target = int(input("Enter the target = " )) 
while(low <= high) : 
    mid = (low + high) //2 
    if nums[mid]  == target: 
        find =True
        print("Find element at  index " ,mid ) 
        break
    elif nums[mid] > target:
        high = mid -1
    else : 
        low=mid+1

if find ==False:
    print(f"Element Not exists !!!!!!!!!!")
        

