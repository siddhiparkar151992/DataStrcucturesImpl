'''
Created on Apr 9, 2016

@author: Dell
'''

import sys
import copy
raw_arr=[]
max_s =0

 
def find_max_sub_arr(a,size):
     
    max_so_far = 0
    max_ending_here = 0
    non_cons =0
    for i in range(0, size):
        
        a[i] = int(a[i])
        if a[i] <= 10**4 and a[i]>= -(10**4):
            if a[i] > 0:
                non_cons +=a[i]
            max_ending_here = max_ending_here + a[i]
            if max_ending_here < 0:
                max_ending_here = 0
            elif (max_so_far < max_ending_here):
                max_so_far = max_ending_here
        else:
            sys.exit()    
    return [max_so_far, non_cons]
        
if __name__ == '__main__':
    test_cases = int(input())
    if test_cases >=1 and test_cases <= 10:
        in_arr =[]
        for tc in range(test_cases):
            arr = []
            in_arr_len = input()
            in_arr_len = int(in_arr_len)
            if in_arr_len >=1 and in_arr_len <= 1000000:
                arr = input().split()
                in_arr.append(arr)
        for arr in in_arr:
            consecutive_sum_arr = []
            sum = find_max_sub_arr(copy.deepcopy(arr), len(arr))  
            print(sum[0],sum[1])
    else:
        sys.exit()
        