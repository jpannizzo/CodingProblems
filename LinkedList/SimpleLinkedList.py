class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print(f"self.head is set to {self.head}")
            return
        
        current = self.head
        while current.next:
            current = current.next
            
        current.next = new_node

    def display(self):
        print("This is the entire linked list:")
        current_node = self.head
        print(current_node.data, end="")
        while current_node.next is not None:
            next_node = current_node.next
            print(f"->{next_node}", end="")
            current_node = next_node

        
class Node():
    def __init__(self, value):
        self.data = value
        self.next = None
        print(f"Current Node Value: {self.data}")

    def __str__(self):
        return f"{self.data}"

list_values = [3,1,4,5]
myll = LinkedList()
for v in list_values:
    myll.append(v)

myll.display()