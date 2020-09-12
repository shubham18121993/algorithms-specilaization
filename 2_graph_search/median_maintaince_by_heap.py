"""
Median maintainace using heap, time O(logn)
it uses min and max heap
script is written from scratch
"""

min_heap = []
max_heap = []


def insert_min(elem):
    l = len(min_heap)
    min_heap.append(elem)
    while min_heap[l] < min_heap[((l+1)//2)-1]:
        min_heap[l], min_heap[((l+1)//2)-1] = min_heap[((l+1)//2)-1], min_heap[l]
        l = ((l+1)//2)-1
        if l == 0:
            break 
    return

def pop_min():
    min_heap[0], min_heap[-1] = min_heap[-1], min_heap[0]
    elem = min_heap.pop()
    l1 = 0
    l2 = 2
    l = len(min_heap)
    while min_heap[l1] > min(min_heap[l2-1:l2+1]):
        try:
            if min_heap[l2-1] < min_heap[l2]:
                min_heap[l2-1], min_heap[l1] = min_heap[l1], min_heap[l2-1]
                l1 = l2-1
            else:
                min_heap[l2], min_heap[l1] = min_heap[l1], min_heap[l2]
                l1 = l2
        except:
            min_heap[l2-1], min_heap[l1] = min_heap[l1], min_heap[l2-1]
            l1 = l2-1
        l2 = (l1+1)*2
        if l2 > l:
            break
    return elem

def insert_max(elem):
    l = len(max_heap)
    max_heap.append(elem)
    while max_heap[l] > max_heap[((l+1)//2)-1]:
        max_heap[l], max_heap[((l+1)//2)-1] = max_heap[((l+1)//2)-1], max_heap[l]
        l = ((l+1)//2)-1
        if l == 0:
            break 
    return

def pop_max():
    max_heap[0], max_heap[-1] = max_heap[-1], max_heap[0]
    elem = max_heap.pop()
    l1 = 0
    l2 = 2
    l = len(max_heap)
    while max_heap[l1] < max(max_heap[l2-1:l2+1]):
        try:
            if max_heap[l2-1] > max_heap[l2]:
                max_heap[l2-1], max_heap[l1] = max_heap[l1], max_heap[l2-1]
                l1 = l2-1
            else:
                max_heap[l2], max_heap[l1] = max_heap[l1], max_heap[l2]
                l1 = l2
        except:
            max_heap[l2-1], max_heap[l1] = max_heap[l1], max_heap[l2-1]
            l1 = l2-1
        l2 = (l1+1)*2
        if l2 > l:
            break
    return elem


def get_median(elem, track):

    if track==1:
        max_heap.append(elem)
        return max_heap[0]
    
    if track==2:
        if elem >= max_heap[0]:
            min_heap.append(elem)
        else:
            max_heap.append(elem)
            temp = max_heap.pop(0)
            min_heap.append(temp)
        return max_heap[0]

    if elem > min_heap[0]:
        insert_min(elem)
    else:
        insert_max(elem)

    l1 = len(max_heap)
    l2 = len(min_heap)

    if l2 > l1:
        elem = pop_min()
        insert_max(elem)
    if l1 > l2+1:
        elem = pop_max()
        insert_min(elem)
    return max_heap[0]



if __name__ == "__main__":
    with open('../../dataset/course2/Median.txt', 'r') as f0:
        lines = f0.readlines()
    track = 0
    with open('median_valus.txt', 'w') as f1:
        for elem in lines:
            track+=1
            elem = int(elem.strip())
            median = get_median(elem, track)
            f1.write(str(median)+'\n')
            if len(min_heap) > 0 and min(min_heap) != min_heap[0]:
                print(track)
                print(min(min_heap))
                print(f"min_heap:{min_heap}")
                print(f"max_heap:{max_heap}")
                break

