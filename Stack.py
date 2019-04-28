class Stack():
    def __init__(self, size):
        self.items = []
        self.top = -1
        self.size = size
    def isEmpty(self):
        return len(self.items) == 0 
    def push(self,item):
        if self.top == (self.size-1):
            raise Exception('stack overflow exception')
        self.items.append(item)
        self.top = self.top + 1
    def pop(self):
        if self.top == -1:
            raise Exception('empty stack exception')
        itemToPop = self.items.pop()
        self.top = self.top - 1
        return itemToPop
    def peek(self):
        if self.top == -1:
            raise Exception('empty stack exception')
        return self.items[len(self.items)-1]
    def display(self):
        print(self.items)
    def reverse(self):
        if not self.isEmpty():
            poppedItem = self.pop()
            self.reverse()
            self.insertAtBottom(poppedItem)
    def insertAtBottom(self, data):
        if self.isEmpty():
            self.push(data)
        else:
            popped = self.pop()
            self.insertAtBottom(data)
            self.push(popped)
        
