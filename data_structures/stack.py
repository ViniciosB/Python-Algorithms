class Stack:
    def __init__(self):
        """
        Initializes an empty stack.
        - self.stack: List used to store stack elements.
        """
        self.stack = []

    def push(self, data):
        """
        Pushes an element onto the top of the stack.
        - data: The value to be added.
        """
        self.stack.append(data)  # Adds to the end of the list (top of the stack)

    def pop(self):
        """
        Removes and returns the top element of the stack.
        Returns None if the stack is empty.
        """
        if self.is_empty():
            print("The stack is empty!")
            return None
        return self.stack.pop()  # Removes and returns the last element

    def peek(self):
        """
        Returns the top element of the stack without removing it.
        Returns None if the stack is empty.
        """
        if self.is_empty():
            print("The stack is empty!")
            return None
        return self.stack[-1]  # Returns the last element of the list

    def is_empty(self):
        """
        Returns True if the stack is empty, otherwise False.
        """
        return len(self.stack) == 0

    def size(self):
        """
        Returns the number of elements in the stack.
        """
        return len(self.stack)

    def display(self):
        """
        Displays the stack elements (from top to bottom).
        """
        if self.is_empty():
            print("The stack is empty!")
        else:
            print("Stack (top -> bottom):", self.stack[::-1])  # Shows from top to bottom


# Example usage:

stack = Stack()  # Creates an empty stack

# Pushing elements onto the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Displaying the stack
print("Current stack state:")
stack.display()

# Checking the top element of the stack
print("\nTop element:", stack.peek())

# Removing an element from the stack
print("\nPopping:", stack.pop())

# Displaying the stack after removal
print("\nStack state after popping:")
stack.display()

# Checking the stack size
print("\nStack size:", stack.size())
