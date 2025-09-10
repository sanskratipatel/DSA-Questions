str1 = "pPRroOGRAMMmIiaNG" 
str1 = str1.lower() 
my_dict = {} 

for i in range(0 , len(str1)) : 
    if str1[i] in my_dict: 
        my_dict[str1[i]] = my_dict[str1[i]] +1  
    else : 
        my_dict[str1[i]] = 1 

print(my_dict)


min_occ = None 
max_occ = None 
max_count = float("-inf") 
min_count = float("inf")
for key in my_dict:  
    if my_dict[key] > max_count: 
        max_count = my_dict[key] 
        max_occ = key 
    if my_dict[key] < min_count : 
        min_count = my_dict[key] 
        min_occ = key

print(f"{min_occ} and its count is = {min_count}") 
print(f"{max_occ} and its count is = {max_count}")