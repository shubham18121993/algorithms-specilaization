"""
This script contains dijkstra algorithm.
Algorithm is used to calculate shortest path from a vertex
to all other nodes.
Algorithm works on greedy search.
Naive way takes O(m*n) times.
With heap data structure it can be done in O(m*logn)
This implementation is with heap data structure
"""

import heapq
import math
from collections import defaultdict

"""
# using heap data structure: TO DO
def get_shortest_path(s, n, edges):
    inf = math.inf
    nodes = [[inf, i] for i in range(1, n+1)]
    nodes[0][0] = 0
    heapq.heapify(nodes)
    shortest_path = {}

    for _ in range(n):
        shortest_path[nodes[0][1]] = nodes[0][0]
        distances = edegs[nodes[0][1]]
        heapq.heappop(nodes)
        for elem in distances:
            key = elem[0]
            val = elem[1]
"""                         

# naive implementation
def get_shortest_path(s, n, edges):
    track = [False for _ in range(n)]
    shortest_path = {1:0}
    track[0] = True
    nodes = [1]

    while not all(track):
        min_dis = math.inf
        curr = 0
        for node in nodes:
            temp_edges = edges[node]
            for edge in temp_edges:
                head, dist = edge[0], edge[1]
                if not track[head-1]:
                    total_dis = dist + shortest_path[node]
                    if total_dis < min_dis:
                        min_dis = total_dis
                        curr = head
        track[curr-1] = True
        nodes.append(curr)
        shortest_path[curr] = min_dis
    return shortest_path

with open("dijkstraData.txt", 'r') as f0:
    lines = f0.readlines()
f0.close()

edges = defaultdict(list)
for line in lines:
    n = 200
    lst = line.strip().split()
    key = int(lst[0])
    value = [list(map(int, elem.strip().split(","))) for elem in lst[1:]]
    edges[key] = value
shortest_path = get_shortest_path(1, n, edges)
print(shortest_path)
