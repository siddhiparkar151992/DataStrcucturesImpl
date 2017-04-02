'''
Created on May 14, 2016

@author: Dell
'''

import sys

class Stack(object):
    '''
    classdocs
    '''

    
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


def reverse_str(input_str):
    out_str = ''
    s = Stack()
    [s.push(i) for i in input_str]
    while s.size() != 0:
        out_str += str(s.pop())
    return out_str
def main():
    test = int(input())
    arr = []
    if test >= 1 and test <= 1000:
        opening = ['(', '{', '[', ')', '}', ']']
        for t in range(0, test):
            in_str = input()
            if len(in_str) >= 1 and len(in_str) <= 1000:
                valid = []
                [valid.append(i) for i in in_str if i in opening]
                if len(valid) == len(in_str):
                    
                    arr.append(in_str)
            
        for a in arr:
            print(balanced_paratheses(a))
def balanced_paratheses(string):
    s = Stack()
    opening = ['(', '{', '[']
    closing = [')', '}', ']']
    char = string[0]
    for char in string:
        
        print("checking char ", char)
        if char in opening:
            print("char in openng")
            s.push(char)
        elif char in closing:
            if s.size() == 0:
                return 'NO'
            stackPop = s.pop()
            bracket = opening[closing.index(char)]
            if stackPop != bracket:
                return 'NO'
                
                
    if s.size() == 0: 
        return 'YES'
    else:
        return 'NO'
    
def find_greater_next(arr):
    st = Stack()
    st.push(arr[0])
    for i in range(1, len(arr)):
        next = arr[i]
        if not st.is_empty():
            stack_elem = st.pop()
            while stack_elem < next:
                print(stack_elem, ' ', next)
                if st.is_empty():
                    break
                stack_elem = st.pop()
            if next < stack_elem:
                st.push(stack_elem)
        st.push(next)
 
    while st.is_empty() == False:
        element = st.pop()
        next = -1
        print(str(element) + " " + str(next))

n = int(input())
arr = [int(i) for i in input().split(' ')]
print(arr)
find_greater_next(arr)
