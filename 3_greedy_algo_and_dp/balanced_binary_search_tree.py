import numpy as np


weights = [0.2, 0.05, 0.17, 0.1, 0.2, 0.03, 0.25]
n = len(weights)
track = np.full((n, n), np.inf)

for i in range(n):
    track[i, i] = weights[i]

for s in range(n):
    for i in range(0, n-s):
        
        pi =  sum(weights[i: i+s+1])
        
        for pivot in range(i, i+s+1):
            
            if i > pivot-1:
                left_tree = 0
            else:
                left_tree= track [i, pivot-1]
            
            if pivot+1 > i+s:
                right_tree = 0
            else:
                right_tree = track[pivot+1, i+s]

            track [i, i+s] = min(track [i, i+s], 
                pi+ left_tree + right_tree)


print(track)


