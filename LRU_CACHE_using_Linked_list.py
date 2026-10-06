class Node:
    def __init__(self, key: int = 0, val: str = ""):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.capacity = capacity
        self.cache = {}

        
        self.next_key = 1

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> str:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove_node(node)

        self.add_to_head(node)

        return node.val


    def put(self, value: str) -> None:

        
        key = self.next_key
        self.next_key += 1

        node = Node(key, value)

        self.cache[key] = node

        
        self.add_to_head(node)

        self.size += 1

       
        if self.size > self.capacity:

            node = self.tail.prev

            self.cache.pop(node.key)

            
            self.remove_node(node)

            self.size -= 1


    def remove_node(self, node):

        node.prev.next = node.next
        node.next.prev = node.prev


    def add_to_head(self, node):

        node.next = self.head.next
        node.prev = self.head

        self.head.next = node
        node.next.prev = node


    # Display
    def print_cache(self):

        current = self.head.next

        print("\nHEAD → ", end="")

        while current != self.tail:
            print(f"[{current.key}: {current.val}]", end=" → ")
            current = current.next

        print("TAIL")



obj = LRUCache(4)

obj.put("insta")
obj.put("whatsapp")
obj.put("spotify")
obj.put("youtube")




obj.print_cache()