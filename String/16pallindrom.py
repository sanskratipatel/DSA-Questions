str1 = "MAdAM"
rev = "" 
str2 = str1.lower() 

for i in range( len(str1)-1,-1,-1) : 
    rev = rev + str1[i].lower() 

if rev == str2 : 
    print("Pallindrom") 
else: 
    print("not pallindrom")
    