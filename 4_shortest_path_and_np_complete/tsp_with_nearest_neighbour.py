"""
This solves the travelling salesman problem for bigger dataset.
Algorithm finds the next nearest neighbour and visit that.
Computational time taken is 
"""
import math
import numpy as np


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

with open("../../dataset/course4/nn.txt", 'r') as f0:
    lines = f0.readlines()
    locations = []
    num_of_cities = int(lines[0].strip())
    for coordinates in lines[1:]:
        _, x, y = map(float, coordinates.strip().split(" "))
        locations.append(Point(x, y))


def eucleadian_distance(point1, point2):
    dis = math.sqrt(pow(point1.x - point2.x, 2) + pow(point1.y - point2.y, 2))
    return dis

# distance_matix = np.zeros((num_of_cities, num_of_cities))
# for i in range(num_of_cities):
#     for j in range(num_of_cities):
#         distance_matix[i, j] = eucleadian_distance(locations[i], locations[j])

def shortest_distance_with_nearest_neighbour(num_of_cities, locations):
    track = [False for _ in range(num_of_cities)]
    track[0] = True
    
    prev_pos = 0
    distance_travelled = 0.0
    while not all(track):
        distances = []
        for i in range(num_of_cities):
            if not track[i]:
                distances.append((eucleadian_distance(locations[prev_pos], locations[i]), i))
        min_dis, next_pos = min(distances)
        track[next_pos] = True
        distance_travelled += min_dis
        prev_pos = next_pos

    distance_travelled += eucleadian_distance(locations[0], locations[prev_pos])
    return distance_travelled

print(shortest_distance_with_nearest_neighbour(num_of_cities, locations))
