str1 = "Hello this is me" 

str2 = str1.split(" ") 
str3 = ""
for i in range(0,len(str2)): 
    for j in range (len(str2[i])-1,-1,-1): 
          str3 = str3  + str2[i][j]  
    str3 = str3 +" "
print(str3)