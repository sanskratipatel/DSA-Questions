list1 = [1,2,3,4,5] 
list2 = [1,3,5,6,7,8,9] 
n1 = len(list1) 
n2 = len(list2) 
num = [] 
i = 0 
j = 0 
while(i < n1 and j < n2) : 
    if list1[i] <= list2[j] : 
        if len(num) ==0 or num[-1] != list1[i]  : 
            num.append(list1[i])  
        i = i+1
    else :
        if len(num) ==0 or num[-1] != list2[j]  :  
            num.append(list2[j])
        j = j+1
print(num) 

while(i < n1):
    if len(num) == 0 or num[-1] != list1[i]:
        num.append(list1[i])   
    i=i+1

while(j < n2):  
    if len(num) == 0 or num[-1] != list2[j]: 
        num.append(list2[j]) 
    j = j+1
print(num)