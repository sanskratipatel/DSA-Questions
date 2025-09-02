class Node : 
    def __init__(self,val): 
        self.val = val 
        self.next =None 
    
class SLL: 
    def  __init__(self): 
        self.head  = None 

    def append(self,val) : 
        new_node = Node(val) 
        if self.head == None:
            self.head =new_node 
        else: 
            current = self.head 
            while(current.next != None) : 
                current = current.next 
            current.next = new_node 

    def findcircleinLL(self) : 
        is_circle = False 
        temp = self.head 
        my_set = set() 
        while temp is not None : 
            if temp in my_set : 
                is_circle = True  
            my_set.add(temp) 
            temp = temp.next 
        if is_circle == True: 
            print("Cycle Exists")
        else:
            print("Not Exists")
