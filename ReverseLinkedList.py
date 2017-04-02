'''
Created on Apr 26, 2016

@author: Dell
'''

class Node(object):
    '''
    classdocs
    '''


    def __init__(self, data=None, next_n=None):
        '''
        Constructor
        '''
        self.data = data
        self.next = next_n
        
class LinkedList(object):
    
    def __init__(self):
        self.head = None
        self.count = 0
        
    def add(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.count += 1
        
    def reverse(self):
        pre = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = pre
            pre = current
            current = next
        self.head = pre
    def get_middle(self):
        slow = self.head 
        fast = slow.next
        pre = None
        while fast is not None and fast.next is not None:
            # print("fast is ,slow is ", fast.data, slow.data)
            pre = slow
            slow = slow.next
            fast = fast.next.next
        if self.count % 2 == 0:
            temp = slow
            slow.next = slow.next.next
            return
        print("previous of middle is ", pre.data)
        temp = pre
        pre.next = slow.next
        
        return slow.data
        
    def detect_loop(self):
        slow_pointer = self.head
        fast_pointer = self.head
        
        while slow_pointer and fast_pointer and fast_pointer.next:
            
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                fast_pointer.next.data = None
                return "found"
                
        return "loop not found"
            
    
            
                
        
    def printList(self):
        temp = self.head
        li = []
        while temp:
#             print(temp.data)
            li.append(temp.data)
            temp = temp.next
        print(' '.join(list([str(i) for i in reversed(li)])))
            
    def find_length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
    
    def swap_nodes(self, x, y):
        current = self.head
        x_node = None
        x_node = None
        if x == y : return
        preX = None 
        currentX = self.head
        preY = None
        currentY = self.head
        
        while True:
            if currentX is not None and currentX.data != x:
                preX = currentX
                currentX = currentX.next
            elif currentY is not None and currentY.data != y:
                preY = currentY
                currentY = currentY.next
            
        if currentX is None or currentY is None: 
            return
        
        if preY is not None:
            preY.next = currentX
            
        else :
            currentY = self.head
        if preX is not None:
            preX.next = currentY
            
        else :
            currentX = self.head
            
        temp = currentX.next
        
        currentX.next = currentY.next
        currentY.next = temp
        
        
            
            
    
def merge_sorted_list(l1, l2):
    curr_a = l1.head 
    curr_b = l2.head
    
    l = LinkedList()
    while curr_a or curr_b:
        if curr_a == None:
           
            while curr_b is not None:
                l.add(curr_b.data)
                curr_b = curr_b.next
            break
        elif curr_b is None:
            
            while curr_a is not None:
                l.add(curr_a.data)
                curr_a = curr_a.next
            break
        if curr_a.data < curr_b.data:
            c = curr_a
            curr_a = curr_a.next
        else:
            c = curr_b
            curr_b = curr_b.next
        l.add(c.data)
        
    l.printList()
            
          
                
llist = LinkedList()
 
# The constructed linked list is:
# 1->2->3->4->5->6->7
llist.add(7)
llist.add(6)
llist.add(5)
llist.add(4)
llist.add(3)
llist.add(2)
llist.add(1)
 
# llist.printList()
# llist.reverse()
# print("\nReversed Linked List")
# llist.printList()
# print ("Length of the list is ", llist.find_length())

# llist.swap_nodes(3, 4)
# print("after swapping ")
# llist.printList()


rlist = LinkedList()
 
# The constructed linked list is:
# 1->2->3->4->5->6->7
rlist.add(14)
rlist.add(12)
rlist.add(10)
rlist.add(8)
rlist.add(6)
rlist.add(4)
rlist.add(2)
''
# merge_sorted_list(rlist, llist)


rlist = LinkedList()
 
# The constructed linked list is:
# 1->2->3->4->5->6->7
rlist.add(1)
rlist.add(2)
rlist.add(3)
rlist.add(8)
rlist.add(6)
rlist.add(4)

rlist.printList()  # rlist.head.next.next.next = rlist.head

print(rlist.get_middle())
rlist.printList()
