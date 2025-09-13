str1= "a4k3b2"   
pre = ""
output = "" 

for i in range(0 ,len(str1)): 
    if str1[i].isalpha() : 
        pre = str1[i] 
    else : 
        char = ord(pre) + int (str1[i]) 
        output = output + pre + chr(char) 
print(output)