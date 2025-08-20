class Node: 
    def __init__(self,val):
        self.val = val
        self.next = None
    
class SLL:
    def __init__(self): 
        self.head =None
    
    def append(self, val): 
        new_node =Node(val) 
        if self.head == None:
            self.head =new_node 
        else : 
            current = self.head 
            while current.next is not None: 
                current = current.next
            current.next = new_node
    def travel(self): 
        if self.head == None:
            print("This is empty")
        else: 
            current =self.head
            while current is not None: 
                print(current.val , end = " ")
                current = current.next 
    def reverse(self ,head): 
        self.head = head
        

s1 = SLL()
s1.append(100)
s1.append(12)
s1.append(13)
s1.append(14)
s1.travel() 

