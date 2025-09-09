str1 = "Hello This is me" 
str2 = str1.split(" ") 
print(str2) 
str4 = ""
for i in range(len(str2)-1,-1,-1) : 
    str4 = str4 + " "+ str2[i] 
    

str3 = ''.join(str2) 
print(str4)