"""
Algorithm is used to find closest pair from a group of points on plane.

Naive way is of order O(n^2).
Assumptions: no points are same.
Pre-processing step:
Sort array on both X coordinates and Y coodinates.
Array sorted on Y coordinates will be used later.
Steps:
1) Find the middle point in the sorted array (array sorted on X 
coordinates, and divide the array in two halves.
2) Recursively find the smallest distances in both subarrays.
Let it be d (minimum of both subarrays).We have an upper bound d of 
minimum distance.
3) Now take the middle point (right most point of left subarray).
and find all points whose x coordinate is closer than d. Build an array
strip[] of all such points.
4) Sort the array strip[] according to y coordinates. This step is
O(nLogn), optimized to O(n) by using sorted array on Y coordinates.
6) Now we only need to check at most 7 points after it (note that strip
is sorted according to Y coordinate)
7) Finally return the minimum of d and distance calculated in the above
step (step 6)
Time Complexity Let Time complexity of above algorithm be T(n).
Let us assume that we use a O(nLogn) sorting algorithm.
The above algorithm divides all points in two sets and recursively calls
for two sets. After dividing, it finds the strip in O(n) time, sorts the
strip in O(nLogn) time and finally finds the closest points in strip in
O(n) time. So T(n) can expressed as follows:
T(n) = 2T(n/2) + O(n) + O(nLogn) + O(n)
T(n) = 2T(n/2) + O(nLogn)
T(n) = T(n x Logn x Logn)
"""
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dist(p1, p2):
    distance = math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
    return distance


def brute_force(n, arr):
    if n <=1:
        return None, None, None

    if n == 2:
        return arr[0], arr[1], dist(arr[0], arr[1])

    else:
        d1 = dist(arr[0], arr[1])
        d2 = dist(arr[0], arr[2])
        d3 = dist(arr[1], arr[2])
        if min(d1, d2, d3) == d1:
            return arr[0], arr[1], d1
        elif min(d1, d2, d3) == d2:
            return arr[0], arr[2], d2
        else:
            return arr[1], arr[2], d3

def get_closest_distance(arr_x, arr_y):
    n = len(arr_x)  # Number of elements in array

    if n <= 3:
        p1, p2, distance = brute_force(n, arr_x)
        return p1, p2, distance

    arr_yl = [k for k in arr_y if arr_x[n//2-1].x - k.x >= 0]
    arr_yr = [k for k in arr_y if arr_x[n//2].x - k.x <= 0]

    pl_1, pl_2, dl = get_closest_distance(arr_x[: n // 2], arr_yl)
    pr_1, pr_2, dr = get_closest_distance(arr_x[n // 2 :], arr_yr)
    d = min(dl, dr)

    if d == dl:
        p1, p2 = pl_1, pl_2 
    else:
        p1, p2 = pr_1, pr_2

    lst = [k for k in arr_y if abs(arr_x[n // 2 - 1].x - k.x) < d]

    for index, point in enumerate(lst):
        for elem in lst[index+1: index + 8]:
            if dist(point, elem) < d:
                d = dist(point, elem)
                p1 = point
                p2 = elem

    return p1, p2, d


if __name__ == "__main__":
    arr = [
        Point(2, 3),
        Point(12, 30),
        Point(40, 50),
        Point(5, 1),
        Point(12, 10),
        Point(3, 4),
    ]
    arr_x = sorted(arr, key=lambda point: point.x)
    arr_y = sorted(arr, key=lambda point: point.y)
    p1, p2, distance = get_closest_distance(arr_x, arr_y)
    print(f"points are: ({p1.x}, {p1.y}), ({p2.x}, {p2.y})")
    print(f"distance: {distance}")
