"""
Ford Warshall algorithm
To detect negative cycle we can use 1 run of bellman's algorithm
code is written assuming there are no negative cycles
"""
import numpy as np

# reading edges from text file
with open('../../dataset/course4/g3.txt', 'r') as f0:
    lines = f0.readlines()
    node_count, edge_count = map(int, lines[0].strip().split(" "))
    edges = np.full((node_count, node_count), np.inf)

    for i in range(node_count):
        edges[i, i] = 0.0

    for row in lines[1:]:
        tail, head, edge_cost = map(int, row.strip().split(" "))
        edges[tail-1, head-1] = edge_cost


def ford_warshall_algorithm(node_count, edges):
    distances = np.full((2, node_count, node_count), np.inf)
    distances[0, :, :] = edges 

    # k: number of nodes, i: tail, h: head
    for k in range(1, node_count):
        k2 = k % 2
        k1 = (k+1) % 2
        for i in range(node_count):
            for j in range(node_count):
                distances[k2, i-1, j-1] = min(
                    distances[k1, i-1, j-1],
                    distances[k1, i-1, k-1] + edges[k-1, j-1]
                )

    return np.amin(distances[k2, :, :])


print(ford_warshall_algorithm(node_count, edges))
