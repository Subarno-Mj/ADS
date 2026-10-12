"""
append(data) adds an element to the rear of the queue.

pop(0) removes and returns the front element.

self.queue[0] accesses the front element without removing it.

"""

class Queue:
    def __init__(self):
        self.queue = []

    # Insert an element at the rear
    def enqueue(self, data):
        self.queue.append(data)
        print(data, "inserted into queue")

    # Remove an element from the front
    def dequeue(self):
        if not self.queue:
            print("Queue Underflow")
            return

        removed = self.queue.pop(0)
        print(removed, "removed from queue")

    # View the front element
    def peek(self):
        if not self.queue:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[0])

    # Display queue elements
    def display(self):
        if not self.queue:
            print("Queue is empty")
        else:
            print("Queue elements (front to rear):", *self.queue)


# Main program
q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()
q.peek()

q.dequeue()
q.display()