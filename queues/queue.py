# Queues are limited access data sturctures, in that items are inserted and removed
# according to the First-in First-out (FIFO) principle.
# Specifically, items can only be added to the back and removed from the front of the Queue.
# Enqueue means to insert an item into the back of the queue, and Dequeue means removing the front item.
# Theory: https://www.cs.cmu.edu/~adamchik/15-121/lectures/Stacks%20and%20Queues/Stacks%20and%20Queues.html
from collections import deque
class Queue:

    # Queues are built on top of other data structures.
    # This implementation uses an internal deque to store its data.
    # Documentation: https://docs.python.org/2/tutorial/datastructures.html#using-lists-as-queues
    def __init__(self):
        self.dataList = deque()

    def size(self):
        return len(self.dataList)

    # Appends value to the back of the queue.
    def enqueue(self, value):
        self.dataList.append(value)

    # Removes value from the front of the queue and returns it.
    def dequeue(self):
        return self.dataList.popleft()

    def print_data(self):
        print(self.dataList)

# Create a new empty Queue.
queue = Queue()

# Enqueue items into the queue.
queue.enqueue(10) # Front
queue.enqueue(11)
queue.enqueue(12)
queue.enqueue(13) # Back

# Exercise the queue...
#
print("Size (expect 4): ", queue.size())
queue.print_data()

# Dequeue an item from the queue.
x = queue.dequeue()
print("Dequeued (expect 10): ", x)
print("Size (expect 3): ", queue.size())
queue.print_data()

# Enqueue an item.
queue.enqueue(14)
print("Size (expect 4): ", queue.size())
queue.print_data()

# Dequeue another item off the queue.
x = queue.dequeue()
print("Dequeued (expect 11): ", x)
print("Size (expect 3): ", queue.size())
queue.print_data()