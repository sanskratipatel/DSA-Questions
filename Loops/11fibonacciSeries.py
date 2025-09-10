num = 10 
fib1 = 0 
fib2 = 1 
fib  = 0 
print(fib1,end =" ") 
print(fib2 , end = " ")
for i in range(0 ,8) :  
    fib =  fib1 +fib2 
    fib1 = fib2 
    fib2 = fib 
    print(fib ,end = " ")

print()
print(fib)
