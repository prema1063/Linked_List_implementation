class Node:
    def __init__(self, data):
        self.data = data
        self.sai = None


class Stack:
    def __init__(self):
        self.top = None

    # Push → add an element to the top
    def push(self, data):
        new_node = Node(data)

        new_node.sai = self.top
        self.top = new_node

    # Pop → remove the top element
    def pop(self):
        if self.top is None:
            print("Stack is empty")
            return None

        value = self.top.data
        self.top = self.top.sai

        return value

    # Peek → see the top element
    def peek(self):
        if self.top is None:
            return None

        return self.top.data


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.peek())   # 30

print(stack.pop())    # 30
print(stack.pop())    # 20
print(stack.pop())    # 10