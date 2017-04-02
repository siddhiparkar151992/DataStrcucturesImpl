'''
Created on May 20, 2016

@author: Dell
'''

class PriorityQueue(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        self.queue = []
        
    def put(self, item):
        data, priority = item
        
    def is_empty(self):
        return len(self.queue)
    
    def insert(self, data):
        q = self.queue
        low = 0
        high = len(0)
    
        while low < high:
            mid = low + high // 2
            if data[0] < q[low][0]:
                hi = mid
            else:
                low = mid + 1
                
        self.queue.insert(low, data)
        
        
def test():
    pq = PriorityQueue()

    pq.put(('b', 1))
    pq.put(('a', 1))
    pq.put(('c', 1))
    pq.put(('z', 0))
    pq.put(('d', 2))

    while not pq.empty():
        print(pq.get())
