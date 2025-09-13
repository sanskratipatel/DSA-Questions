nums = 20 
result = [] 
i = 1
while((nums//2) >= i) : 
    if nums % i == 0: 
        result.append(i) 
    i = i+1
print(result)