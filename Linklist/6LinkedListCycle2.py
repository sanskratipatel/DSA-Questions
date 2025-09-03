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
    def cycleNode(self) : 
        temp = self.head  
        is_find = None  
        my_set = set()
        while temp is not None:  
            if temp in my_set: 
                is_find = temp 
                return is_find
            my_set.add(temp)
            temp = temp.next    

        if is_find is None: 
            print("Not circle and not find its first node ") 
        else: 
            print("node is = ",is_find)
 

