"""
This file contains johnson algorithm.
Running time O(mnlogn)
"""
import numpy as np
from collections import defaultdict
import time


# reading edges from text file
with open('E:/Personal/StudyMaterial/CoursesAndSpecializations/Algorithms/dataset/course4/g3.txt', 'r') as f0:
    lines = f0.readlines()
    edges = defaultdict(list)
    node_count, edge_count = map(int, lines[0].strip().split(" "))

    for row in lines[1:]:
        tail, head, edge_cost = map(int, row.strip().split(" "))
        edges[tail].append((head, edge_cost))

"""
# Test case
node_count = 6
edges = {
    1: [(2, -2)],
    2: [(3, -1)],
    3: [(1, 4), (4, 2), (5, -3)],
    4: [],
    5: [],
    6: [(4, 1), (5, -4)],
}
"""

# single source shortest path algo, runs in O(mn)
# no negative cycle allowed
# notifies if there is any negative cycle
# negative edge costs allowed
def bellman_ford_algo(s=0, node_count=1, edges=[]):
    node_count += 1
    track = np.zeros((node_count + 1, node_count))
    for i in range(1, node_count + 1):
        for tail in range(1, node_count):
            for edge in edges[tail]:
                head, cost = edge
                track[i, head] = min(
                    track[i - 1, tail] + cost,
                    track[i - 1, head],
                    track[i, head],
                )

    for i in range(node_count):
        if track[node_count, i] != track[node_count - 1, i]:
            return "neg cycle", track
    return "no neg cycle", track[-1, :]


# converting negative to positive edges
response, points_val = bellman_ford_algo(0, node_count, edges)
print(response)

for key, val in edges.items():
    key_weight = points_val[key]
    new_val = []
    for elem in val:
        new_val.append((elem[0], elem[1] + key_weight - points_val[elem[0]]))
    edges[key] = new_val


# dijkstra algo for finding shortest path without heap data structure
def dijkstra_algo_without_heap(node_count, edges):
    distances = np.full((node_count + 1, node_count + 1), np.inf)
    for i in range(node_count + 1):
        distances[i, i] = 0

    for node in range(1, node_count + 1):
        nodes_visited = [node]
        curr = node
        while curr is not None:
            min_dis = np.inf
            curr = None
            for tail in nodes_visited:
                temp = edges[tail]
                for elem in temp:
                    head, cost = elem
                    if distances[node, head] == np.inf:
                        dis = cost + distances[node, tail]
                        if dis < min_dis:
                            curr = head
                            min_dis = dis
            if curr is not None:
                distances[node, curr] = min_dis
                nodes_visited.append(curr)
    return distances




# dijkstra algo for finding shortest path with heap data structure
# to heapify lst
def heapify(lst):
    length_2 = len(lst)//2 - 1
    for i in range(length_2, -1, -1):
        pos = i
        while lst[pos][1] > min([elem[1] for elem in lst[pos*2 + 1: pos*2 + 3]]):
            if min([elem[1] for elem in lst[pos*2 + 1: pos*2 + 3]]) == lst[pos*2 + 1][1]:
                lst[pos*2 + 1], lst[pos] = lst[pos], lst[pos*2 + 1]
                pos = pos*2 + 1
            else:
                lst[pos*2 + 2], lst[pos] = lst[pos], lst[pos*2 + 2]
                pos = pos*2 + 2
            if pos > length_2:
                break
    return lst


# to insert elem in heap
def insert(lst, elem):
    lst.append(elem)
    length = len(lst)
    pos = length-1
    while pos > 0 and lst[pos][1] < lst[(pos+1)//2-1][1]:
        lst[pos], lst[(pos+1)//2-1] = lst[(pos+1)//2-1], lst[pos]
        pos = (pos+1)//2-1
    return lst


# to delete elem in heap
def pop_elem(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    min_elem = lst.pop()
    length = len(lst)
    length_2 = length//2 - 1
    pos = 0
    while (pos<= length_2) and (lst[pos][1] > min([elem[1] for elem in lst[pos*2 + 1: pos*2 + 3]])):
        if min([elem[1] for elem in lst[pos*2 + 1: pos*2 + 3]]) == lst[pos*2+1][1]:
            lst[pos], lst[pos*2+1] = lst[pos*2+1], lst[pos]
            pos = pos*2+1
        else:
            lst[pos], lst[pos*2+2] = lst[pos*2+2], lst[pos]
            pos = pos*2+2
    return min_elem, lst


def dijkstra_algo_with_heap(node_count, edges):
    distances = np.full((node_count + 1, node_count + 1), np.inf)
    for i in range(node_count + 1):
        distances[i, i] = 0

    for node in range(1, node_count + 1):
        temp_edges = edges[node][:]
        temp_edges = heapify(temp_edges)
        while temp_edges:
            next_min, lst = pop_elem(temp_edges)
            head, cost = next_min
            if distances[node, head] >= np.inf:
                distances[node, head] = cost
                head_edges = edges[head]
                for elem in head_edges:
                    if distances[node, elem[0]] >= np.inf:
                        temp_edges = insert(temp_edges, (elem[0], cost+elem[1]))

    return distances

start_time = time.time()
matrix_with_heap = dijkstra_algo_with_heap(node_count, edges)
end_time = time.time()
print(f"time_taken: {end_time - start_time}")
print("with heap_data_structure")
print(np.amin(matrix_with_heap))

for i in range(node_count+1):
    for j in range(node_count+1):
        matrix_with_heap[i, j] = matrix_with_heap[i, j] -points_val[i] + points_val[j] 

print(np.amin(matrix_with_heap))

start_time = time.time()
matrix_without_heap = dijkstra_algo_without_heap(node_count, edges)
end_time = time.time()
print(f"time_taken: {end_time - start_time}")

print("without heap_data_structure")
print(np.amin(matrix_without_heap))

for i in range(node_count+1):
    for j in range(node_count+1):
        matrix_without_heap[i, j] = matrix_without_heap[i, j] -points_val[i] + points_val[j] 

print(np.amin(matrix_without_heap))