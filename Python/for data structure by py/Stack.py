"""
py实现栈的原理
"""

class Element(object):
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self,head=None):
        self.head = head

    def append(self,new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self,new_element):
        """在链表的头部插入一个新的元素"""
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        """删除链表中的第一个元素，并返回它"""
        if self.head:
            deleted_element = self.head
            temp = deleted_element.next
            self.head = temp
            return deleted_element
        else:
            return None

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top);

    def push(self,new_element):
        """把一个新的元素压入栈顶"""
        self.ll.insert_first(new_element)

    def pop(self):
        """把栈顶元素弹出并返回它"""
        return self.ll.delete_first()

# Test cases
# Set up some Eleents
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

#Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop().value)
print(stack.pop())
stack.push(e4)
print(stack.pop().value)
