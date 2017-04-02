'''
Created on May 16, 2016

@author: Dell
'''

class Stack(object):
    '''
    classdocs
    '''
    auxilaryStack = None
    
    def __init__(self):
        self.stack = []
        
    
    def is_empty(self):
        return self.stack == []
    
    def push(self, elm):
        self.stack.append(elm)
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[len(self.stack) - 1]
    
    def size(self):
        return len(self.stack)
    
    def push_sort(self, elem):
        
        self.stack.append(elem)
        if self.auxilaryStack == None:
            self.auxilaryStack = Stack()
        if not self.auxilaryStack.is_empty():
            min = self.auxilaryStack.pop()
            print('current min is ', min)
            if min > elem:
                print('elem greater than auxStack', min, elem)
                self.auxilaryStack.push(elem)
            else:
                print('elem less than auxStack', min, elem)
                
                self.auxilaryStack.push(min)
        else:
            
            self.auxilaryStack.push(elem)
    def sort_insert(self, elem):
        if self.is_empty() or elem > self.peek():
            print(elem, ' is greater than top')
            self.push(elem)
            print('stack is ', self.stack)
        else:
            temp = self.pop()
            print(elem, ' is less than top ', temp)
            self.sort_insert(elem)
            print('adding ', temp, ' back to stack')
            self.push(temp)
            print('stack after adding iytem back is ', self.stack)
    def sort(self):
        if not self.is_empty():
            item = self.pop()
            self.sort()
            self.sort_insert(item)
    def get_min(self):
        if self.auxilaryStack.is_empty():
            return -1
        else:
            return self.auxilaryStack.peek()   
s = Stack()
s.push_sort(4)
s.push_sort(6)
s.push_sort(3)
s.push_sort(8)
s.push_sort(1)
s.push_sort(7)
# s.sort()
print(s.get_min())

# print(s.stack)
