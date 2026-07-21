class link:
    def __init__(self, val):
        self.val = val
        self.next = None


class reverse:
    def __init__(self):
        self.head = None

    def middle(self, val):
        new_node = link(val)

        if self.head == None:
            self.head = new_node
        else:
            curr = self.head

            while curr.next != None:
                curr = curr.next

            curr.next = new_node

    def rev(self):
        temp = self.head
        stack = []

        while temp != None:
            stack.append(temp.val)
            temp = temp.next

        temp = self.head

        while temp != None:
            temp.val = stack.pop()
            temp = temp.next

        return self.head

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")


obj = reverse()

obj.middle(1)
obj.middle(2)
obj.middle(3)
obj.middle(4)
obj.middle(5)

print("Before Reverse:")
obj.display()

obj.rev()

print("After Reverse:")
obj.display()