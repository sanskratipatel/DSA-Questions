str2 = "hello" 

dict1 = {} 

for i in range(0 , len(str2)) : 
    if str2[i] in dict1: 
        dict1[str2[i]] = dict1[str2[i]] +1 
    else:
        dict1[str2[i]] = +1  
print(dict1)

max_count = 0 
max_char = ""
for key in dict1 : 
    if dict1[key] > max_count: 
        max_count = dict1[key]  
        max_char = key

print(max_char)