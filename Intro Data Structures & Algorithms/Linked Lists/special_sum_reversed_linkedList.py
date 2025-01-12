"""FIND THE SUM OF EVERY THIRD ELEMENT IN THE LINKED LIST WHILE REVERSE TRAVERSING"""
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.next = None
    def find_sum(self):
        stack = []
        node = self.head
        while node:
            # implement this
            stack.append(node.data)
            node = node.next
            pass
            
        sum_, index = 0, 1
        while stack:
            # implement this
            if index % 3 == 0:
                sum_ += stack.pop()
            else:   stack.pop()
            index += 1
            pass
        print(sum_)
        
        
    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    def print_list(self):
        current_node = self.head
        while(current_node):
            print(current_node.data, end="->")
            current_node = current_node.next
            
            
list = LinkedList()
list.insert(1)
list.insert(2)
list.insert(3)
list.insert(4)
# list.print_list()
list.find_sum()

