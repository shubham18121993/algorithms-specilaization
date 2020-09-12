"""
Programming Assignment #2
This modules counts number of inversions in an array.
An inversion is defined as for any i < j if array[i] > array[j].
This module uses merge sort to do that, so at cost of O(n*logn)
"""


def count_inversions(arr):
    inversions = 0
    n = len(arr)
    if n <= 1:
        return arr, inversions

    arr_x, x = count_inversions(arr[:n//2])
    arr_y, y = count_inversions(arr[n//2:])


    i = 0
    j = 0
    sorted_arr = []

    while i < n // 2 and j < (n - n // 2):
        if arr_x[i] <= arr_y[j]:
            sorted_arr.append(arr_x[i])
            i += 1
        else:
            sorted_arr.append(arr_y[j])
            j += 1
            inversions += (n//2 - i)

    for k in range(j, n - n // 2):
        sorted_arr.append(arr_y[k])

    for k in range(i, n // 2):
        sorted_arr.append(arr_x[k])

    inversions = inversions + x + y
    return sorted_arr, inversions


if __name__ == "__main__":

    with open("./DataSet/IntegerArray.txt", 'r') as f0:
        lines = f0.readlines()
    f0.close()
    arr = [int(line.strip()) for line in lines]
    # arr = [1, 3, 5, 2, 4, 6]
    _, inversions = count_inversions(arr)
    print(f"inversions:{inversions}")
