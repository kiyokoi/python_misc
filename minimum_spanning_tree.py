# -*- coding: utf-8 -*-
"""
Given an undirected graph G, find the minimum spanning tree within G. A 
minimum spanning tree connects all vertices in a graph with the smallest 
possible total weight of edges. Your function should take in and return an 
adjacency list structured like this:
{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
Vertices are represented as unique strings.
"""

from heapq import heappop, heappush
### Question3 main code
def mst(G):
    # initialize visited vertices list and output dict    
    visited = []
    tree = {}
    try:
        # initialize priority queue (weight, edge1, edge2)
        queue = [(0, None, 'A')]
        while queue:
            weight, e1, e2 = heappop(queue) #edge with smallest weight
            if e2 in visited: continue # skip vertices already visited
            visited.append(e2)
            if e1 is None:
                pass
            elif e1 in tree:
                tree[e1].append((e2, weight))
            else:
                tree[e1] = [(e2, weight)]
            for item in (G[e2]): #adjacent vertices and weights
                v = item[0]
                w = item[1]
                heappush(queue, (w, e2, v))
        if tree != {}:
            return tree
        else:
            print "Invalid inputs!"
    except KeyError:
        print "Invalid inputs!"
    
### Question3 test code
# Case 1: good example
G = {'A': [('B', 2)],\
     'B': [('A', 2), ('C', 5)],\
     'C': [('B', 5)]} 
print mst(G)
# Expected output is {'A': [('B', 2)], 'B': [('C', 5)]}

# Case 2: missing dictionary key
G = {'': [('B', 2)],\
     'B': [('A', 2), ('C', 5)],\
     'C': [('B', 5)]} 
print mst(G)
# Expected output is an error message: "Invalid inputs!"

# Case 3: emptry minimal spanning tree
G = {'A': [],\
     'B': [('A', 2), ('C', 5)],\
     'C': [('B', 5)]} 
print mst(G)
# Expected output is an error message: "Invalid inputs!"