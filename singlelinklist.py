class link:
    def __init__(self,val):
        self.val=val
        self.next=None
class singlelink:
    def __init__(self):
       self.head=None
    def append(self,val):
         new_node=link(val)
         if self.head==None:
             self.head=new_node
         else:
            corr=self.head
            while corr.next!=None:
                corr=corr.next
            corr.next=new_node
    def traverse(self):
     if self.head == None:
        print("SLL is empty")
     else:
        corr = self.head
        while corr != None:
            print(corr.val)
            corr = corr.next 
sll=singlelink()
sll.append(2)
sll.append(3)
sll.append(5)

sll.traverse()



























  


