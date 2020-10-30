# Singly linked list example.
# For the theory see:
# https://www.cs.cmu.edu/~adamchik/15-121/lectures/Linked%20Lists/linked%20lists.html

# Node represents an item in the list that
# stores some data (value) and a reference to the next Node (next).
# Getter/setter functions are needed to access or modify
# the Node's data and its position within the list structure.
class Node(object):

    # Constructor
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_data(self):
        return self.value

    def set_data(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


# This basic singly linked list simply stores the number of Nodes (count)
# and a reference to the first Node (head). Its functions
# define how Nodes are operated on, e.g. find, insert, delete.
#
# This is not an extensive implementation of all possible linked list operations.
class SinglyLinkedList(object):

    # Constructor instantiates an empty linked list.
    # 'head' initially stores 'None' until a Node is inserted.
    def __init__(self):
        self.head = None
        self.count = 0

    def get_count(self):
        return self.count

    # Takes the 'data' to be stored and handles the logic of instantiating
    # a Node object. This way, the code that uses this LinkedList doesn't need to
    # know its inner structure, i.e. it's decoupled from it.
    #
    # For simplicity, only inserts to the beginning of the list.
    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    # To find a specific data value stored within the list, start at the first Node
    # and check one by one until either (a) data is found, or (b) reach the last Node
    # without finding the data, i.e. data doesn't exist in the list.
    #
    # The last Node is determined by its 'next' reference to 'None' instead of a Node object.
    def find(self, value):
        node = self.head
        while (node != None):
            if node.get_data() == value:
                return node
            else:
                node = node.get_next()
        return None

    # Remove node from beginning, when it's the Head, or else from middle or end.
    # For simplicity, if there are two nodes with the given value, just remove the first one.
    def delete(self, value):
        head_node = self.head
        if head_node == None:
            # Head doesn't point to a Node so the list is empty.
            raise ValueError("Cannot delete from empty list.")
        elif head_node.get_data() == value:
            # Remove from beginning.
            self.head = head_node.get_next()
        else:
            # Now, it's known that list is not empty and Head doesn't store value,
            # so must remove either (a) middle, (b) end, or (c) nothing since value doesn't exist in list.
            #
            # Nodes in singly linked lists don't reference their previous Node, only next one,
            # so must use temporary variable (previous) while traversing the list.
            previous = self.head
            current = self.head.get_next()
            while ((current != None) and (current.get_data() != value)):
                # Move to next node.
                current = current.get_next()
                previous = current

            if (current == None):
                raise ValueError("Cannot delete non-existent value from list.")
            else:
                # Remove current node.
                # Changing previous' next to reference current's next node means that current
                # is no longer referenced by any node in the list; effectively removing it.
                previous.set_next(current.get_next())
        self.count -= 1

    def print_data(self):
        current_node = self.head
        while (current_node != None):
            print("Node: ", current_node.get_data())
            current_node = current_node.get_next()


# Create a linked list and insert some data.
list = SinglyLinkedList()
list.insert(38) # End
list.insert(49)
list.insert(13)
list.insert(15) # Head

list.print_data()

# Exercise the list.
print("Item count: ", list.get_count())
print("head: ", list.head.get_data())
print("Finding item: ", list.find(13))
print("Finding item: ", list.find(78))

# Deletion exercise.
#
# Removing a node from the beginning.
list.delete(15)
# Removing a node from the middle.
list.delete(49)
# Removing a node from the end.
list.delete(38)

print("Item count: ", list.get_count())
print("head: ", list.head.get_data())
list.print_data()