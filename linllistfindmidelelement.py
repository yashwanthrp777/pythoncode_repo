class link:
    def __init__(self, val):
        self.val = val
        self.next = None


class middlelist:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = link(val)

        if self.head == None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node

    def findmid(self):
        temp = self.head
        n = 0

        while temp != None:
            n += 1
            temp = temp.next

        temp = self.head

        for i in range(n // 2):
            temp = temp.next

        return temp.val


obj = middlelist()

obj.append(10)
obj.append(20)
obj.append(30)
obj.append(40)
obj.append(50)

print(obj.findmid())