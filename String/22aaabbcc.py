str1 = "aabbccddd" 

pre = str1[0]
output = "" 
count = 0
for i in range(0 , len(str1)) : 
    if pre == str1[i] : 
        count=count + 1  
    else: 
        output = output + pre + str(count) 
        count = 1
        pre = str1[i]  
    if i == (len(str1)-1): 
        output = output + pre + str(count) 

print(output)