# Unique character in string first 

 
str1 = "hello" 
dict1  = {} 

for i in range(0 ,len(str1)) : 
    if str1[i] in dict1:
         dict1[str1[i]] = dict1[str1[i]]+ 1
    else : 
         dict1[str1[i]] =1 

print(dict1)
find =False

for i in range(0 , len(str1)) : 
     if dict1[str1[i]] == 1 :   
          find = True
          print(f"{str1[i]} is index  {i}")  
          break


if find ==False : 
    print("There is no unique char")
     
str3 = "ll" 
unique = ""

for i in range(0 , len(str3)) :  
    count = 0
    for j in range(0 ,len(str3)) : 
          if str3[i] == str3[j] :  
               count = count +1 
    if count == 1:
        #  unique = unique + str3[i]
         print(str3[i]) 
         break 
else: 
     print("not exists")
# print(unique) 

str4 = "hey" 

# if i not in str4 : 
#      print("no") 
# else: 
#      print("yes")
               