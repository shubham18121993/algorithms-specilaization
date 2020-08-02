"""
"""

# k- means clustering algorithm
class Node():
	def __init__(self, val):
		self.child = val
		self.parent = val
	
	def parent(self, val):
		self.parent = val


with open('clustering1.txt', 'r') as f0:
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
		parent = parent_list[parent-1].parent
	return parent



def clustering(edges, clusters, node_count):
	track_parent = [Node(i+1) for i in range(node_count)]
	edges.sort()

	print(edges[-10:])

	for elem in edges:
		cost, node1, node2 = elem
		root1, root2 = get_root(node1, track_parent), get_root(node2, track_parent)
		if root1 == root2:
			pass
		else:
			track_parent[root1-1].parent = root2
			node_count -= 1
		if node_count<=clusters:
			break
	return cost

print(clustering(edge_costs, CLUSTERS, node_count))


# big clusters

with open('clustering_big.txt', 'r') as f0:
	lines = f0.readlines()

edge_costs = []
node_count, bit_per_node = map(int, lines[0].strip().split(" "))

for line in lines[1:]:
	node = line.strip()
	edge_costs.append((cost, node1, node2))

