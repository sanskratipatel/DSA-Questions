arr= [1,2,3,4,5,6,7,8] 
n= len(arr)
key = arr[n-1]

for i in range(n-2,-1,-1):
    arr[i+1] = arr[i] 

arr[0] = key 

print(arr)