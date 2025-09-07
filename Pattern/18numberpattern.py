n =5 
p = n

for i in range(1 ,n) : 
    for j in range(i ,n+1) : 
        print(" ",end= " ") 
    for k in range(1 , i+1) : 
        print(p ,end= " ") 
    for l in range(1 , i) : 
        print(p ,end=" ") 
    p = p-1
    print() 

for i in range(1 ,n+1): 
    for j in range(1 ,i+1) : 
        print(" ",end=" ") 
    for k in range(i ,n+1): 
        print(p , end=" ") 
    for l in range(i ,n) : 
        print(p , end=" ") 
    p = p+1
    print()  
#           5 
#         4 4 4 
#       3 3 3 3 3
#     2 2 2 2 2 2 2
#   1 1 1 1 1 1 1 1 1
#     2 2 2 2 2 2 2
#       3 3 3 3 3
#         4 4 4
#           5

n =5 
p = n
p1 =1
for i in range(1 ,n) : 
    for j in range(i ,n+1) : 
        print(" ",end= " ") 
    for k in range(1 , i+1) : 
        print(p1 ,end= " ") 
    for l in range(1 , i) : 
        print(p1 ,end=" ") 
    p1 = p1+1
    print() 

for i in range(1 ,n+1): 
    for j in range(1 ,i+1) : 
        print(" ",end=" ") 
    for k in range(i ,n+1): 
        print(p1 , end=" ") 
    for l in range(i ,n) : 
        print(p1 , end=" ") 
    p1 = p1-1
    print()  


#           1
#         2 2 2
#       3 3 3 3 3
#     4 4 4 4 4 4 4
#   5 5 5 5 5 5 5 5 5
#     4 4 4 4 4 4 4
#       3 3 3 3 3
#         2 2 2
#           1
