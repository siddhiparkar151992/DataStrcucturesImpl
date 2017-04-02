'''
Created on Apr 9, 2016

@author: Dell
'''

if __name__ == '__main__':
    dimension = int(input())
    arr =[]
    lr_sum = 0
    rl_sum = 0
    for i in range(0,dimension):
        row = input().split()
        row = [int(v) for v in row]
        lr_sum += row[i]
        rl_sum += row[-int(i)-1]
    print(abs(lr_sum-rl_sum))