"""
enqueue() = Insert an element at the rear.

dequeue() = Remove an element from the front.

peek() = View the front element.

display() =  Display all queue elements

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    # Insert at the rear
    def enqueue(self, data):
        new_node = Node(data)

        # 1st node 
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

        print(data, "inserted into queue")

    # Remove from the front
    def dequeue(self):
        if self.front is None:
            print("Queue Underflow")
            return

        removed = self.front.data
        self.front = self.front.next

        # If the queue becomes empty
        if self.front is None:
            self.rear = None

        print(removed, "removed from queue")

    # View the front element
    def peek(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Front element:", self.front.data)

    # Display queue elements
    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        current = self.front
        print("Queue elements (front to rear):", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next

        print()


# Main program
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()
q.peek()

q.dequeue()
q.display()