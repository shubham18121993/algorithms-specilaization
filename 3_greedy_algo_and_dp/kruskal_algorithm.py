# to do kruskal algorithm
with open("../../dataset/course3/edges.txt", 'r') as f0:
    lines = f0.readlines()

node_count, _ = map(int, lines[0].strip().split(" "))
edges = []

class Node():
    def __init__(self, val):
        self.parent = val
        self.val = val
        self.depth = 0

for line in lines[1:]:
    node1, node2, cost = map(int, line.strip().split(" "))
    edges.append((cost, node1, node2))

edges.sort()


def get_root(node, lst):
    node_traverse = []
    while lst[node].val != lst[node].parent:
        node_traverse.append(node)
        node = lst[node].parent

    return lst[node], node_traverse

def change_parent(nodes, parent_track, parent_val):
     for elem in nodes:
        parent_track[elem].parent = parent_val


def kruskal_with_union_find(node_count, edges):
    parent_track = [Node(i) for i in range(node_count+1)]
    parent_count = node_count
    total_cost = 0

    for edge in edges:
        if parent_count <= 1:
            break
       
        cost, node1, node2 = edge
        root1, root1_nodes = get_root(node1, parent_track)
        root2, root2_nodes = get_root(node2, parent_track)
        
        if root1.parent == root2.parent:
            pass
        else:
            parent_count -= 1
            total_cost += cost
            if root1.depth == root2.depth:
                parent_track[root1.val].depth += 1
                parent_track[root2.val].parent = root1.parent
                change_parent(root2_nodes, parent_track, root1.parent)

            elif root1.depth > root2.depth:
                parent_track[root2.val].parent = root1.parent
                change_parent(root2_nodes, parent_track, root1.parent)


            else:
                parent_track[root1.val].parent = root2.parent
                change_parent(root1_nodes, parent_track, root2.parent)

    return total_cost


total_cost = kruskal_with_union_find(node_count, edges)
print(f"total_cost: {total_cost}")