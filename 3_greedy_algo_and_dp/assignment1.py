"""
1) greedy algorithms from lecture for minimizing 
the weighted sum of completion times
"""



with open("jobs.txt", 'r') as f0:
	jobs = f0.readlines()

priority = []

n_jobs = int(jobs[0])
for job in jobs[1:]:
	weight, length = map(int, job.strip().split(" "))
	priority.append((weight-length, weight, length))

sorted_priority = sorted(priority, key=lambda x: x[0], reverse=True)
current_time = 0
weighted_sum = 0
temp_lst = []

for elem in sorted_priority:
	if temp_lst:
		if elem[0] == temp_lst[-1][0]:
			temp_lst.append(elem)
		else:
			temp_lst = sorted(temp_lst, key=lambda x: x[1], reverse=True)
			for job in temp_lst:
				current_time += job[2]
				weighted_sum += (current_time*job[1])
			temp_lst = [elem]
	else:
		temp_lst.append(elem)


temp_lst = sorted(temp_lst, key=lambda x: x[1], reverse=True)
for job in temp_lst:
	current_time += job[2]
	weighted_sum += current_time*job[1]

print(weighted_sum)

"""
run the greedy algorithm that schedules jobs (optimally)
in decreasing order of the ratio (weight/length). In this
algorithm, it does not matter how you break ties
"""

with open("jobs.txt", 'r') as f0:
	jobs = f0.readlines()
priority = []

n_jobs = int(jobs[0])
for job in jobs[1:]:
	weight, length = map(int, job.strip().split(" "))
	priority.append((weight/length, weight, length))

sorted_priority = sorted(priority, key=lambda x: x[0], reverse=True)
current_time = 0
weighted_sum = 0

for elem in sorted_priority:
	current_time+=elem[2]
	weighted_sum += current_time*elem[1]


print(weighted_sum)

"""
Prim's algorithm
O(mn) without using data structure
O(mlogn) with heap based data structure
"""
from collections import defaultdict
import math


with open("edges.txt", 'r') as f0:
	lines = f0.readlines()

node_count, _ = map(int, lines[0].strip().split(" "))
edges = [[] for _ in range(node_count)]

for line in lines[1:]:
	node1, node2, cost = map(int, line.strip().split(" "))
	edges[node1-1].append((node2, cost))
	edges[node2-1].append((node1, cost))

def mincost(node_count, edges):
	node_travelled = [False for _ in range(node_count)]
	temp_edges = {elem[0]: elem[1] for elem in edges[0]}
	total_cost = 0
	track = 1
	node_travelled[0] = True

	while not all(node_travelled) and temp_edges:
		# print(temp_edges)
		# print(node_travelled[385])
		# print(node_travelled[227])
		min_val = math.inf
		for key, value in temp_edges.items():
			if value < min_val:
				min_val = value
				node = key

		node_travelled[node-1] = True
		print(node)
		total_cost += min_val 
		track += 1
		# print(track)
		del temp_edges[node]
		node_edges = edges[node-1]
		for elem in node_edges:
			if not node_travelled[elem[0]-1]:
				temp_edges[elem[0]] = min(elem[1], temp_edges.get(elem[0], math.inf))
	print(track)
	return total_cost

total_cost = mincost(node_count, edges)
print(f"total_cost: {total_cost}")

