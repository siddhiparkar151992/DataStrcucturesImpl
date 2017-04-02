'''
Created on Apr 30, 2016

@author: Dell
'''

class Node(object):
    '''
    classdocs
    '''


    def __init__(self, data):
        self.data = data
        
class LinkedList():
    
    def __init__(self):
        self.tail = None
        
    def add(self, data):
        node = Node(data)
        node.previous = self.tail
        self.tail = node
        
    def printList(self):
        temp = self.tail
        while temp:
            print(temp.data)
            temp = temp.previous
            
    
def merge_sorted_list(llist, rlist=None):
        dummyList = LinkedList()
        dummyTail = None
        if llist == None:
            return
        else:
            
            while True:                
                
            dummyList.printList()
                            
                    
llist = LinkedList()
 
# The constructed linked list is:
# 1->2->3->4->5->6->7
llist.add(1)
llist.add(3)
llist.add(5)
llist.add(7)
llist.add(9)
llist.add(11)
llist.add(13)


rlist = LinkedList()
 
# The constructed linked list is:
# 1->2->3->4->5->6->7
rlist.add(2)
rlist.add(4)
rlist.add(6)
rlist.add(8)
rlist.add(10)
rlist.add(12)
rlist.add(14)
''
merge_sorted_list(llist, rlist)
#llist.printList()   
        
    
        