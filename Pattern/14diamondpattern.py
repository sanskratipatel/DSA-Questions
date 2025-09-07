n = 5 

for i in range(1 , n+1) : 
    for j in range(i,n+1) : 
        print(" " , end=" ") 
    for k in range(1, i+1) : 
        print("*" , end=" ") 
    for l in range(1 ,i): 
        print("*",end=" ")
    print() 

for i in range(0 , n+1) : 
    for j in range(1 ,i+1) : 
        print(" ",end=" ") 
    for k in range(i ,n+1): 
        print("*" ,end=" ") 
    for l in range(i ,n): 
        print("*",end=" ") 
    print()  
 
#          * 
#         * * * 
#       * * * * *
#     * * * * * * *
#   * * * * * * * * *
# * * * * * * * * * * *
#   * * * * * * * * *
#     * * * * * * *
#       * * * * *
#         * * *
#           *