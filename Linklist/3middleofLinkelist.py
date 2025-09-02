class Node : 
    def __init__(self ,val):
        self.val = val 
        self.next = None
    

class SLL: 
    def __init__(self):
        self.head =None 
    
    def append(self,val) : 
        newnode = Node(val) 
        if self.head == None: 
            self.head = newnode 
        
        else : 
            current = self.head 
            while current.next is not None: 
                current = current.next  
            current.next = newnode
      
    def traversal(self) : 
        if self.head == None: 
            print("LL is Empty") 
        else:
            current =  self.head 
            while current is not None: 
                print(current.val ,end=" ")  
                current =current.next

    def middle_element(self) :  
        n =  0 
        temp = self.head 
        while temp is not None :  
            n = n+1 
            temp = temp.next 
        temp  =self.head 
        for i in range(0,n//2) : 
            temp = temp.next 
        return temp.val

s1 = SLL() 
s1.append(10) 
s1.append(20) 
s1.append(30) 
s1.append(40) 
s1.append(50)
s1.traversal() 
print()

print(s1.middle_element())

    