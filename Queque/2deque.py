from collections import deque 

lst1 = deque() 
lst1.append(100) 
lst1.append(200) 
lst1.append(300) 
lst1.append(400) 
lst1.appendleft(101)   # It add at first poistion  
lst1.appendleft(102) 
print(lst1) 
lst1.pop() 
print(lst1) 
print(lst1.popleft())    #First position remove 
print(lst1)