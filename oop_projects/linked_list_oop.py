"""A simple singly linked list implementation using OOP principles."""

class LinkedList:
    """A simple singly linked list implementation."""

    class Node:
        """Represents a node in the linked list."""
        def __init__(self, element):
            self.element = element
            self.next = None

    def __init__(self):
        self.length = 0
        self.head = None

    def is_empty(self):
        """Return True if the list is empty."""
        return self.length == 0

    def add(self, element):
        """Add an element to the end of the list."""
        node = self.Node(element)

        if self.is_empty():
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node

        self.length += 1

    def remove(self, element):
        """Remove the first occurrence of element from the list."""
        previous_node = None
        current_node = self.head

        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return

        if previous_node is not None:
            previous_node.next = current_node.next
        else:
            self.head = current_node.next

        self.length -= 1

    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.element))
            current = current.next
        return " -> ".join(elements) if elements else "Empty LinkedList"


if __name__ == '__main__':
    my_list = LinkedList()
    print(my_list.is_empty())

    my_list.add(1)
    my_list.add(2)
    print(my_list.is_empty())
    print(my_list.length)

    my_list.remove(1)
    print(my_list.length)
    print(my_list)
