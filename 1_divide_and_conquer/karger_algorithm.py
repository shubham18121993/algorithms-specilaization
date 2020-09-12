"""
Karger Algorithm

Algorithm finds minimum cuts with probabilty of 1/n^2
after n^2logn trials algorithm can find the minimum cut with probability
of 1/e
"""
import random
import math



def karger_algorithm(arr, vertices):

    sys_random = random.SystemRandom()
    while len(vertices) > 2:
        # val = random.randrange(0, len(vertices))
        # randomly select an edge
        head = sys_random.choice(vertices)
        tail = sys_random.choice(arr[head])
        vertices.remove(tail)

        # always merging tail in head
        edges = arr[tail]
        edges = [x for x in edges if x != head]
        arr[head] = [x for x in arr[head] if x != tail] + edges
        for elem in set(edges):
            arr[elem] = [head if x == tail else x for x in arr[elem]]

    return len(arr[vertices[0]])

if __name__ == "__main__":

    value = math.inf
    for i in range(100000):
        with open("./DataSet/kargerMinCut.txt", 'r') as f0:
            lines = f0.readlines()
        arr = {}
        vertices = []

        for line in lines:
            lst = list(map(int, line.strip().split()))
            vertices.append(lst[0])
            arr[lst[0]] = lst[1:]
        value = min(value, karger_algorithm(arr, vertices))
    print(value)


