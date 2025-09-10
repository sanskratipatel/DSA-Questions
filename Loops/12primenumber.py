num = 100 

for i in range(2, 101) :  
    is_prime =True
    for j in range(2 , int(i** 0.5 )+1): 
        if i%j == 0 :   
           is_prime = False
           break 
    if is_prime == True: 
        print(i ,end =" ")  


num = 7 
is_prime = True
for i in range(2,(num//2)+1): 
    if num % i == 0 :  
        is_prime = False
        print("not Prime number") 
        break 

if is_prime ==True : 
    print("Prime number")