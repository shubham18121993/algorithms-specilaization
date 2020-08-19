import matplotlib.pyplot as plt
import numpy as np
import math



with open("../../dataset/course4/tsp.txt", 'r') as f0:
	lines = f0.readlines()
	locations = []

	for row in lines[1:]:
		x_coord, y_coord = map(float, row.strip().split(" "))
		locations.append((x_coord, y_coord))

def calculate_cost(y_hat, y_num):
	return np.sum(np.square(y_hat - y_num))


def linear_regression(xs, ys):
	learning_rate = 0.009
	b = 0
	m = 0
	x_num = np.reshape(np.array(xs[:]), (1, 25)) / 10000
	y_num = np.reshape(np.array(ys[:]), (1, 25)) / 10000
	iterations = 100000
	while iterations > 0:
		y_hat  = b + m*x_num
		m -= learning_rate*(np.dot((y_hat - y_num), np.transpose(x_num)))/25
		b -= learning_rate*(np.sum(y_hat - y_num))/25
		iterations -=1

	y_cal = [m[0, 0]*x + b*10000 for x in xs]
	return y_cal



xs = [point[0] for point in locations]
ys = [point[1] for point in locations]
y_cal = linear_regression(xs, ys)

plt.plot(xs, ys)
print(y_cal)
plt.plot(xs, y_cal)

plt.show()