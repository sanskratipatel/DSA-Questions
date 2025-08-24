# ArmStrong Number 

nums = int(input("Enter the number = "))
count = 0 
num2 = nums

while(nums > 0 ):
    count = count +1
    nums = nums // 10   
asn =num2
arm = 0
print(count) 
while(num2 > 0 ): 
    arm = arm + (num2 % 10) ** count 
    num2 = num2 //10

if (asn == arm): 
    print("This is armstrong ",arm) 
else: 
    print("This not" ,arm)