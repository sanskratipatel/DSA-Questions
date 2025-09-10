str1 = "education"  
str1 = str1.lower() 
vow = "aeiou"
count = 0
for i in range(0 , len(str1)) : 
    # if str1[i] =='a' or str1[i] =='e' or str1[i] =='i' or str1[i] =='o' or str1[i] =='u':  
    if str1[i] in vow:
        count = count +1 
print(count)