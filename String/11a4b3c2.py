# Input : - a4b2c3 
# Output :- aaaabbccc 

str1 = "a4b12c3"  
pre = 0
output = ""
for i in range(0 , len(str1)) : 
    if str1[i].isalpha() : 
        pre = str1[i] 
    else: 
        # pre2 = str1[i] 
        output = output + (pre * int(str1[i])) 

print(output)