"""
This file contains kosaraju algorithm.

algorithm steps:
1) navigate through reverse graph
2) make a keeper to store values when a nodes
2) navigate through graph, start in reverse order
"""

from collections import deque, defaultdict


def kosaraju_algorithm(n, edges, reverse_edges):
    keeper = []
    stack = deque()
    explored = [False for i in range(n)]

    # traversing through reverse graph
    while not all(explored):
        while stack:
            node = stack[-1]
            if not explored[node-1]:
                flag = 0
                nodes = reverse_edges[node]
                for k in nodes:
                    if not explored[k-1] and k not in stack:
                        stack.append(k)
                        flag = 1
                        break
                
                if flag == 0:
                    node = stack[-1]
                    explored[node-1] = True
                    keeper.append(node)
                    stack.pop()

        # when stack gets empty but all nodes are not travlled
        for i in range(n):
            if not explored[i]:
                node = i+1
                stack.append(node)
                break

    scc = defaultdict(list)
    stack = deque()
    explored = [False for i in range(n)]
    count = 0


    while not all(explored):
        while stack:
            node = stack[-1]
            if not explored[node-1]:
                flag = 0
                nodes = edges[node]
                for k in nodes:
                    if not explored[k-1] and k not in stack:
                        stack.append(k)
                        flag = 1
                        break
                
                if flag == 0:
                    node = stack[-1]
                    explored[node-1] = True
                    scc[count].append(node)
                    stack.pop()
        count+=1
        # when stack gets empty but all nodes are not travlled
        for i in range(n-1, -1, -1):
            node = keeper[i]
            if not explored[node-1]:
                stack.append(node)
                break

    return scc



if __name__ == "__main__":
    edges = defaultdict(list)
    reverse_edges = defaultdict(list)

    # tail = [1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 8, 9, 9, 10, 10, 10, 11]
    # head = [3, 1, 2, 3, 7, 2, 4, 5, 4, 6, 1, 2, 8, 10, 6, 7, 11, 9]
    # n = 11

    # for i in range(18):
    #     edges[tail[i]].append(head[i])
    #     reverse_edges[head[i]].append(tail[i])
    # scc = kosaraju_algorithm(n, edges, reverse_edges)

    with open("SCC.txt", 'r') as f0:
        lines = f0.readlines()
    f0.close()
    n = 875714
    for line in lines:
        node1, node2 = map(int, line.strip().split())
        edges[node1].append(node2)
        reverse_edges[node2].append(node1)
    scc = kosaraju_algorithm(n, edges, reverse_edges)

    lst = []
    for key, value in scc.items():
        lst.append(len(value))
    lst.sort(reverse = True)
    print(lst[0:5])


