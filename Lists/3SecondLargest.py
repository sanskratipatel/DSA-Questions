nums = [12,342,4,3,23,34,4,2331,5,3,21]

largest = -float("inf") 
second_largest = -float("inf") 


for i in range(0,len(nums)):
    if nums[i] > largest:
        second_largest = largest
        largest = nums[i]

    elif nums[i] > second_largest and nums[i] <largest:
        second_largest = nums[i] 


print(largest) 
print(second_largest) 


minmum = float("inf") 
second_minimum = float("inf") 

for i in range(0 ,len(nums)) : 
    if nums[i] < minmum:
        second_minimum = minmum
        minmum = nums[i] 
    elif nums[i] < second_minimum and minmum < nums[i] :
        second_minimum = nums[i] 

print("minimum",minmum) 
print("second minimun =  ",second_minimum) 


num1 = set(nums) 
num2 = list(num1)

for i in range(0,len(num2)):
    mini = i
    for j in range(i ,len(num2)): 
        if num2[j] > num2[mini]: 
            mini = j
    num2[mini],num2[i] = num2[i] ,num2[mini] 

print(num2) 
