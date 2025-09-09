s1 = "Abhi" 
s2 ="Patel" 
i = 0 
j = 0 
output = ""
while (i< len(s1) and j < len(s2)): 
    output = output + s1[i] + s2[j] 
    i = i+1  
    j = j+1 

if len(s1) >i:
   while (i < len(s1)) : 
       output = output + s1[i]  
       i = i+1

if len(s2) >j:
   while (j < len(s2)) : 
       output = output + s2[j]  
       j = j+1

print(output)