num = [1,2,3,4,5,6,7,8] 

key = 5 
high = len(num)-1 
low = 0 
found = False
while (low <= high): 
    mid = (low+high)//2 
    if key == num[mid] :  
        print("find key = ",mid)
        found =True 
        break
    elif key > num[mid] : 
        low = mid+1 
    else : 
        high  = mid-1 
 
# print