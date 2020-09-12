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
import time


# using heap data structure
def heap_method(s, n, edges):
    inf = math.inf
    track = [False for _ in range(n)]
    lst = edges[s]
    track[s-1] = True
    heapq.heapify(lst)
    shortest_path = {1:0}

    while not all(track) and lst:
        next_node = heapq.heappop(lst)
        dis, node = next_node[0], next_node[1]
        if not track[node-1]:
            shortest_path[node] = dis
            track[node-1] = True
            temp_edges = edges[node]
            for elem in temp_edges:
                length, head = elem[0], elem[1]
                if not track[head-1]:
                    heapq.heappush(lst, [length+dis, head])
    return shortest_path


                       

# naive implementation
def naive_method(s, n, edges):
    track = [False for _ in range(n)]
    shortest_path = {s:0}
    track[s-1] = True
    nodes = [s]

    while not all(track):
        min_dis = math.inf
        curr = 0
        for node in nodes:
            temp_edges = edges[node]
            for edge in temp_edges:
                dist, head = edge[0], edge[1]
                if not track[head-1]:
                    total_dis = dist + shortest_path[node]
                    if total_dis < min_dis:
                        min_dis = total_dis
                        curr = head
        track[curr-1] = True
        nodes.append(curr)
        shortest_path[curr] = min_dis
    return shortest_path


with open("../../dataset/course2/dijkstraData.txt", 'r') as f0:
    lines = f0.readlines()
f0.close()

edges = defaultdict(list)
for line in lines:
    n = 200
    lst = line.strip().split()
    key = int(lst[0])
    value = [[int(elem.strip().split(',')[1]), 
        int(elem.strip().split(',')[0])]
    for elem in lst[1:]]
    edges[key] = value

start = time.time()
shortest_path = naive_method(1, n, edges)
end = time.time()
print(f"\nnaive_method: {end - start}\n")
print(shortest_path)

start = time.time()
shortest_path = heap_method(1, n, edges)
end = time.time()
print(f"\nheap_method: {end - start}\n")
print(shortest_path)
