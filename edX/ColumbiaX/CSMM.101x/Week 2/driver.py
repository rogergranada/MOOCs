#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
Implement 

bfs (Breadth-First Search)
dfs (Depth-First Search)
ast (A-Star Search)
ida (IDA-Star Search)
"""
import sys
import resource
from collections import deque

def bfs(start_board):
    pass

def dfs(start_board):
    pass

def ast(start_board):
    pass

def ida(start_board):
    pass


def main(algorithm, start_board):
    if algorithm == 'bfs':
        bfs(start_board)
    elif algorithm == 'dfs':
        dfs(start_board)
    elif algorithm == 'ast':
        ast(start_board)
    elif algorithm == 'ida':
        ida(start_board)
    else:
        print 'ERROR: algorithms allowed [bfs, dfs, ast, ida]'


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print 'usage: driver.py <algorithm> <list_of_numbers>'
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])


""""

d = deque()
d.append('a')
print d
d.append('b')
print d
d.append('c')
print d
d.append('d')
print d
d.popleft()
print d
d.popleft()
print d


memory = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0
print memory
#
#with open('output.txt', 'w') as fout:
#    fout.write('output')
"""

"""
#output
path_to_goal: the sequence of moves taken to reach the goal
cost_of_path: the number of moves taken to reach the goal
nodes_expanded: the number of nodes that have been expanded
fringe_size: the size of the frontier set when the goal node is found
max_fringe_size: the maximum size of the frontier set in the lifetime of the algorithm
search_depth: the depth within the search tree when the goal node is found
max_search_depth:  the maximum depth of the search tree in the lifetime of the algorithm
running_time: the total running time of the search instance, reported in seconds
max_ram_usage: the maximum RAM usage in the lifetime of the process as measured by the ru_maxrss attribute in the resource module, reported in megabytes

#example
path_to_goal: ['Up', 'Left', 'Left']
cost_of_path: 3
nodes_expanded: 10
fringe_size: 11
max_fringe_size: 12
search_depth: 3
max_search_depth: 4
running_time: 0.00188088
max_ram_usage: 0.07812500
"""
