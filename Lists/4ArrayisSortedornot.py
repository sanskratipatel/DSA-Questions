nums = [1,2,3,4,6,662] 

is_ascending = True
is_desending = True
for i in range(0 , len(nums)-1) : 
    if nums[i] < nums[i+1]:
         is_ascending =False
    elif nums[i] >nums[i+1]:
         is_desending = False 
        

if is_ascending:
    print("Array is sorted in Ascending order")
elif is_desending:
    print("Array is sorted in Descending order")
else:
    print("Array is Not sorted")