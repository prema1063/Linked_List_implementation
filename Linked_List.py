
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Insert a node at the beginning
    def insert_at_head(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    # Insert a node at the end
    def insert_at_tail(self, data):
        new_node = Node(data)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.size += 1

    # Delete a node by value
    def delete(self, data):
        current = self.head

        while current is not None:
            if current.data == data:

                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self.size -= 1
                return True

            current = current.next

        return False

    # Search for a value
    def search(self, data):
        current = self.head

        while current is not None:
            if current.data == data:
                return True
            current = current.next

        return False

    # Display the linked list
    def display(self):
        current = self.head

        print("HEAD → ", end="")

        while current is not None:
            print(current.data, end=" ⇄ ")
            current = current.next

        print("None")


# Create a linked list
obj = LinkedList()

obj.insert_at_head(10)
obj.insert_at_head(20)
obj.insert_at_tail(30)
obj.insert_at_tail(40)

obj.display()

obj.delete(20)
obj.display()

print("Search 30:", obj.search(30))
print("Size:", obj.size)
