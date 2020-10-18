import numpy as np


weights = [0.2, 0.05, 0.17, 0.1, 0.2, 0.03, 0.25]
n = len(weights)
track = np.full((n, n), np.inf)

for i in range(n-1, -1, -1):
	for j in range(i):
		i_2 = i - j
		for k in range(n -i):

