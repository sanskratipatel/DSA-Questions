class Node : 
    def __init__ (self ,val) :
        self.val =val 
        self.next = None

class SLL: 
    def __init__(self):
        self.head = None 

    def append(self,val ): 
        newnode = Node(val)
        if self.head == None: 
            self.head =newnode 
        else: 
            curr = self.head 
            while curr.next is not None: 
                curr = curr.next 
            curr.next = newnode
    
    def traverse(self):
        if self.head ==None:
            print("SLL is empty") 
        else : 
            current = self.head 
            while current is not None:
                print(current.val , end = " ")
                current = current.next  
    def middleelement (self):
        temp = self.head
        count =0 
        while temp is not None:
            count = count + 1 
            temp = temp.next
        temp2 = self.head
        for i in range (0,count//2): 
            temp2 = temp2.next
        print("middle = ",temp2 ,"value ",temp2.val)


s1 = SLL()
s1.append(10)
s1.append(20) 
s1.append(110)
s1.append(201) 
s1.append(105)
s1.append(207) 
s1.traverse() 
s1.middleelement()




