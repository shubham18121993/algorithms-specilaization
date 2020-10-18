

def get_max_weight(n, lst):
    optimal_solution = [0]
    prev = 0
    curr = 0
    for elem in lst:
        optimal_solution.append(max(prev+elem, curr))
        prev = curr
        curr = optimal_solution[-1]

    solution_set = []
    val = optimal_solution[-1]
    
    for i in range(n, 0, -1):
        if val < optimal_solution[i]:
            pass
        
        elif val == optimal_solution[i] and optimal_solution[i] !=optimal_solution[i-1]:
            val -= lst[i-1]
            solution_set.append(i)
        
        else:
            pass

    return solution_set

with open("../../dataset/course3/mwis.txt", 'r') as f0:
    lines = f0.readlines()

n = int(lines[0].strip())
lst = []
for line in lines[1:]:
    lst.append(int(line.strip()))
sol = get_max_weight(n, lst)
print(sol)