# While loop using 
# Extraction of Digit 
nums = int(input("Enter the number = "))
sums = 0 
count =0
while(nums > 0 ):
    nums = nums % 10 
    sums = nums + sums
    count = count + 1  
    nums = nums -1 

print("Count = ",count) 
print("Sums = ",sums)