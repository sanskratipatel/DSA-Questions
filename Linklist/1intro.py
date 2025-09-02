class Node : 
    def __init__ (self,val) : 
        self.val = val 
        self.next = None 

        
n1 = Node(3)
n2 = Node(4) 
n3 = Node(5) 
n4 = Node(6) 
n1.next = n2  
n2.next = n3 
n3.next = n4


print(n1.next.next.val)