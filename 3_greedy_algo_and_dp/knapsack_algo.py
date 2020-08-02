"""
This file has 2 implementation of knapsack.
One is not space efficient so we can track back points.
knapsack_track
Other is space efficient but we can't track back the points.
knapsack_space
Also, both the solution uses O(n^2) times, so efficient process.
"""
import numpy as np
import pandas as pd


def knapsack_track(lst, max_weight, n):
	track = np.zeros((max_weight+1, n+1))
	for v in range(1, n+1):
		vertex, weight = lst[v-1]
		for w in range(1, max_weight+1):
			if weight > w:
				track[w, v] = track[w, v-1]
			else:
				residual_weight = w - weight
				track[w, v] = max(track[w, v-1], vertex+track[residual_weight, v-1])
	# return pd.DataFrame(track)
	return track[-1, -1]

def knapsack_space(lst, max_weight, n):
	track = np.zeros((max_weight+1, 2))
	for v in range(1, n+1):
		vertex, weight = lst[v-1]
		j = v%2
		i = 1-j
		for w in range(1, max_weight+1):
			if weight > w:
				track[w, j] = track[w, i]
			else:
				residual_weight = w - weight
				track[w, j] = max(track[w, i], vertex+ track[residual_weight, i])
	# return pd.DataFrame(track)
	return track[-1, j]



with open("knapsack1.txt", 'r') as f0:
	lines = f0.readlines()

lst_small = []
max_weight, n = map(int, lines[0].strip().split(" "))
# n = 46
for line in lines[1:n+1]:
	vertex, weight = map(int, line.strip().split(" "))
	lst_small.append((vertex, weight))

print(knapsack_track(lst_small, max_weight, n))


with open("knapsack_big.txt", 'r') as f1:
	lines = f1.readlines()

lst_big = []
max_weight, n = map(int, lines[0].strip().split(" "))
# n = 46
for line in lines[1:n+1]:
	vertex, weight = map(int, line.strip().split(" "))
	lst_big.append((vertex, weight))

print(knapsack_space(lst_big, max_weight, n))

# knapsack_track(lst, max_weight, n).to_excel("text1.xlsx")
# knapsack_space(lst, max_weight, n).to_excel("text2.xlsx")
