# input = a4k3b2 
# output = aeknbd 

str1= "a4k3b2"  
pre = ""
output= ""
for i in range(0 , len(str1)) :  
    if str1[i].isalpha(): 
        pre = str1[i] 
    
    else:  
        ch = ord(pre) + int(str1[i]) 
        output = output + pre + chr(ch) 
print(output)

