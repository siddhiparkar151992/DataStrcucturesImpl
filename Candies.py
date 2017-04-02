'''
Created on Apr 10, 2016

@author: Dell
'''
candies = []
valleys = []
def get_rating(i,N,arr):
    if i < 0 or i > N-1:
        return None
    return arr[i]
def get_candies(arr):
    for i,v in enumerate(range(0,len(arr)-1)):
        if get_rating(i,len(arr),arr) <= get_rating(i-1,len(arr),arr) and get_rating(i,len(arr),arr) <= get_rating(i+1,len(arr),arr):
            valleys.append(i)
    candies = [0]*len(arr) # An array of N 0s
    for valley_idx in valleys:
        try:
            candies[valley_idx] = 1
        except IndexError:
            candies= candies + [0]*len(candies)
            candies[valley_idx] = 1
    
        cur_idx = valley_idx-1
        cur_candies = 2
        while cur_idx >= 0 and arr[cur_idx] > arr[cur_idx+1]:
            candies[cur_idx] = max(candies[cur_idx], cur_candies)
            cur_idx -= 1
            cur_candies += 1
    
        cur_idx = valley_idx+1
        cur_candies = 2
        while cur_idx < len(arr) and arr[cur_idx] > arr[cur_idx-1]:
            candies[cur_idx] = max(candies[cur_idx], cur_candies)
            cur_idx += 1
            cur_candies += 1
    
if __name__ == '__main__':
    
    noc= int(input())
    score_array = []
    if noc <=(10**5) and noc >=1:
        for score in range(noc):
            score = int(input())
            score_array.append(score)
        
        print(valleys)
        pass