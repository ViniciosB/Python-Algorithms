# Define a class for a node in the doubly linked list
class Node:
    def __init__(self, data):
        """
        Constructor to initialize a node.
        Each node contains:
        - data: The value stored in the node.
        - next: Pointer to the next node (initially None).
        - prev: Pointer to the previous node (initially None).
        """
        self.data = data
        self.next = None
        self.prev = None


# Define a class for the doubly linked list
class DoublyLinkedList:
    def __init__(self):
        """
        Constructor to initialize an empty doubly linked list.
        - self.head: The first node of the list (initially None).
        """
        self.head = None

    def append(self, data):
        """
        Adds a new node with the given data at the end of the linked list.
        - data: The value to be stored in the new node.
        """
        new_node = Node(data)  # Create a new node

        if not self.head:
            # If the list is empty, set the new node as the head
            self.head = new_node
            return

        # Otherwise, traverse to the last node
        last = self.head
        while last.next:
            last = last.next

        # Link the last node to the new node
        last.next = new_node
        new_node.prev = last  # Set the previous pointer

    def delete(self, key):
        """
        Removes the first occurrence of a node containing the given key.
        - key: The value to be removed from the linked list.
        """
        current = self.head  # Start from the head

        # Case 1: Deleting the head node
        if current and current.data == key:
            self.head = current.next  # Move head to the next node
            if self.head:
                self.head.prev = None  # Update the new head's previous pointer
            current = None  # Free memory
            return

        # Case 2: Deleting a node in the middle or at the end
        while current and current.data != key:
            current = current.next  # Move to the next node

        # If the key was not found
        if not current:
            print(f"Value {key} not found in the list.")
            return

        # If the node to be deleted is not the last node
        if current.next:
            current.next.prev = current.prev

        # If the node to be deleted is not the first node
        if current.prev:
            current.prev.next = current.next

        current = None  # Free memory

    def display_forward(self):
        """
        Prints all elements of the doubly linked list from head to tail.
        """
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")  # Indicate end of list

    def display_backward(self):
        """
        Prints all elements of the doubly linked list from tail to head.
        """
        current = self.head
        if not current:
            print("None")
            return

        # Traverse to the last node
        while current.next:
            current = current.next

        # Print in reverse order
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")  # Indicate start of list


# Example usage:

# Create an empty doubly linked list
dll = DoublyLinkedList()

# Add elements to the linked list
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

# Display the linked list from head to tail
print("Doubly Linked List (Forward):")
dll.display_forward()

# Display the linked list from tail to head
print("\nDoubly Linked List (Backward):")
dll.display_backward()

# Remove an element (e.g., 20)
dll.delete(20)

# Display the linked list after deletion
print("\nDoubly Linked List after deletion of 20:")
dll.display_forward()
