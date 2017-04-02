'''
Created on May 19, 2016

@author: Dell
'''

class Queue(object):
    '''
    classdocs
    '''


    def __init__(self):
        
        self.first = ()
    def enqueue(self, item):
        node = [item, ()]
        print('self first is ', self.first, ' node is ', node)
        if self.first:
            self.last[1] = node
        else:
            self.first = node
            
        self.last = node
        
    def dequeue(self, n=-1):
        node = self.first
        print('dequee node is ', node)
        self.first = node[1]
        return node[0]
    
a = Queue()
a.enqueue(10)
a.enqueue(20)
print(a.dequeue(0))
print(a.dequeue(0))
a.enqueue(5)
print(a.dequeue(0))
    
    
    
    
        
    
        
        
        
