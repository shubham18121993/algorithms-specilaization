"""
"""
# problem3: Weighted median

def get_sublist_median(sublist):
    sublist.sort()
    sub_weight = sum([elem[1] for elem in sublist])
    curr_weight = 0.0
    for elem in sublist:
        val, weight = elem
        curr_weight += weight
        if curr_weight >= sub_weight/2:
            return elem


def get_weighted_median(lst, total_weight, wl, wr):
    n = len(lst)

    if n == 1:
        return [lst[0][0]]

    pivot_lst = [(lst[i][0], lst[i][1], i) for i in range(n)]
    total_pivots = n
    while total_pivots > 1:
        temp = [get_sublist_median(pivot_lst[i: i+5]) for i in range(0, n, 5)]
        pivot_lst = temp[:]
        total_pivots = len(temp)

    pivot_pos = pivot_lst[0][2]
    lst[pivot_pos], lst[0] = lst[0], lst[pivot_pos]
    pivot = lst[0][0]
    pivot_weight = lst[0][1]
    track = 1

    for i in range(1, n):
        x, w = lst[i]
        if x < pivot:
            wl += w
            lst[track], lst[i] = lst[i], lst[track]
            track += 1
        else:
            wr += w

    if wl <= total_weight/2 and wr <= total_weight/2:
        return [pivot]
    elif wl <= total_weight/2:
        return get_weighted_median(lst[track:], total_weight, wl+pivot_weight, 0)
    else:
        return get_weighted_median(lst[1:track], total_weight, 0, wr+pivot_weight)



