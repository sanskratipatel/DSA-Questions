n =5 

for i in range(1,n+1) : 
    for j in range(1, i+1) : 
        print("*" , end=" ") 
    print()

# * 
# * * 
# * * *
# * * * *
# * * * * *


for i in range(1 ,n+1) : 
    print(" * " *i ,end = " ") 
    print() 

#  *
#  *  *
#  *  *  *
#  *  *  *  *
#  *  *  *  *  *  

# Inverted Triangle  
print()
for i in range(1 ,n+1) : 
    for j in range(i ,n+1) : 
        print("*" , end= " ")
    print() 

# * * * * *
# * * * *
# * * *
# * *
# * 
new= n
for i in range(1 , n+1) :  
  print("* " * new ,end = " ") 
  new  = new - 1
  print()  

# * * * * *
# * * * *
# * * *
# * *
# * 

for i in range(n , 0 ,-1): 
    for j in range(1 ,i+1): 
        print("*" ,end = " ") 
    print()   

# * * * * *
# * * * *
# * * *
# * *
# * 

