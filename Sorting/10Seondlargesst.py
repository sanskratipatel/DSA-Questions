arr = [1,2,3,4,5,3,2,4,6,7] 
largest  = float("-inf") 
secondlargest = float("-inf") 

for i in range(0 , len(arr)) : 
    if arr[i] > largest:  
          secondlargest = largest
          largest = arr[i] 
    elif  arr[i] > secondlargest and arr[i] <largest : 
         secondlargest = arr[i]

print(largest , secondlargest)