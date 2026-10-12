# In a linked-list stack,
#  we insert and delete elements at the head of the linked list,
#  which is the top of the stack. This makes push() and pop() efficient O(1), 
#  without needing a fixed stack size.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None  # here top = head

    # Insert an element
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "pushed into stack")

    # Remove the top element
    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return

        popped = self.top.data
        self.top = self.top.next
        print(popped, "popped from stack")

    # View the top element
    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element:", self.top.data)

    # Display stack elements
    def display(self):
        if self.top is None:
            print("Stack is empty")
            return

        current = self.top
        print("Stack elements (top to bottom):", end=" ")

        while current:
            print(current.data, end=" ")
            current = current.next

        print()


# Main program
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()
s.peek()

s.pop()
s.display()