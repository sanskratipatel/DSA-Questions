str1 = "learning" 
str1 = str1.lower() 
vowels ="aeoui" 
i = 0
count = 0
while(i< len(str1)) : 
    if str1[i] not in vowels: 
        count = count+1  
    i = i+1 
print(count)