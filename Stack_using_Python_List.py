# Python lists provide built-in methods like append() and pop() 
#  to implement a stack at the END 

class Stack:
    def __init__(self):
        self.stack = []

    # Insert an element
    def push(self, data):
        self.stack.append(data)
        print(data, "pushed into stack")

    # Remove the top element
    def pop(self):
        if not self.stack:
            print("Stack Underflow")
            return

        popped = self.stack.pop()
        print(popped, "popped from stack")

    # View the top element
    def peek(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])

    # Display stack elements
    def display(self):
        if not self.stack:
            print("Stack is empty")
        else:  
            print("Stack elements (top to bottom):", *self.stack[::-1])
            # * is to print element individually not as a list


# Main program
s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()
s.peek()

s.pop()
s.display()