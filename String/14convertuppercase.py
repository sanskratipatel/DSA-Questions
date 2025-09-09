str1 = "hello" 

# print(ord("h")) 
# print(ord('H')) 
 
str2 = ""
for i in range(0 , len(str1)) : 
    if str1.isalpha() : 
        ch = chr(ord(str1[i]) -32 ) 
        str2 = str2  + ch

print(str2)