from typing import Counter


class Node(object):
    """ A node for a doublyLinkedList """

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        """ append a new item to the end of the list """
        new_node = Node(data, None, None)
        if(self.head is None):
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def iter(self):
        """ Iterate through the list """
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def reverse_iter(self):
        """ Iterate throught the list backwards """
        current = self.tail
        while current:
            val = current.data
            current = current.prev
            yield val

    def delete(self, data):
        """ Delete a node from the list """
        current = self.head
        node_deleted = False

        if current is None:
            node_deleted = False
        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True

        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next

        if node_deleted:
            self.count -= 1

    def search(self, data):
        """ Search through the list. Return True if found """
        for node in self.iter():
            if data == data:
                return True
        return False

    def print_forward(self):
        """ Print the nodes in the list from beggining to end """
        for node in self.iter():
            print(node)

    def print_backward(self):
        """ Print from last to first. """
        current = self.tail
        while current:
            print(current.data)
            current = current.prev

    def insert_head(self, data):
        """ Insert a  new node at the head of the list """
        if self.head is not None:
            new_node = Node(data, None, None)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.count+= 1

    
