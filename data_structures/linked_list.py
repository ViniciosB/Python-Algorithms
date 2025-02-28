# Define a class for a node in the linked list
class Node:
    def __init__(self, data):
        """
        Constructor to initialize a node.
        Each node contains:
        - data: The value stored in the node.
        - next: A pointer to the next node (initially set to None).
        """
        self.data = data  # Store the data in the node
        self.next = None  # Pointer to the next node, initially None


# Define a class for the linked list itself
class LinkedList:
    def __init__(self):
        """
        Constructor to initialize an empty linked list.
        - self.head: The first node of the list (initially set to None).
        """
        self.head = None  # Initially, the linked list is empty

    def append(self, data):
        """
        Adds a new node with the given data to the end of the linked list.
        - data: The value to be stored in the new node.
        """
        new_node = Node(data)  # Create a new node with the given data

        if not self.head:
            # If the list is empty, set the new node as the head (first node)
            self.head = new_node
            return  # Exit the function

        # Otherwise, traverse the list to find the last node
        last = self.head
        while last.next:
            last = last.next  # Move to the next node

        # Once we reach the last node, set its next pointer to the new node
        last.next = new_node

    def delete(self, key):
        """
        Removes the first occurrence of a node containing the given key.
        - key: The value to be removed from the linked list.
        """
        current = self.head  # Start from the head

        # Case 1: The node to be deleted is the head node
        if current and current.data == key:
            self.head = current.next  # Move the head to the next node
            current = None  # Free memory (optional in Python)
            return

        # Case 2: The node to be deleted is in the middle or at the end
        prev = None  # Keep track of the previous node
        while current and current.data != key:
            prev = current  # Move previous pointer
            current = current.next  # Move to the next node

        # If the key was not found in the list
        if not current:
            print(f"Value {key} not found in the list.")
            return

        # Unlink the node from the list
        prev.next = current.next
        current = None  # Free memory (optional)

    def display(self):
        """
        Prints all the elements of the linked list in order.
        """
        current = self.head  # Start from the head (first node)

        while current:
            # Print the data of the current node, followed by " -> "
            print(current.data, end=" -> ")

            # Move to the next node
            current = current.next

        # Print "None" at the end to indicate the end of the list
        print("None")


# Example usage:

# Create an empty linked list
ll = LinkedList()

# Add elements to the linked list
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

# Display the linked list before deletion
print("Linked List before deletion:")
ll.display()

# Remove an element (e.g., 20)
ll.delete(20)

# Display the linked list after deletion
print("\nLinked List after deletion of 20:")
ll.display()
