"""
py实现队列结构
"""

class Queue:
    def __init__(self,head=None):
        self.storage = [head]

    def enqueue(self,new_element):
        self.storage.append(new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop(0)

# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

#Test peek
#should be 1
print(q.peek())

#Test enqueue
q.enqueue(4)
#should be 2
print(q.dequeue())
#should be 3
print(q.dequeue())
#should be 4
print(q.dequeue())

q.enqueue(5)
#should be 5
print(q.peek())
