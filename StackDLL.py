'''
Created on May 18, 2016

@author: Dell
'''
from DoublyLinkedList import DoublyLinkedList
from test.test_finalization import SelfCycleBase
class Stack(object):
    '''
    classdocs
    '''
    auxilaryStack = None
    
    def __init__(self):
        self.stack = DoublyLinkedList()
        self.count = 0
        self.middle = None
    
    def is_empty(self):
        pass
    
    def push(self, elem):
        self.stack.add(elem)
        
    def print_middle(self):
        print(self.stack.get_mid().data)
    def pop(self):
        return self.stack.delete()
    
    def peek(self):
        return self.stack.head
    
    def print_stack(self):
        self.stack.print_list()
    
    
    def find_middle(self):
        print(self.stack.get_middle())    
    
    def delete_middle(self):
        middle_node = self.stack.get_mid()
        if middle_node is not None and middle_node.previous:
            pre = middle_node.previous
            ne = middle_node.next
            pre.next = ne
            middle_node.next.previous = pre
            middle_node.previous.next = middle_node.next

s = Stack()
s.push(2)
s.push(5)
s.push(8)
s.push(9)
s.push(10)
# s.print_stack()
# 
# s.pop()
# print('after deleting element ')
s.delete_middle()
print('middle')
s.print_stack()
