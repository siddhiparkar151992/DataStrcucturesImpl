'''
Created on Apr 13, 2016

@author: Dell
'''
import sys

def return_reduced_str(strData=None):
    allsame = False
    strLen = len(strData)
    if strData.count('a')==strLen or strData.count('b')==strLen or strData.count('c')==strLen:
        return len(strData)
    
    else:
        countArr= []
        for s in ['a','b','c']:
            countArr.append(strData.count(s))
        
        allodd= True
        alleven = True
        for count in countArr:
            if count%2 ==0:
                allodd = False
                
            elif count%2 !=0:
                alleven = False
                
        if alleven or allodd:
            return 2
        else:
            return 1
    
        
if __name__ == '__main__':
    test_cases = int(input())
    if test_cases>=1 and test_cases<=100:
        input_arr = []
        for t in range(test_cases):
            curr_input = str(input())
            if len(curr_input) >0 and len(curr_input) <= 100:
                input_arr.append(curr_input)
                
            else:
                sys.exit()
        for inp in input_arr:
            print(return_reduced_str(strData=inp))
            
    else:
        sys.exit()
    