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
    
    def LengthofCycleLoop(self) : 
        count = 0 
        real_count =0
        my_set = set() 
        temp = self.head  
        while temp is not None :  
            if temp in my_set:
                real_count = count  
                return  real_count
            count = count+1  
            temp = temp.next
