class link:
    def __init__(self,val):
        self.val=val
        self.next=None
  

node1=link(1)
node2=link(2)
node3=link(3)

node1.next=node2
node2.next=node3

print(node1.val)
print(node2.val)
print(node3.val)
