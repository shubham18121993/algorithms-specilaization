"""
Prim's algorithm
O(mn) without using data structure
O(mlogn) with heap based data structure
"""
from collections import defaultdict
import math
import heapq


with open("../../dataset/course3/edges.txt", 'r') as f0:
	lines = f0.readlines()

node_count, _ = map(int, lines[0].strip().split(" "))
edges = [[] for _ in range(node_count)]

for line in lines[1:]:
	node1, node2, cost = map(int, line.strip().split(" "))
	edges[node1-1].append((node2, cost))
	edges[node2-1].append((node1, cost))

def prim_without_heap(node_count, edges):
	node_travelled = [False for _ in range(node_count)]
	temp_edges = {elem[0]: elem[1] for elem in edges[0]}
	total_cost = 0
	track = 1
	node_travelled[0] = True

	while not all(node_travelled) and temp_edges:
		min_val = math.inf
		for key, value in temp_edges.items():
			if value < min_val:
				min_val = value
				node = key

		node_travelled[node-1] = True
		total_cost += min_val 
		track += 1
		# print(track)
		del temp_edges[node]
		node_edges = edges[node-1]
		for elem in node_edges:
			if not node_travelled[elem[0]-1]:
				temp_edges[elem[0]] = min(elem[1], temp_edges.get(elem[0], math.inf))

	return total_cost

total_cost = prim_without_heap(node_count, edges)
print(f"total_cost without heap: {total_cost}")


def prim_with_heap(node_count, edges):
	node_travelled = [False for _ in range(node_count)]
	temp_edges = [(elem[1], elem[0]) for elem in edges[0]]
	total_cost = 0.0

	heapq.heapify(temp_edges)
	node_travelled[0] = True  # For first node

	while not all(node_travelled) and temp_edges:
		cost, head = heapq.heappop(temp_edges)
		if not node_travelled[head-1]:
			total_cost += cost
			node_travelled[head-1] = True
			for elem in edges[head-1]:
				if not node_travelled[elem[0]-1]:
					heapq.heappush(temp_edges, (elem[1], elem[0]))

	return total_cost

total_cost = prim_with_heap(node_count, edges)
print(f"total_cost with heap: {total_cost}")



