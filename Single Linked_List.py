
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Singly_Linked_List:
    def __init__(self):
        self.head = None

    # Insert a node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert a node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        
        # if list is empty
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    # Delete the first occurrence of a value
    def delete(self, value):
        if self.head is None:
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    # Search for a value
    def search(self, value):
        current = self.head

        while current is not None:
            if current.data == value:
                return True
            current = current.next

        return False

    # Display all nodes
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Example usage
linked_list = Singly_Linked_List()

linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)

linked_list.display()
# Output: 10 -> 20 -> 30 -> None

linked_list.insert_at_beginning(5)
linked_list.display()
# Output: 5 -> 10 -> 20 -> 30 -> None

print(linked_list.search(20))
# Output: True

linked_list.delete(20)
linked_list.display()
# Output: 5 -> 10 -> 30 -> None
