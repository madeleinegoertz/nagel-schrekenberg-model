# one node in a linked list
class Node:
    def __init__(self, data):
        self.data = data # contents of node
        self.next = None # pointer to next node in list

class CreateList:
    # connect the circle
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head
    
    # add a new node to the end of the list
    def add(self, data):
        new_node = Node(data)
        # check if list is empty
        if self.head.data is None:
            # if list is empty, both the head and tail point to the new node
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            # tail will point to new node
            self.tail.next = new_node
            # new node becomes the new tail
            self.tail = new_node
            # since it's circular, the linked list tail points to the head
            self.tail.next = self.head
    
    # displays all the nodes in the list
    def display(self):
        current = self.head
        if current is None:
            print("List is empty.")
        else:
            print("Nodes of the circular linked list.")
            # print each node by incrementing the pointer
            print(current.data)
            while (current.next != self.head):
                current = current.next
                print(current.data)

def test_list():
    cl = CreateList()
    cl.add(1)
    cl.add(2)
    cl.add(3)
    cl.add(4)
    cl.display()