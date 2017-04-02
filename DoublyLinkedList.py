'''
Created on May 1, 2016

@author: Dell
'''
from test.test_finalization import SelfCycleBase
class Node():
    
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.previous = None
        
class DoublyLinkedList():
    
    def __init__(self):
        self.head = None
        self.count = 0
        self.middle = None
        
    def delete(self):
        head = self.head
        next = self.head.next
        if head and next:
            next.previous = None
            self.head = next
        self.count -= 1
        return head.data
    def add(self, data):
        node = Node(data)
        node.next = self.head
        if self.head is not None:       
            self.head.previous = node
            
        self.count += 1
        if self.count == 1:
            self.middle = self.head
        elif self.count == 2:
            self.middle = self.head
        elif self.count % 2 != 0:
            self.middle = self.middle.previous
        self.head = node
        
        
        
             
    def get_mid(self):
        return self.middle
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
            
    def get_middle(self):
        slow = self.head 
        fast = slow.next
        
        while fast is not None and fast.next is not None:
#             print("fast is ,slow is ", fast.data, slow.data)
            slow = slow.next
            fast = fast.next.next
#         print ("slow.data ", slow.data, 'slow next ', slow.next.data)
        temp = slow.next 
        
        return slow.data 
    
  
    def reverse(self):
        temp = None
        current = self.head
        
        is_head = False
        while current:
            if not current.previous:
                n = current.next
                current.next = None
                current.previous = n
            elif not current.next:
                n = None
                p = current.previous
                current.previous = None
                current.next = p
                self.head = current
            else:    
                n = current.next
                print("current is ", current.data)
                current.next = current.previous
                print("next and current is ", current.next.data, current.previous.data)
                current.previous = n
            current = n
           
            
            
        
    def insert_sort(self, data):
        node = Node(data)
        current = self.head
        while current:
            if  current.data <= node.data:
                if current.next and current.next.data >= node.data:
                    node.next = current.next
                    node.previous = current
                    current.next = node
                    current.next.previous = node
                    break
                elif not current.next and current.data <= node.data:
                    node.previous = current
                    current.next = node
                    break
            elif not current.previous and current.data > node.data:
                node.next = current
                current.previous = node
                self.head = node
                break
            
            current = current.next
        self.print_list()
        
# li = DoublyLinkedList()
# li.add(7)
# li.add(6)
# li.add(4)
# li.add(3)
# li.add(5)
# 
# 
# li.print_list()
# 
# print(li.get_middle())
