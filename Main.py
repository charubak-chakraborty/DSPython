from Stack import Stack
from LinkedList import Node, LinkedList
from Employee import Employee
# stack implementation
# s = Stack(3)
# print(s.isEmpty())
# s.push(1)
# s.display()
# s.push(2)
# s.display()
# s.push(3)
# s.display()
# print(s.pop())
# s.display()
# print(s.peek())
# s.push(4)
# s.display()
# s.push(5)

# stack reverse
# s = Stack(3)
# print(s.isEmpty())
# s.push(1)
# s.display()
# s.push(2)
# s.display()
# s.push(3)
# s.display()
# s.reverse()
# s.display()

# list = LinkedList()
# list.insertAtBeginning(5)
# list.insertAtBeginning(4)
# list.insertAtEnd(6)
# list.display()

e1 = Employee('john',23,23000)
e2 = Employee('alice', 28, 60000)
e3 = Employee('drake', 35, 120000)
employees = [e1,e2,e3]
print(sorted(employees, key = lambda e: e.name))

