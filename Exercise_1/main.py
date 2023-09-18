from solve_tsp import *

string1= input()
parent1 = [int(k) for k in string1.split(',')]


string2= input()
parent2 = [int(k) for k in string2.split(',')]

lower_bound = int(input())
upper_bound = int(input())

# parent1 = [8, 11, 3, 5, 6, 4, 2, 12, 1, 9, 7, 10]  # padre
# parent2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 4]  # madre
# lower_bound = 6  # lowerbound
# upper_bound = 9  # upper bound

solution = order_crossover(parent1, parent2, lower_bound, upper_bound)

print(solution)
