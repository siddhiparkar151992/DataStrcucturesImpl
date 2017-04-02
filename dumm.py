'''
Created on 25-Apr-2016

@author: siddhi
'''

import re
def check_pattern_grid(input_arr,pattern_arr):
    #print input_arr
    #print pattern_arr
    pattern_indexes= [-1]*len(pattern_arr)
    for idx,in_row in enumerate(input_arr):
        for i,patter_row in enumerate(pattern_arr):
            found_list = [(a.start(),a.end()) for a in list(re.finditer(patter_row, in_row))]
            pattern_indexes[i]
            for match in found_list:
                pattern_indexes[i] = [idx,start,end]
    print(pattern_indexes)
    generated =  (n for n in pattern_indexes)
    current = next(generated)
    ans= "YES"
    while True:
        try:
            next_elem = next(generated)
            if current ==-1 or next_elem==-1:
                ans ="NO"
                break
            if current[0] == next_elem[0] or current[0] > next_elem[0]+1:
                ans ="NO"
                break
            if current[0]+1 != next_elem[0] or current[1]!=next_elem[1] or current[2] != next_elem[2]:
                ans = "NO"
                break
        except StopIteration:
            break
        current =  next_elem
        
    #print ans
    return ans
        
                

test_cases = int(input())
if test_cases>=1 and test_cases<=5:
    for t in range(test_cases):
        first=  input().split(' ')
        R= int(first[0])
        C= int(first[1])
        input_arr = []
        pattern_arr = []
        if R>=1 and R<=1000 and C>=1 and C<=1000:
            for row in range(R):
                in_row = input()
                input_arr.append(in_row)
            pattern_rc = input().split(' ')
            r= int(pattern_rc[0])
            c= int(pattern_rc[1])
            if r>=1 and r<=R and c>=1 and c<=C:
                for row in range(r):
                    in_row = input()
                    pattern_arr.append(in_row)
        print(check_pattern_grid(input_arr,pattern_arr))