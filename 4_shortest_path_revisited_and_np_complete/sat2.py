"""
Problem has been solved using 2 methods.
1) kosaraju algorithm
    Steps:
    a) navigate through reverse graph
    b) make a keeper to store values of nodes
    c) navigate through the graph, traverse in reverse order of nodes
2) Papadimitriou's algorithm
    a) Runs in (n^2*logn) times
    b) Probability of accuracy (1 - 1/n)
"""

from collections import deque, defaultdict
import time


for i in range(1, 7):
    # read data
    with open("../../dataset/course4/2sat"+str(i)+".txt", 'r') as f0:
        lines = f0.readlines()
        node_count = int(lines[0].strip())
        edges = defaultdict(list)
        reverse_edges = defaultdict(list)
        conjuctions = []
        for row in lines[1:]:
            node1, node2 = map(int, row.strip().split(" "))
            conjuctions.append((node1, node2))
            edges[-1*node1].append(node2)
            edges[-1*node2].append(node1)
            reverse_edges[node1].append(-1*node2)
            reverse_edges[node2].append(-1*node1)

    # kosaraju algorithm: we will need to create edges for this
    # each condition will have 2 edges for (A or B)
    # edges: (A' -> B) or (B' -> A)
    def get_nodeval(pos):
        node = pos//2 + 1
        if pos%2 == 1:
            node = -1*node
        return node


    def get_posval(node):
        pos = abs(node)*2 - 2 + int(node < 0)
        return pos


    def kosaraju_algorithm(node_count, edges, reverse_edges):
        total_nodes = 2*node_count
        keeper = []
        stack = deque()
        track = 0
        # nodes in explored 1->0, -1->1, 2->2, -2->3, 3->4
        explored = [False for _ in range(total_nodes)]

        while not all(explored):
            while stack:
                node = stack[-1]
                pos = get_posval(node)

                if not explored[pos]:
                    flag = False
                    node_edges = reverse_edges[node]
                    
                    for head in node_edges:
                        head_pos = get_posval(head)
                        if not(explored[head_pos]) and head not in stack:
                            stack.append(head)
                            flag = True
                            break
                    
                    if not flag:
                        node = stack[-1]
                        keeper.append(node)
                        pos = get_posval(node)
                        explored[pos] = True
                        stack.pop()

            for pos in range(total_nodes):
                if not explored[pos]:
                    node = get_nodeval(pos)
                    stack.append(node)
                    break

        print('part1_done')
        scc = defaultdict(list)
        stack = deque()
        explored = [False for _ in range(total_nodes)]
        count = 0

        while not all(explored):
            while stack:
                node = stack[-1]
                pos = get_posval(node)
                
                if not explored[pos]:
                    flag = False
                    node_edges = edges[node]
                    
                    for head in node_edges:
                        head_pos = get_posval(head)
                        if not(explored[head_pos]) and head not in stack:
                            stack.append(head)
                            flag = True
                            break
                    
                    if not flag:
                        node = stack[-1]
                        pos = get_posval(node)
                        explored[pos] = True
                        scc[count].append(node)
                        stack.pop()
            count +=1


            for i in range(total_nodes-1, -1, -1):
                node = keeper[i]
                if not explored[get_posval(node)]:
                    stack.append(node)
                    break
        return scc

    start_time = time.time()
    cycle = False

    scc = kosaraju_algorithm(node_count, edges, reverse_edges)

    for _, val in scc.items():
        sorted_lst = sorted(val)
        i = 0
        j = len(val) -1
        while i != j and sorted_lst[i] < 0:
            if abs(sorted_lst[i]) == sorted_lst[j]:
                cycle = True
                break
            elif abs(sorted_lst[i]) > sorted_lst[j]:
                i+=1
            else:
                j-=1
        if cycle:
            break

    end_time = time.time()
    print(f"problem {i} satisfiable: {cycle}")
    print(f"time_taken for problem {i} is: {end_time - start_time}")