class Node : 
    def __init__ (self,val) : 
        self.val = val 
        self.next = None 

class SSL : 
    def __init__(self) : 
        self.head = None
    
    def append(self,val) : 
        newnode = Node(val) 
        if self.head ==None : 
            self.head = newnode 
        else: 
            current  = self.head  
            while(current.next !=None ) :
               current = current.next 
            current.next = newnode
   
    def traversal (self) : 
        if self.head ==None: 
            print("Linkelist is Empty") 
        else : 
            current =  self.head
            while(current is not None) : 
                print(current.val ,end = " ") 
                current =current.next 
        
    def insert(self,position,val) : 
        newnode = Node(val) 
        if position == 0 : 
            newnode.next = self.head 
            self.head = newnode 
        else: 
            current =  self.head 
            prev_node = None 
            count = 0 
            while current is not None and count <position:
                prev_node = current 
                current = current.next 
                count = count +1 
            prev_node.next = newnode 
            newnode.next = current
    def delete (self,val ) : 
        temp = self.head 
        if temp.next is not None : 
            self.head = self.head.next  
            # temp.next = None 
            del temp  
            return 
        else : 
            found =False 
            prev =None
            while temp is not None: 
                if temp.val == val: 
                    found = True 
                    break 
                prev =temp 
                temp = temp.next
            if found:
                prev.next = temp.next 
                return

            else:
                print("Node  not found")
     
s1 = SSL() 
s1.append(1) 
s1.append(11)
s1.append(12)
s1.append(123) 
s1.append(123) 
s1.append(13) 
s1.append(133) 
s1.traversal() 
print()
s1.delete(13) 
s1.traversal()