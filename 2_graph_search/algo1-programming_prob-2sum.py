"""
This file compares target values t in the 
interval [-10000,10000] (inclusive) such that there are 
distinct numbers x,y in the input file that satisfy x+y=t
There are 2 solutions, one uses sorting another one uses
hash tables
"""
import math
import time


def get_hash_val(num):
    is_negative = False
    if num < 0:
        is_negative = True
        num = abs(num)
    str_num = str(num)
    try:
        hash_val = int(str_num[0:6])
    except:
        hash_val = 0
    if is_negative:
        hash_val = 1000000 - hash_val
    else:
        hash_val = 1000000 + hash_val
    return hash_val


class Node:
    def __init__(self, val=None):
        self.dataval = val
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None

    def insert_node(self, newval):
        new_node = Node(newval)
        new_node.nextval = self.headval
        self.headval = new_node

    def delete_node(self, delval):
        val =  self.headval
        if val is not None:
            if val.dataval == delval:
                self.headval = val.nextval
                return

        while val is not None:
            if val.dataval == delval:
                prev.nextval = val.nextval
                break
            prev = val
            val = val.nextval
        return

    def check_node(self, dataval):
        val = self.headval
        while val is not None:
            if val.dataval == dataval:
                return True
            val = val.nextval
        return False

    def get_count(self, val1, val2):
        count = 0
        val = self.headval
        while val is not None: 
            if val.dataval >= val1 and val.dataval <= val2:
                count+=1
            val = val.nextval
        return count


def get_count_of_sum_by_hash(lst):
    count = 0
    hash_list = [LinkedList() for _ in range(2000000)]

    for elem in lst:
        hash_val = get_hash_val(elem)
        if not hash_list[hash_val].check_node(elem):
            hash_list[hash_val].insert_node(elem)

    for elem in lst:
        hash_val = get_hash_val(elem)
        hash_list[hash_val].delete_node(elem)
        val2 = -10000-elem
        val1 = 10000-elem
        if val1 > val2:
            val1, val2 = val2, val1

        hash_val1 = get_hash_val(val1)
        hash_val2 = get_hash_val(val2)
        if hash_val1 > hash_val2:
            hash_val2, hash_val1 = hash_val1, hash_val2

        for i in range(hash_val1, hash_val2+1):
            count += hash_list[i].get_count(val1, val2)
    return count

def get_count_of_sum_by_sort(lst):
    lst1 = sorted(lst)
    count = 0
    prev_elem = math.inf
    next_elem = math.inf
    len_lst = len(lst1)
    j = len_lst-1
    for i in range(len_lst-1):
        elem = lst1[i]
        track = 0
        if i >= j:
            print(i)
            print(j)
            break
        while elem != prev_elem and i < j:
            if lst1[j] != next_elem:
                sum_val = elem+lst1[j]
                if sum_val >= -10000:
                    if sum_val <= 10000:
                        track+=1
                else:
                    break
            next_elem = lst1[j]
            j-=1
        j = j + track
        count += track
        try:
            next_elem = lst1[j+1]
        except:
            next_elem = math.inf

        prev_elem = elem
    return count


if __name__ == "__main__":
    with open('algo1-programming_prob-2sum.txt', 'r') as f0:
        lines = f0.readlines()

    # lst = []
    # for line in lines:
    #     lst.append(int(line.strip()))
    lst = [i for i in range(1000000)]

    start_time = time.time()
    count1 = get_count_of_sum_by_sort(lst)
    end_time =  time.time()
    print(f"count by sort: {count1}, time taken: {end_time-start_time}")

    start_time = time.time()
    count1 = get_count_of_sum_by_hash(lst)
    end_time =  time.time()
    print(f"count by hash: {count1}, time taken: {end_time-start_time}")




