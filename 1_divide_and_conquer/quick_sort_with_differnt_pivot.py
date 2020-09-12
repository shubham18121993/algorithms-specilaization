"""
Assignment week 3:
https://www.coursera.org/learn/algorithms-divide-conquer/exam/37cop/
programming-assignment-3/attempt
"""


def quick_sort_first_pivot(lst):
    # first element as pivot
    n = len(lst)
    inversions = n-1
    if n <= 1:
        return lst, inversions

    pivot = lst[0]
    track = 1
    for i in range(1, n):
        if lst[i] < pivot:
            lst[track], lst[i] = lst[i], lst[track]
            track+=1
    lst[0], lst[track-1] = lst[track-1], lst[0]
    lst1, inverions_left = quick_sort_first_pivot(lst[:track-1])
    lst2, inverions_right = quick_sort_first_pivot(lst[track:])
    inversions = inverions_left + inversions + inverions_right
    return lst1 + [pivot] + lst2, inversions

def quick_sort_last_pivot(lst):
    # last element as pivot
    n = len(lst)
    inversions = n-1
    if n <= 1:
        return lst, inversions

    lst[0], lst[-1] = lst[-1], lst[0]
    pivot = lst[0]
    track = 1
    for i in range(1, n):
        if lst[i] < pivot:
            lst[track], lst[i] = lst[i], lst[track]
            track+=1
    lst[0], lst[track-1] = lst[track-1], lst[0]
    lst1, inverions_left = quick_sort_last_pivot(lst[:track-1])
    lst2, inverions_right = quick_sort_last_pivot(lst[track:])
    inversions = inverions_left + inversions + inverions_right
    return lst1 + [pivot] + lst2, inversions


def quick_sort_median_pivot(lst):
    n = len(lst)
    inversions = n-1
    if n <= 1:
        return lst, inversions

    
    pivot = min(lst[0], lst[n//2], lst[-1])
    if pivot != lst[0]:
        if pivot == lst[n//2]:
            lst[0], lst[n//2] = lst[n//2], lst[0]
        else:
            lst[0], lst[-1] = lst[-1], lst[0]

    track = 1
    for i in range(1, n):
        if lst[i] < pivot:
            lst[track], lst[i] = lst[i], lst[track]
            track+=1
    lst[0], lst[track-1] = lst[track-1], lst[0]
    lst1, inverions_left = quick_sort_median_pivot(lst[:track-1])
    lst2, inverions_right = quick_sort_median_pivot(lst[track:])
    inversions = inverions_left + inversions + inverions_right
    return lst1 + [pivot] + lst2, inversions



if __name__ == "__main__":
    with open("./DataSet/QuickSort.txt", 'r') as f0:
        lines = f0.readlines()
    f0.close()
    lst = [int(line.strip()) for line in lines]
  
    _, inversions = quick_sort_median_pivot(lst)
    print(inversions)