class Node:
    def __init__(self, data=None):
        # implement this
        pass

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None # extra pointer to the last node
        self.iseven = True

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node 
            self.tail = new_node # set tail point to the first node
        else:
            self.tail.next = new_node
            self.tail = new_node # update tail point to the new node
        self.iseven = not self.iseven

    def length_parity(self):
        # implement this
        return 'Odd' if self.iseven == False else "Even"
        pass
        

# Test cases:

linked_list = LinkedList()
linked_list.add_node(1) 
linked_list.add_node(2)
linked_list.add_node(3)
print(linked_list.length_parity()) # Expected 'Odd'
        
linked_list = LinkedList()
linked_list.add_node(10) 
linked_list.add_node(20)
linked_list.add_node(30)
linked_list.add_node(40)
print(linked_list.length_parity()) # Expected 'Even'
        
linked_list = LinkedList()
print(linked_list.length_parity()) # Expected 'Even'