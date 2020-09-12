"""
This contains solutions of optional problem from algorithsm.
Link:
https://www.coursera.org/learn/algorithms-divide-conquer/supplement/
Geunn/optional-theory-problems-batch-1
"""

# Problem 1:
# You are given as input an unsorted array of n distinct numbers, where n
# is a power of 2. Give an algorithm that identifies the second-largest
# number in the array, and that uses at most n +logn(base2)-2 comparisons.
# Solution
# n/2 -1  and n/2-1
# a1, a2 (a1 > a2) 
# b1, b2 (b1 > b2)  (3 comparisons)
# n = 2^m
# nth level n/2 comp

"""
from collections import defaultdict
import random


# My solution not so elegant needs
arr_dic = defaultdict(list)


def get_second_max(arr):
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
"""

"""
Problem2:
You are a given a unimodal array of n distinct elements, meaning that
its entries are in increasing order up until its maximum element,
after which its elements are in decreasing order. Give an algorithm to
compute the maximum element that runs in O(log n) time.
"""
"""
def get_max(arr):
    n = len(arr)
    if n ==1:
        return arr[0]

    if n==2:
        return arr[0] if arr[0]>arr[1] else arr[1]

    n2 = n//2
    pivot = arr[n2]

    if pivot > arr[n2-1]:
        if pivot > arr[n2+1]:
            return pivot
        else:
            return get_max(arr[n2:])
    else:
        return get_max(arr[:n2])


if __name__ == "__main__":
    arr_1 = [x for x in range(0, 1000)]
    arr_2 = [x for x in range(1500, 1000, -1)]
    arr = arr_1 + arr_2
    print(get_max(arr))
"""

"""
Problem Statement
You are given a sorted (from smallest to largest) array A of n distinct
integers which can be positive, negative, or zero. You want to decide
whether or not there is an index i such that A[i] = i. Design the
fastest algorithm that you can for solving this problem.
Solution: log(n)
"""

"""
def find_elem(arr, start):
    print(arr)
    print(start)
    
    n = len(arr)
    if n == 1:
        return arr[0]==start

    n2 = n//2
    if arr[n2] == start+n2:
        return True

    elif arr[n2] < start+n2:
        return find_elem(arr[n2:], start+n2)

    else:
        return find_elem(arr[:n2], start)


if __name__ == "__main__":
    arr = [-1, 0, 1, 2, 3, 4, 5, 7, 10]
    print(find_elem(arr, 0))

"""


"""
Problem4:
You are given an n by n grid of distinct numbers. A number is a local
minimum if it is smaller than all of its neighbors. (A neighbor of a
number is one immediately above, below, to the left, or the right. Most
numbers have four neighbors; numbers on the side have three; the four
corners have two.) Use the divide-and-conquer algorithm design paradigm
to compute a local minimum with only O(n) comparisons between pairs of
numbers. (Note: since there are n^2 numbers in the input, you cannot
afford to look at all of them. Hint: Think about what types of
recurrences would give you the desired upper bound.)

Solution:
Divide array in 4 equal parts by middle column and row.
Find the minimum of middle row and column. 
If its at intersection then its the local minimum.
If minimum is any element other the intersection, check rest two
elements for that element is minimum return it else return the matrix
in which minimum elem lies
"""

# Code
import numpy as np


def find_local_minimum(arr, x, y):
    print(arr)
    # def borderline cases
    num_rows, num_cols = arr.shape
    if num_rows ==1 or num_cols ==1:
        return np.amin(arr)

    # recursion code
    col = np.argmin(arr[x, :])
    row = np.argmin(arr[:, y])

    if row==x and col==y:
        return arr[x, y]
    else:
        try:
            xl = arr[x-1, col]
        except:
            xl = np.inf

        try:
            xr = arr[x+1, col]
        except:
            xr = np.inf

        try:
            yl = arr[row, y-1]
        except:
            yl = np.inf
        
        try:
            yr = arr[row, y+1]
        except:
            yr = np.inf

        # when min in row
        if arr[x, col] < arr[row, y]:
            if arr[x, col] < xl and arr[x, col] < xr:
                return arr[x, col]
            else:
                if xl < xr:
                    x2 = x//2
                    if col < y:
                        return find_local_minimum(arr[:x, :y], x2, col)
                    else:
                        return find_local_minimum(arr[:x, y:], x2, col-y)
                else:
                    x2 = (num_rows - x)//2
                    if col < y:
                        return find_local_minimum(arr[x:, :y], x2, col)
                    else:
                        return find_local_minimum(arr[x:, y:], x2, col-y)
        
        # when min in column
        else: 
            if arr[row, y] < yl and arr[row, y] < yr:
                return arr[row, y]
            else:
                if yl < yr:
                    y2 = y//2
                    if row < x:
                        return find_local_minimum(arr[:x, :y], row, y2)
                    else:
                        return find_local_minimum(arr[x:, :y], row-x, y2)
                else:
                    y2 = (num_cols -y) //2
                    if row < x:
                        return find_local_minimum(arr[:x, y:], row, y2)
                    else:
                        return find_local_minimum(arr[x:, y:], row-x, y2)


if __name__ == "__main__":
    arr = np.random.randint(1,900, size=(15,15))

    # arr = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])
    row, col = arr.shape
    arr[row//2, :] = np.random.randint(300,900, size=(15))
    arr[:, col//2] = np.random.randint(300,900, size=(15))
    local_min = find_local_minimum(arr, row//2, col//2)
    print(f"local_min: {local_min}")
