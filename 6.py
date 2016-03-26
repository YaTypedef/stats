import numpy as np
import math

def read_points():
    points = []
    for line in open('cauchy.txt'):
        points.append(float(line))
    return points

def find_optimal_x0(points, left, right, step):
    min_sum = None
    best_x0 = None
    for x0 in np.arange(left, right, step):
        s = sum([math.log(1 + (x - x0) * (x - x0)) for x in points])
        if min_sum == None or s < min_sum:
            min_sum = s
            best_x0 = x0
    return best_x0


points = read_points()
left = -1000
right = 1000
step = 1.0

for i in range(10):
    x0 = find_optimal_x0(points, left, right, step)
    print x0, "+/-", step
    radius = (right - left) / 20
    left = x0 - radius
    right = x0 + radius
    step /= 10
