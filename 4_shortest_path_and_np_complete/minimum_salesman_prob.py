"""
This is code for travelling salesman problem.
It is NP problem.
Brute force search takes O(n!) time.
Execution is in O(n^2 * 2^n) times.
"""
import math
import time
import numpy as np
from itertools import permutations

reduced_points = 26

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


with open("../../dataset/course4/tsp.txt", "r") as f0:
    lines = f0.readlines()
    locations = []

    # num_of_locations = int(lines[0].strip())
    num_of_locations = reduced_points-1
    for row in lines[1:reduced_points]:
        x, y = map(float, row.strip().split(" "))
        locations.append(Point(x, y))


def euclidean_distance(pos1, pos2):
    dis = math.sqrt(pow(pos1.x - pos2.x, 2) + pow(pos1.y - pos2.y, 2))
    return dis


distances = np.zeros((num_of_locations, num_of_locations))
for i in range(num_of_locations):
    for j in range(num_of_locations):
        if i != j:
            distances[i, j] = euclidean_distance(locations[i], locations[j])

print(distances)

def shortest_route(num_of_locations, distances):
    total_des = num_of_locations-1  # start from point 0
    array_size = pow(2, total_des)

    shortest_distance = np.full(
        (array_size, total_des), np.inf
    )

    # shortest_distance[0, 0] = 0.0

    for curr in range(1, array_size):
        bin_repr = bin(curr)
        bin_repr = list(bin_repr[2:].rjust(total_des, '0'))

        for point, val in enumerate(reversed(bin_repr)):  
            if val == "1":
                temp = bin_repr[:]
                temp[total_des -1 - point] = '0'
                prev = int("".join(temp[:]), 2)
                
                if prev == 0:
                    shortest_distance[curr, point] = distances[0, point+1]
                
                for last_point, bit in enumerate(reversed(temp)):
                    if bit == "1":
                        shortest_distance[curr, point] = min(
                            shortest_distance[curr, point],
                            shortest_distance[prev, last_point]
                            + distances[last_point+1, point+1]
                        )

            else:
                pass

    min_dis = np.inf
    for i in range(1, num_of_locations):
        if shortest_distance[-1, i-1]+ distances[i, 0] < min_dis:
            min_dis = shortest_distance[-1, i-1]+ distances[i, 0]

    return min_dis

start_time = time.time()
print("shortest_route by algo")
print(shortest_route(num_of_locations, distances))
end_time = time.time()
print(f"time taken{end_time - start_time}")


def brute_force_method(num_of_locations, distances):
    loc_points = [i for i in range(1, num_of_locations)]
    all_perm = permutations(loc_points)

    min_dis = math.inf

    for item in all_perm:
        total_dis = 0.0
        prev = 0
        for curr in item:
            total_dis += distances[prev, curr]
            prev = curr
        total_dis += distances[prev, 0]
        if total_dis < min_dis:
            min_dis = total_dis
    return min_dis


# start_time = time.time()
# print("shortest_route by brute force")
# print(brute_force_method(num_of_locations, distances))
# end_time = time.time()
# print(f"time taken{end_time - start_time}")

