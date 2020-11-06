
# Stacks are limited access data sturctures, in that items are inserted and removed
# according to the Last-in First-out (LIFO) principle.
# Specifically, items can only be added and removed from the top of the Stack.
# Push adds an item to the top, pop removes the item from the top.
# Theory: https://www.cs.cmu.edu/~adamchik/15-121/lectures/Stacks%20and%20Queues/Stacks%20and%20Queues.html
class Stack:

    # Stacks are built on top of other data structures.
    # This implementation uses an internal List to store its data.
    # Documentation: https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-stacks
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    # Appends value to the end of the internal list structure.
    def push(self, value):
        self.data.append(value)

    # Removes last value from the end of the list and returns it.
    def pop(self):
        return self.data.pop()

    # Returns the next item to be popped, but will not actually remove it from
    # the Stack like pop does.
    def peek(self):
        index_last_item = (len(self.data)-1)
        return self.data[index_last_item]

# Create a new empty stack.
stack = Stack()

# Push items onto the stack.
stack.push(10) # Bottom
stack.push(11)
stack.push(12)
stack.push(13) # Top

# Exercise the Stack...
#
print("Size: ", stack.size())

# Pop an item off the stack.
x = stack.pop()
print("Popped: ", x)
print("Now size is: ", stack.size())

# Peek an item from the stack.
x = stack.peek()
print("Peeked: ", x)
print("Size stays as: ", stack.size())

# Pop another item off the stack.
x = stack.pop()
print("Popped: ", x)
print("Now size is: ", stack.size())
