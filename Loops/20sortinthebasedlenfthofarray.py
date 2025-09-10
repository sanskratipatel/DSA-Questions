list1 = ["GO","PYTHON","JAVA","C"]  
my_dict = {} 
my_list =[]
for i in range(0 , len(list1)) : 
    if list1[i] not in my_dict: 
        my_dict[list1[i]] = len(list1[i])   
        my_list.append(len(list1[i]))


my_list = sorted(my_list)
print(my_list)  
my_list1 =[] 

for i in range(0 ,len(my_list)):
    for keys in my_dict: 
        if my_list[i] == my_dict[keys]: 
            my_list1.append(keys) 

print(my_list1)