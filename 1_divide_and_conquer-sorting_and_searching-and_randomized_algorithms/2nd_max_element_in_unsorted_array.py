"""
Problem Statement:
You are given as input an unsorted array of n distinct numbers, where n
is a power of 2. Give an algorithm that identifies the second-largest
number in the array, and that uses at most n +logn(base2)-2
comparisons.
"""

"""
Logic
n/2 -1  and n/2-1

a1, a2 (a1 > a2) 
b1, b2 (b1 > b2)  (3 comparisons)
n = 2^m
n th level n/2 comp

"""

from collections import defaultdict
import random


# My solution not so elegant needs
arr_dic = defaultdict(list)


def get_second_max(arr):
	global arr_dic
	if len(arr) == 2:
		if arr[0] > arr[1]:
			values = arr_dic[arr[0]]
			return max(max(values) , arr[1])
		else:
			values = arr_dic[arr[1]]
			return max(max(values) , arr[0])

	sub_array = []

	for i in range(0, len(arr), 2):
		if arr[i] > arr[i+1]:
			arr_dic[arr[i]].append(arr[i+1])
			sub_array.append(arr[i])
		else:
			arr_dic[arr[i+1]].append(arr[i])
			sub_array.append(arr[i+1])
	return get_second_max(sub_array)

# from discussion forum
def get_max(arr):
	n = len(arr)
	if n == 2:
		if arr[0] > arr[1]:
			return arr[0], [arr[1]]
		else:
			return arr[1], [arr[0]]

	elif n>2:
		max1, comp1 = get_max(arr[:n//2])
		max2, comp2 = get_max(arr[n//2:])
		if max1 > max2:
			return max1, comp1+[max2]
		else:
			return max2, comp2+[max1]

	else:
		return arr[0], []

if __name__ == "__main__":
	arr = [x for x in range(2**20)]
	random.shuffle(arr)
	max1, comp = get_max(arr)
	max2, _ = get_max(comp)
	print(max2)
