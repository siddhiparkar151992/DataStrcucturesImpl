'''
Created on Apr 23, 2016

@author: Dell
'''
import itertools 
def shortest_path(arr, start_node, num_of_nodes):
    to_traverse =[]
    all_paths =[]
    for r in (range(1,num_of_nodes+1)):
        if r is not 1:
            current_combinations =  itertools.combinations(range(1,num_of_nodes+1),r)
            [all_paths.append(c) for c in current_combinations]
    print(all_paths)
    possible_paths_btwn_nodes = {}
    for path in all_paths :
        curr_path = path 
        if path[0]==start_node and len(path)==2:
            for p in all_paths:
                if p[0] ==start_node and p[len(p)-1] == path[1]:
                    if path in possible_paths_btwn_nodes:
                        possible_paths_btwn_nodes[path].append(p)
                    else:
                        possible_paths_btwn_nodes[path]=[]
                        possible_paths_btwn_nodes[path].append(p)
                     
    print(possible_paths_btwn_nodes)
    
    for key,value in possible_paths_btwn_nodes.iteritems():
        valid_paths = []
        for v in value:
            combs = 
                
if __name__ == '__main__':
    arr = [[1,2,24],[1,4,20],[3,1,3],[4,3,12]]
    start_node = 1
    shortest_path(arr, start_node,4)