class link:
    def __init__(self, val):
        self.val = val
        self.next = None


class linllist:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = link(val)

        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def rev(self):
        prev = None
        temp = self.head

        while temp is not None:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front

        self.head = prev

    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")


obj = linllist()

obj.append(1)
obj.append(2)
obj.append(3)
obj.append(4)

print("Before Reverse:")
obj.display()

obj.rev()

print("After Reverse:")
obj.display()