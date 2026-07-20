class link():
    def __init__(self,val):
        self.val=val
        self.next=None
class middle():
    def __init__(self):
     self.head=None
    def append(self,val):
       new_node=link(val)
       if self.head==None:
          self.head=new_node
       else:
          curr=self.head   
          while curr.next!=None:
             curr=curr.next
          curr.next=new_node
    def opt(self):
       slo=self.head
       fast=self.head
       while fast!=None and fast.next!=None:
          slo=slo.next
          fast=fast.next.next
       return slo.val
obj1=middle()
obj1.append(1)
obj1.append(5)
obj1.append(7)
obj1.append(8)
obj1.append(9)
print(obj1.opt())


                

