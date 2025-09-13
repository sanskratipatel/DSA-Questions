str1 = "a2b3c4" 
pre = ""
output = "" 

for i in range(0 , len(str1) ): 
    if str1[i].isalpha() : 
        pre = str1[i] 
    else: 
        output = output + (pre * int(str1[i]) ) 

print(output)