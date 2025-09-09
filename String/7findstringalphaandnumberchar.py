# Find alphbate ,special character and number 

str1 = "123hell232o*^3" 

alpha = "" 
number = "" 
special = "" 

for i in range(0 ,len(str1)) : 
    if str1[i].isalpha() : 
        alpha = alpha +str1[i] 
    elif str1[i].isdigit(): 
        number = number + str1[i] 
    else: 
       special = special +str1[i] 
print("NUMBER = ",number) 
print("Alpha = ",alpha) 
print("Specail = ",special)