"""
This file solves sudoku.
There are 2 methods.
1) the way our minds solve sudoku.
(no trial and error, method involves how our mind solve it)
(steps are little complex, but speed needs to be test)

2) the back tracking method
"""

# resolve issue where (2, 3), (3,4), (4, 3) are in a row/column
# it will remove the current scenario 2^9 cases (mostly will be)
import numpy as np

sudoku = [
    [3, 0, 5, 0, 7, 1, 0, 0, 9], 
    [0, 0, 0, 3, 4, 0, 0, 0, 0], 
    [0, 9, 0, 2, 0, 0, 0, 0, 0], 
    [0, 3, 0, 0, 0, 4, 0, 0, 0], 
    [0, 6, 0, 0, 0, 0, 0, 0, 7], 
    [0, 0, 0, 0, 0, 2, 8, 5, 0], 
    [0, 0, 0, 0, 0, 0, 0, 8, 0], 
    [0, 5, 4, 0, 0, 0, 9, 0, 1], 
    [0, 0, 7, 0, 0, 0, 4, 0, 0]]

puzzle = np.array(sudoku) # initiate from values, empty values as 0

# we are ensuring probable entries are sorted
probable_val = [[[] for _ in range(9)] for _ in range(9)]
probable_count = np.zeros((9, 9)) # initialize from 0


def get_valid_entries(puzzle, probable_val, probable_count):
    for i in range(9):
        for j in range(9):
            if puzzle[i, j] != 0:
                continue

            count = 0
            not_valid = set()
            for k in range(9):
                if puzzle[i, k] != 0:
                    not_valid.add(puzzle[i, k])

            for k in range(9):
                if puzzle[k, j] != 0:
                    not_valid.add(puzzle[k, j])

            temp_i = i//3
            temp_j = j//3
            for x in range(temp_i*3, (temp_i+1)*3):
                for y in range(temp_j*3, (temp_j+1)*3):
                    if puzzle[x, y] != 0:
                        not_valid.add(puzzle[x, y])

            for val in range(1, 10):
                if val not in not_valid:
                    probable_val[i][j].append(val)
                    count +=1
            probable_count[i, j] = count

get_valid_entries(puzzle, probable_val, probable_count)


def update_block(values):
    lst = []
    temp = []
    for i in range(0, 9):
        if values[i]:
            lst.append(i)
            temp.append(values[i])

    length = len(lst)

    for i in range(pow(2, length) - 1):
        curr = []
        track = 0
        x = bin(i)
        x = list(x[2:].rjust(length, '0'))
        for index, val in enumerate(x):
            if val == '1':
                curr = curr + temp[index]
                track +=1
        curr = set(curr)
        if len(curr) == track:
            for elem in curr:
                for index, val in enumerate(x):
                    if val == '0' and elem in temp[index]:
                        temp[index].remove(elem)

    for index, val in enumerate(lst):
        values[val] = temp[index]
    return values



def update_sudoku():
    # for rows
    for row in range(0, 9):
        values = probable_val[row][:]
        values = update_block(values[:])
        for column in range(0, 9):
            if probable_count[row, column] > 0:
                probable_val[row][column] = values[column]
                probable_count[row, column] = len(values[column])

    for column in range(0, 9):
        values = [probable_val[i][column] for i in range(9)]
        values = update_block(values[:])
        for row in range(0, 9):
            if probable_count[row, column] > 0:
                probable_val[row][column] = values[row]
                probable_count[row, column] = len(values[row])
    
    for row in [0, 3, 6]:
        for column in [0, 3, 6]:
            values = []
            for i in range(row, row+3):
                values = values + probable_val[i][column: column+3]
            values = update_block(values[:])
            for i in range(row, row+3):
                for j in range(column, column+3):
                    probable_val[i][j] = values[(i%3)*3 + (j%3)]
                    probable_count[i, j] = len(values[(i%3)*3 + (j%3)])


iterations = 0
while np.amax(probable_count) > 1:
    prev = np.sum(probable_count)
    print(f"prev: {prev}")
    iterations +=1
    update_sudoku()
    curr = np.sum(probable_count)
    print(f"curr: {curr}")
    if prev <= curr:
        print("sorry...:( sudoku not solvable")
        break
      

print(iterations)
for i in range(9):
    for j in range(9):
        if puzzle[i, j] == 0:
            puzzle[i, j] = probable_val[i][j][0]
print(puzzle)
print(probable_val)
print(probable_count)