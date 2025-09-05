class Queues : 
    def __init__(self): 
        self.item = [] 

    def push(self,items) : 
        self.item.append(items) 
    
    def isEmpty(self) : 
        return len(self.item) ==0 
    
    def front(self) :  
        if len(self.item) == 0 : 
            print("Cannot peek,queue is empty")
            return
        return self.item[0] 
    
    def dequeue(self) :  
        if len(self.item) == 0 : 
            print("Dequeue from empty queue")
            return
        return self.item.pop(0)
     
    def rear(self):
        if len(self.item) == 0: 
            print("Cannot Read,queue is empty ")
        return self.item[-1] 
    
    def size(self) : 
        return len(self.item) 
    

q1 =Queues() 

print(q1.isEmpty()) 
q1.push(10)
q1.push(20) 
q1.push(30) 
print(q1.dequeue()) 
print(q1.rear()) 
print(q1.front()) 
print(q1.size())