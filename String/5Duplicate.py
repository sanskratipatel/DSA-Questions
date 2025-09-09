str1 = "Abhilasha patel hai z" 
result = "" 

for i in range(0 , len(str1)) : 
    if str1[i] not in result : 
        result = result + str1[i] 

print(result)