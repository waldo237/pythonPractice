class LinkedListNode():
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = LinkedListNode
        self.tail = LinkedListNode

    def append(self, data):
        newNode = LinkedListNode(data)

        if(self.head):
            self.head = newNode
            self.tail = newNode
