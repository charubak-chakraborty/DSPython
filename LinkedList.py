class Node():
    def __init__(self,data=None):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    def display(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next
    def insertAtEnd(self, data):
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = Node(data)
    def insertAtBeginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
