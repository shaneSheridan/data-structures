# Doubly linked list example.
# For the theory see:
# https://www.cs.cmu.edu/~adamchik/15-121/lectures/Linked%20Lists/linked%20lists.html

# Node represents an item in the list that
# stores some data (value) and a reference to both the next and previous Node.
# Getter/setter functions are needed to access or modify
# the Node's data and its position within the list structure.
class Node(object):

    # Constructor
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def get_data(self):
        return self.value

    def set_data(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next

    def get_previous(self):
        return self.previous

    def set_previous(self, previous):
        self.previous = previous


# This basic doubly linked list simply stores the number of Nodes (count)
# and a reference to the first Node (head). Its functions
# define how Nodes are operated on, e.g. find, insert, delete.
#
# This is not an extensive implementation of all possible linked list operations.
class DoublyLinkedList(object):

    # Constructor instantiates an empty linked list.
    # 'head' initially stores 'None' until a Node is inserted.
    def __init__(self):
        self.head = None
        self.count = 0

    def get_count(self):
        return self.count

    # Takes the 'data' to be stored and handles the logic of instantiating
    # a Node object. This way, the code that uses this linked list doesn't need to
    # know its inner structure, i.e. it's decoupled from other code.
    #
    # For simplicity, only inserts to the beginning of the list.
    def insert(self, data):
        new_node = Node(data)
        if (self.head != None):
            self.head.set_previous(new_node)
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
        node_to_delete = self.find(value)
        if (node_to_delete == None):
            raise ValueError("Cannot delete value. Either list is empty or doesn't contain value: ", value)
        elif (node_to_delete.get_previous() == None):
            # Remove from beginning.
            self.head = self.head.get_next()
            self.head.previous = None
        else:
            # Now, it's known that list is not empty, the value exists in the list, and node_to_delete is not
            # at the beginning of the list. So must remove it from either middle or end.
            #
            # Modifying node_to_delete's previous node to reference its next node, and node_to_delete's next node to
            # reference its previous node, means that node_to_delete is no longer referenced by any node in the list.
            # This effectively deletes it.
            previous_node = node_to_delete.get_previous()
            next_node = node_to_delete.get_next()
            previous_node.set_next(next_node)
            if (next_node != None):
                # next_node would be None if node_to_delete was at the end of the list, otherwise it's in the middle.
                next_node.set_previous(previous_node)
        self.count -= 1

    def print_data(self):
        current_node = self.head
        while (current_node != None):
            print("Node: ", current_node.get_data())
            current_node = current_node.get_next()


# Create a linked list and insert some data.
list = DoublyLinkedList()
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