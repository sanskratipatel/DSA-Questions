class StackClass: 
    def __init__(self): 
        self.item = []
    def isEmpty(self):
        return len(self.item) ==0 
    
    def push(self,items ): 
        self.item.append(items) 

    def pop(self): 
        if len(self.item)==0:
            return "Cannnot Pop Stack is already empty" 
        x = self.item.pop() 
        return x
    
    def top(self) : 
        if len(self.item) ==0:
            return "Camnnot top .stack is Empty" 
        return self.item[-1] 
    
    def size(self):
        return len(self.item)


s1 = StackClass() 

print(s1.isEmpty() ) 

s1.push(10) 
s1.push(20) 

print(s1.pop()) 
s1.push(40) 
print(s1.pop()) 
print(s1.top()) 
print(s1.pop()) 
print(s1.top() )