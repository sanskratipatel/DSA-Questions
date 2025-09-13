str1 = "hello world" 
result =""
for i in range(0 , len(str1)): 
    if i == 0 : 
        result =result + str1[i].upper()   
    elif str1[i-1] == " ": 
        result =result + str1[i].upper() 
    else: 
        result = result+ str1[i]
print(result) 
    