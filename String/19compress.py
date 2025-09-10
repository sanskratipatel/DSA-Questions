str1 = "aaabbcc" 
count = 1 
prev = str1[0] 
answer = ""
n = len(str1)
for i in range(1 , len(str1)) : 
    if prev == str1[i] : 
        count = count+1 
    else :  
        answer = answer +prev + str(count) 
        prev = str1[i] 
        count = 1 
    if i == (len(str1)-1):
      answer =answer + prev + str(count)  

n1 = len(answer) 

if n > n1: 
    print("Compress is not longest ",answer) 
else:
     print("Normal is sort ",str1)
 
