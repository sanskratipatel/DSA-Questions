class Node :
    def __init__(self, val):
        self.next = None 
        self.val =val 


a = Node(5) 
b= Node(6) 
c = Node(7)
d = Node(8)
a.next = b 
b.next = c 
c.next = d

print(a.val)
print(a.next.val)
print(a.next.next.val) 
print(a.next.next.next.val)