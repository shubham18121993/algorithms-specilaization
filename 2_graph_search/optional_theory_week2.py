"""
1) In lecture we define the length of a path to be the sum of the
lengths of its edges. Define the bottleneck of a path to be the maximum
length of one of its edges. A mininum-bottleneck path between two
vertices s and t is a path with bottleneck no larger than that of any
other s-t path. Show how to modify Dijkstra's algorithm to compute a
minimum-bottleneck path between two given vertices. The running time
should be O(mlogn), as in lecture.

2) We can do better. Suppose now that the graph is undirected. Give a 
linear-time O(m) algorithm to compute a minimum-bottleneck path
between two given vertices.
3) What if the graph is directed? Can you compute a minimum-bottleneck
path between two given vertices faster than O(mlog n)?
"""

import heapq
import math


# problem 1
def dijkstra_bottleneck_path(s, nodes, edges):
    """
    In this methodology we have modified such that instead of using some
    path, we are using min of max of each path.     Heapq contains path 
    bottleneck if we include particular edge next.
    """
    # edges dic of tail: [(head1, dis1), (head2, dis2).....]
    lst = [(elem[1], elem[0], s) for elem in edges[s]] #(dis, head, tail)
    heapq.heapify(lst)
    track = [False for _ in range(nodes)]
    keeper = {} 
    keeper[s] = (0, s) # node: (dis, parent)
    track[s-1] = True

    while not all(track) and len(lst) > 0:
        next_elem = heapq.heappop(lst)
        min_dis, node, parent = next_elem
        
        if not track[node-1]:
            track[node-1] =  True
            keeper[node] = (min_dis, parent)

            temp_edges = edges[node]
            for elem in temp_edges:
                head, dis = elem
                if not track[head-1]:
                    heapq.heappush(lst, (max(min_dis, dis), head, node))



# problem2
def bottleneck_path(start, end, edges):
    """
    This methodology is to calculate bottleneck path between two edges.
    Edges will have reverse edges too, since its an undirected graph.
    If we exclude reverse edges this methodlogy will work for directed 
    graph too.
    """
    

