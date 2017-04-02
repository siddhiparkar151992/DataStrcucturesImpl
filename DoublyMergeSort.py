'''
Created on May 7, 2016

@author: Dell
'''
import math

class Node():
    
    def __init__(self, data):
        self.data = data
        self.next = None 
        self.previous = None
        
class DoublyLinkedList():
    
    def __init__(self):
        self.head = None
        self.count = 0
    
    def __len__(self):
        return self.count
         
    def get_middle(self):
        slow = self.head 
        fast = slow.next
        
        while fast is not None and fast.next is not None:
            # print("fast is ,slow is ", fast.data, slow.data)
            slow = slow.next
            fast = fast.next.next
        
        return slow.data 
    
    def delete_middle(self):
        slow = self.head 
        fast = slow.next
        
        
        while fast is not None and fast.next is not None:
            print("fast is ,slow is ", fast.data, slow.data)
            slow = slow.next
            fast = fast.next.next
        return slow.data
    
    
    def add(self, data):
        node = Node(data)
        node.next = self.head
        if self.head is not None:       
            self.head.previous = node
        self.head = node
        self.count += 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
pairs = 0      
def merge(left, right, arr):
    result = left + right
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            global pairs
            pairs += 1
            arr[k] = right[j]
            j += 1
        else:
            
            arr[k] = left[i]
            i += 1
        k += 1
    # print("result ", result)
    # return result
            

def merge_sort(dlist):
    arr2 = []
    if len(dlist) > 1:
        mid = len(dlist) // 2
        left = arr[:mid]
        right = arr[mid:]
        
        # print("merging left and right", left, right)
        leftR = merge_sort(left)
        rightR = merge_sort(right)
        merge(left, right, arr)
    
        
arr = [5, 10, 34, 1, 89, 4, 45, 60, 34]
dlist = DoublyLinkedList()
for elem in arr:
    dlist.add(elem)

dlist.print_list()
print("middle of list is ", dlist.get_middle())


dlist.print_list()