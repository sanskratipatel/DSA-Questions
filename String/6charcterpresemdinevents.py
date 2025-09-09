# Priint charcter whose are on even postion 

str1 = "Hello guys this is me" 
even = "" 
odd = ""
for i in range(0 , len(str1)) : 
    if i%2 == 0 :  
        even = even + str1[i] 
    else: 
        odd = odd + str1[i] 

print("Even Index character = ",even )  
print("Odd character index = ",odd)

