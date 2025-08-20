class Node: 
    def __init__(self,val):
        self.val =val
        self.next = None
    
class SinglyLinklist: 
    def __init__(self):
        self.head =None 
    def appendmethod(self,val):
        newnode = Node(val) 
        if self.head ==None:
            self.head =newnode 
        else :  
            curr =self.head
            while curr.next is not None: 
                curr = curr.next 
            curr.next = newnode
        
    def traversel(self): 
        if self.head is None:
            print("SLL is empty") 
        else:
            curr = self.head
            while curr is not None:
                print(curr.val, end = " ") 
                curr = curr.next

    def insert(self,position ,val):
        newnode = Node(val) 
        if position == 0 :
            newnode.next = self.head 
            self.head = newnode
        else:
            current = self.head 
            previous = None
            count =0 

            while current is not None and count < position:
                previous = current 
                current = current.next 
                count = count +1 
            previous.next =newnode 
            newnode.next = current
    def delete(self,val): 
        temp = self.head  
        if temp.next is not None:
            if  temp.val == val:
                self.head = self.head.next 
                temp.next =None
                del temp
            else:
                current = False
                previous = None
                count = 0 
                while current is not None :
                    if temp.val == val:
                        current =True
                        break 
                    previous = temp 
                    temp = temp.next
                if current : 
                    previous.next = temp.next 
                    return
                else:
                    print("Node not found")



sll =SinglyLinklist() 
sll.appendmethod(10)
sll.appendmethod(12) 
sll.appendmethod(13) 
sll.appendmethod(17) 
sll.traversel()
print("=================")
sll.insert(2,100)
sll.traversel()