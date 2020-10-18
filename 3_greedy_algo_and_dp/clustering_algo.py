"""
"""
from collections import defaultdict
from collections import deque

"""
# k- means clustering algorithm
class Node():
    def __init__(self, val):
        self.child = val
        self.parent = val
    
    def parent(self, new_val):
        self.parent = new_val


with open('../../dataset/course3/clustering1.txt', 'r') as f0:
    lines = f0.readlines()

edge_costs = []
node_count = int(lines[0].strip())
for line in lines[1:]:
    node1, node2, cost = map(int, line.strip().split(" "))
    edge_costs.append((cost, node1, node2))

CLUSTERS = 4

def get_root(node, parent_list):
    child = parent_list[node-1].child
    parent = parent_list[node-1].parent

    while child != parent:
        child = parent
        parent = parent_list[child-1].parent
    return parent



def clustering(edges, clusters, node_count):
    track_parent = [Node(i+1) for i in range(node_count)]
    edges.sort()

    for i, elem in enumerate(edges):
        cost, node1, node2 = elem
        root1, root2 = get_root(node1, track_parent), get_root(node2, track_parent)
        if root1 == root2:
            pass
        else:
            track_parent[root1-1].parent = root2
            node_count -= 1
        if node_count < clusters:
            print(edges[i-5: i+20])
            break
    return cost, edges[i]

# print(clustering(edge_costs, CLUSTERS, node_count))
"""

# big clusters

with open('../../dataset/course3/clustering_big.txt', 'r') as f0:
    lines = f0.readlines()

hashmap = defaultdict(set)
lst = []

node_count, bit_per_node = map(int, lines[0].strip().split(" "))


for index, row in enumerate(lines[1:]):
    val = int("".join(row.strip().split(" ")[:]), 2)
    hashmap[val].add(index)
    lst.append(val)

# tests = ['111000', '000000', '000001',  '111011', '111101', '000101']
# bit_per_node = 6
# node_count = 6


# for index, row in enumerate(tests):
#     val = int(row, 2)
#     hashmap[val].add(index)
#     lst.append(val)



class Node():
    def __init__(self, val):
        self.val = val
        self.parent = val
        self.depth = 0


def get_root(node, lst):
    node_traverse = []
    while lst[node].val != lst[node].parent:
        node_traverse.append(node)
        node = lst[node].parent

    return lst[node], node_traverse

def change_parent(nodes, parent_track, parent_val):
     for elem in nodes:
        parent_track[elem].parent = parent_val



def big_clustering(node_count, bit_per_node, hashmap, lst):
    node_roots = [Node(i) for i in range(node_count)]
    bit_shift = [1 << i for i in range(bit_per_node)]  # shift by 1
    bit_shift.append(0)  # shift by 0

    # bits2 = []
    
    # shift by 2
    for i in range(bit_per_node):
        for j in range(i, bit_per_node):
            if i != j:
                bit_shift.append(bit_shift[i]^bit_shift[j])

    print(len(set(bit_shift)))
    print(bit_shift)

    for elem in lst:
        for bits in bit_shift:
            temp = elem^bits
            temp_val = hashmap.get(temp, set())
            for val in temp_val:
                hashmap[elem].add(val)


    for key, val in hashmap.items():
        if len(val) >= 2:
            temp_list = list(val)
            node = temp_list[0]
            root_node, node_traverse = get_root(temp_list[0], node_roots)
            for elem in temp_list[1:]:
                root_elem, elem_traverse = get_root(elem, node_roots)
                if root_elem.parent == root_node.parent:
                    pass
                else:
                    if root_elem.depth < root_node.depth:
                        node_roots[root_elem.val].parent = root_node.parent
                        change_parent(elem_traverse, node_roots, root_node.parent)

                    elif root_elem.depth > root_node.depth:
                        node_roots[root_node.val].parent = root_elem.parent
                        change_parent(node_traverse, node_roots, root_elem.parent)
                        node = elem
                        root_node = root_elem

                    else:
                        node_roots[root_elem.val].parent = root_node.parent
                        node_roots[root_elem.val].depth += 1
                        change_parent(elem_traverse, node_roots, root_node.parent) 

    parents_set = set()
    for node in node_roots:
        root_node, node_traverse = get_root(node.val, node_roots)
        change_parent(node_traverse, node_roots, root_node.parent)
        parents_set.add(root_node.parent)

    return (len(parents_set))

"""
    # parent = 1
    # i = 0
    # stack = deque()
    # while not all(nodes_travelled):
    #     if not stack:
    #         parent +=1
    #         if not all(nodes_travelled):
    #             for j in range(i, node_count):
    #                 if not nodes_travelled[j]:
    #                     for elem in hashmap[lst[i]]:
    #                         stack.append(elem)
    #                     break
    #             i = j

    #     while stack:
    #         node = stack.popleft()
    #         if nodes_travelled[node]:
    #             pass
    #         else:
    #             node_roots[node].parent = parent
    #             nodes_travelled[node] = True
    #             temp = hashmap[lst[node]]
    #             for elem in temp:
    #                 if not nodes_travelled[elem]:
    #                     stack.append(elem)

    #     parent += 1
    # return parent
"""
print(big_clustering(node_count, bit_per_node, hashmap, lst))
# print(hashmap)
        
