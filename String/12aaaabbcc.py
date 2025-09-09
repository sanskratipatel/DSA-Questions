# Input :- AAAABBBCZZ
# output :- a4b3c1z2 

str1 = " AAAABBBCZZ" 
st1 = str1.strip() 
st2 =str1.replace(" ","") 
print(f"{st1} and {st2}")


count = 0 
pre = st2[0] 
output = ""
i = 0
while i < len(st2):
    if st2[i] == pre: 
        count = count +1 
    else: 
       output = output + pre + str(count) 
       pre = st1[i] 
       count = 1 
    if i == len(st2)-1: 
        output = output + pre + str(count) 
    i = i+1
print(output)