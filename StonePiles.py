'''
Created on Apr 22, 2016

@author: Dell
'''
import itertools

def get_valid_combs(elem):
    combins= []
    for r in range(1,int(elem//2)+2):
            curr_comb=(itertools.combinations(range(1,elem),r))
            #print("combination for element {} is ".format(elem),list(curr_comb))
            [combins.append(c) for c in curr_comb if sum(c)==elem]
            
        
    #print("valid", combins)
    return combins
def find_winner(initial_num, arr=[]):
    bob=0
    alice= 0
    for index,elem in enumerate(arr):
        current= elem 
        combins = get_valid_combs(elem)
        possible_next_combs =[]
        print(combins)
        for comb in combins:
            possible_next_combs.append(get_valid_combs(comb[1]))
            
        print(possible_next_combs)
            
            
            
if __name__ == '__main__':
    find_winner(1, [8])