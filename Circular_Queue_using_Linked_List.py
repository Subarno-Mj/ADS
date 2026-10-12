

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    # Insert an element into the queue
    def enqueue(self, data):
        new_node = Node(data)

        # If the queue is empty
        if self.is_empty():
            self.front = self.rear = new_node
            new_node.next = new_node
        else:
            new_node.next = self.front
            self.rear.next = new_node
            self.rear = new_node

        print(data, "inserted into the queue")

    # Remove an element from the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        data = self.front.data

        # If there is only one node
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

        print(data, "removed from the queue")
        return data

    # Display the elements
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return

        current = self.front
        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.front:
                break

        print("(frnot to rear)")


# Example usage
q = CircularQueue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)
q.enqueue(80)
q.enqueue(90)
q.enqueue(99)

q.display()

q.dequeue()
q.display()

q.enqueue(40)
q.display()
