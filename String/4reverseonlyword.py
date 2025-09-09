str2 = "Hello Gyus" 
str1 =str2.split(" ") 
str3 = ""
for i in range(len(str1)-1 ,-1,-1):  
    str3 = str3 +" "+ str1[i] 
print(str3)