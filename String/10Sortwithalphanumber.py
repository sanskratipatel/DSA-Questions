# Sorting Alphabate then number  


def sorting(str1) : 
    str1 = list(str1)
    for i in range(0 , len(str1)): 
         for j in range(i , len(str1)) : 
             if str1[i] > str1[j] : 
                 str1[i],str1[j] = str1[j] ,str1[i] 
    
    return "".join(str1)


str1 = "A2F134E" 

alphabate = "" 
number = "" 

for i in range(0 , len(str1) ):
    if str1[i].isalpha() :
        alphabate =  alphabate + str1[i] 
    else : 
        number = number +str1[i] 

print(f"{number} and {alphabate}") 

numsort = sorting(number) 
alphasort = sorting(alphabate) 

ans = alphasort + numsort
print(ans)