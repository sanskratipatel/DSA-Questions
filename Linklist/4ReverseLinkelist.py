# Reverse LinkedList 

class Node : 
    def __init__(self,val) : 
        self.val = val 
        self.next = None

class SLL:
    def __init__(self):
        self.head = None  
    def append(self,val) : 
        new_node = Node(val) 
        if self.head ==None : 
            self.head =new_node 
        else : 
            current = self.head 
            while(current.next is not None) : 
                current = current.next 
            current.next = new_node 
    def traversal(self): 
        if self.head == None: 
            print("Empty LL !!!!!!! ") 
        else : 
            current = self.head 
            while(current is not None) : 
                print(current.val, end=" ") 
                current= current.next
            print() 
    def reverse (self) :
        temp = self.head 
        prev = None 
        while(temp is not None) : 
            front = temp.next 
            temp.next=prev 
            prev = temp 
            temp =  front 



s1= SLL() 
s1.append(10)
s1.append(12) 
s1.append(13) 
s1.append(14) 
s1.traversal() 
s1.reverse() 
s1.traversal()