#! /usr/bin/python2.7
########################################################################
# Implementation using collections.deque
# Queue in Python can be implemented using deque class from the collections module.
# Deque is preferred over list in the cases where we need quicker append and pop operations
# from both the ends of container, as deque provides an O(1) time complexity for append
# and pop operations as compared to list which provides O(n) time complexity.
# Instead of enqueue and deque, append() and popleft() functions are used.

# Python program to
# demonstrate queue implementation
# using collections.dequeue
print("=============================================================")
print("============= Queue used by collections.dequep ==============")

from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')

print("Initial queue")
print(q)

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)

# Uncommenting q.popleft()
# will raise an IndexError
# as queue is now empty
########################################################################

#'''
########################################################################
# https://www.geeksforgeeks.org/queue-in-python/
# Implementation using list
# list is a python's build-in data structure that can be used as a queue.
# Instead of enqueue() and dequeue(), append() and pop() function is used.
# However, lists are quite slow for this purpose because inserting or
# deleting an element at the beginning requires shifting all of the other elements by one,
# requiring O(n) time.
print("=============================================================")
print("======================== Stack push/pop =====================")
class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

a = Stack()
val = 1; print("stack push:  %d " % val); a.push(val)
val = 2; print("stack push:  %d " % val); a.push(val)
val = 3; print("stack push:  %d " % val); a.push(val)

print("stack size: ", a.size())
print("stack pop : ", a.pop())
print("stack pop : ", a.pop())
print("stack pop : ", a.pop())

print("=============================================================")
print("===================== Queue Enqueue/Dequeue =================")
class Queue():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def Enqueue(self, item):
        self.items.append(item)

    def Dequeue(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)

a = Queue()
print("Queue is empty? "); print(a.isEmpty())
val = 1; print("Queue Enqueue:  %d " % val); a.Enqueue(val)
val = 2; print("Queue Enqueue:  %d " % val); a.Enqueue(val)
val = 3; print("Queue Enqueue:  %d " % val); a.Enqueue(val)
print("Queue is empty? "); print(a.isEmpty())

print("Queue size    :", a.size())
print("Queue Dequeue :", a.Dequeue())
print("Queue Dequeue :", a.Dequeue())
print("Queue Dequeue :", a.Dequeue())
########################################################################
#'''
