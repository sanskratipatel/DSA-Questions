num = 1211
rev = 0 
num2 =num
while(num>0) : 
    rev = (rev *10) + num %10 
    num =num//10 
print(rev ) 
if rev == num2 : 
    print("Pallindrom")