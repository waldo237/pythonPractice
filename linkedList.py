class LinkedListNode():
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return f"Node: data {self.data}, next: {self.next}"


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = LinkedListNode(data)

        if(self.head is None):
            self.head = newNode
            self.tail = newNode
        else:
            if(self.tail is not None):
                self.tail.next = newNode
                self.tail = newNode

    def prepend(self, data):
        newNode = LinkedListNode(data)
        if(self.head is None):
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def delete(self, value):
        if(self.head is None):
            return None
        else:
            if(self.head.data == value):
                self.head = self.head.next
            # elif(self.tail.data == value):
            #     self.tail = None
            else:
                currNode = self.head
                while(currNode is not None):
                    if(currNode.next is not None and currNode.next.data == value):
                        currNode.next = currNode.next.next
                    currNode = currNode.next

    def print(self):
        if(self.head is None):
            return None
        else:
            currNode = self.head
            while(currNode is not None):
                print(currNode.data)
                currNode = currNode.next

    def __str__(self):
        return f"LinkedList: head:{self.head}, tail:{self.tail}"


def main():
    list = LinkedList()
    list.prepend('primero')
    list.prepend('segundo')
    list.prepend('tercero')
    list.prepend('cuarto')
    list.delete('primero')
    list.delete('segundo')
    # list.delete('tercero')
    list.delete('cuarto')
    print(f'{list.print()}')


if __name__ == '__main__':
    main()
