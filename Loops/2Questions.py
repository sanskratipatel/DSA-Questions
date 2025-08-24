# Pallindrom Number
nums = int(input("Enter the number = ")) 
reverse = 0 
n = nums
while(nums > 0 ):
    reverse = reverse*10 + (nums % 10) 
    nums = nums // 10
print("Reverse = ",reverse) 

if reverse == n : 
    print("This is Pallindrom") 
else: 
    print("No") 

num1 = n 
str1 = str(n)
print((int(str1[::-1])))
