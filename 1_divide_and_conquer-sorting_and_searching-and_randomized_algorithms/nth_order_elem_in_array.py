"""
Deterministic Selection algorithm(Dselect): time O(n)
DSelect(array = A,length = n,order statistics = i)
1. Break A into groups of 5, sort each group 
2. C = the n/5 “middle elements” 
3. p = DSelect(C,n/5,n/10) [recursively computes median of C]
4. Partition A on around p 
5. If j = i return p 
6. If j < i return DSelect(1st part of A, j-1, i) 
7. [else if j > i] return DSelect(2nd part of A, n-j, i-j) 

Randomized Selection algorithm: Average time O(n), worse time O(n^2)

"""
import random

def get_probabilistic_median(lst, n):
	if n <= 5:
		lst.sort()
		return lst[((n+1)//2-1)]

	medians = []
	for i in range(0, n, 5):
		temp = lst[i:i+5]
		temp.sort()
		x = len(temp)
		medians.append(temp[(x+1)//2-1])
	
	n = len(medians)
	return get_probabilistic_median(medians, n)


def deterministic_selection(lst, n, i):
	if n < i or n==0:
		return "lst is smaller than ith order statistics"
	if n <=5:
		lst.sort()
		return lst[i-1]

	pivot = get_probabilistic_median(lst, n)
	
	lst_l = []
	lst_r = []
	for k in range(n):
		if lst[k] < pivot:
			lst_l.append(lst[k])
		else:
			lst_r.append(lst[k])

	len_l = len(lst_l)
	if i <= len_l:
		return deterministic_selection(lst_l, len_l, i)
	elif i == len_l+1:
		return pivot
	else:
		return deterministic_selection(lst_r, len(lst_r), i-len_l)
	

def randomized_selection(lst, n, i):
	if n < i or n==0:
		return "lst is smaller than ith order statistics"
	if n <=5:
		lst.sort()
		return lst[i-1]

	pivot = lst[0]
	
	lst_l = []
	lst_r = []
	for k in range(n):
		if lst[k] < pivot:
			lst_l.append(lst[k])
		else:
			lst_r.append(lst[k])

	len_l = len(lst_l)
	if i <= len_l:
		return deterministic_selection(lst_l, len_l, i)
	elif i == len_l+1:
		return pivot
	else:
		return deterministic_selection(lst_r, len(lst_r), i-len_l)



if __name__ == "__main__":
	lst = [x*0.5 for x in range(1, 500)]
	random.shuffle(lst)
	n = len(lst)
	i = int(input().strip())
	print(randomized_selection(lst, n, i))