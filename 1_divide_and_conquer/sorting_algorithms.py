"""
This module contains all the sorting algorithsm

1) Bubble sort
Bubble Sort is the simplest sorting algorithm that works by repeatedly
swapping the adjacent elements if they are in wrong order.
algorithm this way identifies the largest elem first

2) Insertion sort
Insertion sort is a simple sorting algorithm that works the way we sort
playing cards in our hands. 
first x elements are sorted

3) Selection sort
The selection sort algorithm sorts an array by repeatedly finding the
minimum element (considering ascending order) from unsorted part and 
putting it at the beginning.

4) Merge sort: divide and conquer algorithm
It divides input array in two halves, calls itself for the two halves
The merge() function is used for merging two halves.

5) Quick sort: divide and conquer algorithm
Average time is n*logn. Worse time is O(n*n).
Algorithm require no additional space
Randomized algorithm means implementation order will be different with
same list. Choose random pivot to improve algorithms

6) HeapSort


7) BucketSort
8) CoutingSort
9) RadixSort
"""
import random
import time

def bubble_sort(lst):
	n = len(lst)

	for i in range(n):
		for j in range(n-i-1):
			if lst[j] > lst[j+1]:
				lst[j], lst[j+1] = lst[j+1], lst[j]

	return lst


def insertion_sort(lst):
	n = len(lst)

	for i in range(1, n):
		elem = lst[i]
		j = 0
		for j in range(i-1, -1, -1):
			if elem < lst[j]:
				lst[j+1], lst[j] = lst[j], elem
			else:
				break
	return lst


def merge_sort(lst):
	n = len(lst)
	if n <= 1:
		return lst

	lst1 = merge_sort(lst[:n//2])
	lst2 = merge_sort(lst[n//2:])

	i = 0
	j = 0
	sorted_lst = []

	while (i < (n//2)) and (j < (n - n//2)):
		if lst1[i] < lst2[j]:
			sorted_lst.append(lst1[i])
			i+=1
		else:
			sorted_lst.append(lst2[j])
			j+=1

	for k in range(i, n//2):
		sorted_lst.append(lst1[k])

	for k in range(j, (n - n//2)):
		sorted_lst.append(lst2[k])

	return sorted_lst


def quick_sort(lst):
	n = len(lst)
	if n <= 1:
		return lst

	pivot = lst[0]
	track = 1
	for i in range(1, n):
		if lst[i] < pivot:
			lst[track], lst[i] = lst[i], lst[track]
			track+=1
	lst[0], lst[track-1] = lst[track-1], lst[0]
	return quick_sort(lst[:track-1]) + [pivot] + quick_sort(lst[track:])


def get_min(lst):
	elem = lst[0]
	index = 0
	for i in range(1, len(lst)):
		if lst[i] < elem:
			index = i
			elem = lst[i]
	return index

def selection_sort(lst):
	n = len(lst)

	for i in range(n):
		index = get_min(lst[i:])
		lst[index+i], lst[i] = lst[i], lst[i+index]
	return lst
		


if __name__ == "__main__":
	lst = [x for x in range(10000)]
	lst2 = [x for x in range(10000)]

	for sort_type in ["insertion", "quick", "merge", "bubble", "selection"]:
		flag = False
		start_time = time.time()
		random.shuffle(lst)
		if sort_type == "insertion":
			sorted_lst = insertion_sort(lst)

		if sort_type == "bubble":
			sorted_lst = bubble_sort(lst)

		if sort_type == "quick":
			sorted_lst = quick_sort(lst)

		if sort_type == "merge":
			sorted_lst = merge_sort(lst)

		if sort_type == "selection":
			sorted_lst = selection_sort(lst)

		end_time = time.time()
		if sorted_lst == lst2:
			flag = True
		print(f"{sort_type} Sort: {flag}. Time:{end_time - start_time}")

