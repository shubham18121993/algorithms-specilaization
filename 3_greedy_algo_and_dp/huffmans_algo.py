"""
huffman algo with heap data structure
"""
def heapify(lst):
	l = len(lst)
	l_2 = l//2 - 1
	for i in range(l_2, -1, -1):
		k = i
		while lst[k] > min(lst[k*2+1:k*2+3]):
			if min(lst[k*2+1:k*2+3]) == lst[k*2+1]:
				lst[k*2+1], lst[k] = lst[k], lst[k*2+1]
				k = k*2+1
			else:
				lst[k*2+2], lst[k] = lst[k], lst[k*2+2]
				k = k*2+2

			if k > l_2:
				break
	return lst

def insert_elem(elem):
	lst.append(elem)
	l = len(lst)
	k = l-1
	while k > 0 and lst[k] < lst[(k+1)//2-1]:
		lst[k], lst[(k+1)//2-1] = lst[(k+1)//2-1], lst[k]
		k = (k+1)//2-1
	return lst

def pop_elem():
	lst[0], lst[-1] = lst[-1], lst[0]
	elem = lst.pop()
	l =  len(lst)
	l_2 = l//2-1
	k = 0
	while k<=l_2 and lst[k] > min(lst[k*2+1: k*2+3]):
		if min(lst[k*2+1:k*2+3]) == lst[k*2+1]:
			lst[k*2+1], lst[k] = lst[k], lst[k*2+1]
			k = k*2+1
		else:
			lst[k*2+2], lst[k] = lst[k], lst[k*2+2]
			k = k*2+2

	return elem


def huffman_algo(lst):
	if len(lst) == 0:
		return 0
	while len(lst) > 1 :
		weight1, len1 = pop_elem()
		weight2, len2 = pop_elem()
		weight = weight1 + weight2
		length = max(len1, len2) + 1  # for max depth
		length = min(len1, len2) + 1  # for min depth
		insert_elem((weight, length))
	print(lst)
	return lst[0][1]


with open("../../dataset/course3/huffman.txt", 'r') as f0:
	lines = f0.readlines()

lst = []
for line in lines[1:]:
	lst.append((int(line.strip()), 0))
heapify(lst)
max_len = huffman_algo(lst)
print(max_len)


