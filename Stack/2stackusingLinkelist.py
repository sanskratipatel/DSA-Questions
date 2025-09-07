# Stack Using  Queue  
from collections import deque
class StackUsingQueue: 
    def __init__(self):
        self.items=deque()

    def pushing(self,item): 
        self.items.append(item)  
        for _ in range(len(self.items) -1) : 
            self.items.append(self.items.popleft())

    def top(self) : 
       if len(self.items) == 0:
           print("Stack is Empty") 
           return
       return self.items[0]
    
    def pop(self) : 
        if len(self.items) ==0:
            print("cannot pop,stack is empty")
            return
        return self.items.popleft()  
    
  

    def isEmpty(self):
        return len(self.items) == 0 

    def size(self) : 
        return len(self.items)


s1 = StackUsingQueue() 
s1.isEmpty()
s1.pushing(100) 
s1.pushing(200) 
s1.pushing(300)
print(s1.pop())
print(s1.top()) 
print(s1.size()) 
print(s1.pop())  
print(s1.size())