class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None

    def LinkedList_length(self):
        current_node = self.head
        length = 0
        while current_node is not None:
            length += 1
            current_node = current_node.next
        return length