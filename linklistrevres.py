class link():
    def __init__(self,val):
        self.val=val
        self.next=None
class reverse():
    def __init__(self):
        self.head=None
    def middle(self,val):
        new_node=link(val) 
        if self.head==None:
            self.head=new_node
        else:    
            curr=self.head
        while curr.next!=None:
            curr=curr.next
        curr.next=new_node
    def rev():
        

