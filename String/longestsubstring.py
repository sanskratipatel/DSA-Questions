s= "ABCDAEFASEGA" 
maxi = 0 

for i in range(0 , len(s)) :  
    my_set = set()
    for j in range(i , len(s)) :  
        if s[j] in my_set: 
            break 
        if maxi < (j-i+1) :  
            maxi = (j-i+1)
        my_set.add(s[j]) 
print(maxi)