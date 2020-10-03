"""
1) greedy algorithms from lecture for minimizing 
the weighted sum of completion times
"""



with open("../../dataset/course3/jobs.txt", 'r') as f0:
	jobs = f0.readlines()

priority = []

n_jobs = int(jobs[0])
for job in jobs[1:]:
	weight, length = map(int, job.strip().split(" "))
	priority.append((weight-length, weight, length))

sorted_priority = sorted(priority, key=lambda x: x[0], reverse=True)
current_time = 0
weighted_sum = 0
temp_lst = []

for elem in sorted_priority:
	if temp_lst:
		if elem[0] == temp_lst[-1][0]:
			temp_lst.append(elem)
		else:
			temp_lst = sorted(temp_lst, key=lambda x: x[1], reverse=True)
			for job in temp_lst:
				current_time += job[2]
				weighted_sum += (current_time*job[1])
			temp_lst = [elem]
	else:
		temp_lst.append(elem)


temp_lst = sorted(temp_lst, key=lambda x: x[1], reverse=True)
for job in temp_lst:
	current_time += job[2]
	weighted_sum += current_time*job[1]

print(weighted_sum)

"""
run the greedy algorithm that schedules jobs (optimally)
in decreasing order of the ratio (weight/length). In this
algorithm, it does not matter how you break ties
"""

with open("jobs.txt", 'r') as f0:
	jobs = f0.readlines()
priority = []

n_jobs = int(jobs[0])
for job in jobs[1:]:
	weight, length = map(int, job.strip().split(" "))
	priority.append((weight/length, weight, length))

sorted_priority = sorted(priority, key=lambda x: x[0], reverse=True)
current_time = 0
weighted_sum = 0

for elem in sorted_priority:
	current_time+=elem[2]
	weighted_sum += current_time*elem[1]


print(weighted_sum)

