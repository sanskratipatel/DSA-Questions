# I love python 
# Longest word = Python 

str1 = "I love Python rwe" 
str2 = str1.split(" ") 
print(str2)  
longest = 0
word = ""
for i in range(0 ,len(str2)):
    if len(str2[i]) > longest: 
        longest = len(str2[i])   
        word = str2[i] 

print(word)

