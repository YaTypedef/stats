# encoding: utf-8
import numpy as np
import math

def read_points():
    points = []
    for line in open('weibull.txt'):
        points.append(float(line))
    return points

# F(x) = 1 - e ^ (-x ^ gamma)
# p(x) = F'(x) = e ^ (-x ^ gamma) * gamma * x ^ (gamma - 1)
# L = p(x_1) * ... * p(x_N) =
#   = gamma ^ N * П x_i ^ (gamma - 1) * П e ^ (-x_i ^ gamma)
# ln L = N * ln gamma + (gamma - 1) * sum(ln x_i) - sum(x_i ^ gamma)
# Пусть gamma0 = log_10(gamma)
def find_optimal_gamma(points, left, right, step):
    max_sum = None
    best_gamma0 = None
    sum_logs = sum([math.log(x) for x in points])
    for gamma0 in np.arange(left, right, step):
        gamma = math.pow(10, gamma0)
        s = len(points) * math.log(gamma) + \
            (gamma - 1) * sum_logs - \
            sum([math.pow(x, gamma) for x in points])
        print s, gamma0, gamma
        if max_sum == None or s > max_sum:
            max_sum = s
            best_gamma0 = gamma0
    return math.pow(10, best_gamma0)

print find_optimal_gamma(read_points(), -2, 2, 0.001)
