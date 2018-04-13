"""[LinkedList]
python实现LinkedList
[description]
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

    def get_position(self,position):
        """
        返回该位置的元素
        第一个位置是"1"
        如果位置不在链表内，则返回None
        """
        counter = 1
        current = self.head
        if position < 1:
            return None
        while current and counter <= position:
            if counter == position:
                return current
            current = current.next
            counter += 1
        return None

    def insert(self,new_element,position):
        """
        在给定的位置离插入一个新的元素
        插入到“3”表示在第二到第三之间插入新元素
        """
        counter = 1
        current = self.head
        if position > 1:
            while current and counter < position:
                if counter == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
            

    def delete(self,value):
        """删除第一个值为value的结点"""
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

#test case
#set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

#start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

#Test get_position
#should print 3
print(ll.head.next.next.value)
#should also print 3
print(ll.get_position(3).value)

#Test insert
ll.insert(e4,3)
#should print 4 now
print(ll.get_position(3).value)

#Test delete
ll.delete(1)
#should print 2 now
print(ll.get_position(1).value)
#should print 4 now
print(ll.get_position(2).value)
#should print 3 now
print(ll.get_position(3).value)

