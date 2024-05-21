import random

import scipy.integrate as spi
from pulp import *


def solve_pl():
    model = pulp.LpProblem("Drink_Company", LpMaximize)
    lemonade = pulp.LpVariable('lemonade', lowBound=0)
    juice = pulp.LpVariable('juice', lowBound=0)
    water = pulp.LpVariable('water', lowBound=0, upBound=100)
    sugar = pulp.LpVariable('sugar', lowBound=0, upBound=50)
    lemon_juice = pulp.LpVariable('lemon_juice', lowBound=0, upBound=30)
    sauce = pulp.LpVariable('sauce', lowBound=0, upBound=40)
    model += lemonade + juice, "Problem"

    model += 2 * lemonade + juice <= water, "water_constraint"
    model += lemonade <= sugar, "sugar_constraint"
    model += lemonade <= lemon_juice, "lemon_juice_constraint"
    model += 2 * juice <= sauce, "sauce_constraint"

    model.solve()
    lemonade_value = lemonade.name + "=" + str(lemonade.varValue)
    juice_value = juice.name + "=" + str(juice.varValue)
    return lemonade_value + "\n" + juice_value


# noinspection PyShadowingNames
def f(x):
    return x ** 2


def solve_quad(func, a, b):
    return spi.quad(func, a, b)[0]


def monte_carlo(func, a, b, num_experiments, count, lower_bound=0, upper_bound=10):
    average_area = 0
    need_to_change_upper_bound = False
    need_to_change_lower_bound = False
    for _ in range(num_experiments):
        points = [(random.uniform(a, b), random.uniform(lower_bound, upper_bound)) for _ in range(count)]
        inside_points = 0
        for point in points:
            if func(point[0]) < lower_bound:
                need_to_change_lower_bound = True
            elif func(point[0]) > upper_bound:
                need_to_change_upper_bound = True
            elif point[1] < func(point[0]):
                inside_points += 1

        if need_to_change_upper_bound or need_to_change_lower_bound:
            break

        area = (inside_points / len(points)) * ((b - a) * (upper_bound - lower_bound))

        average_area += area

    if need_to_change_lower_bound:
        return monte_carlo(func, a, b, num_experiments, count, lower_bound - 10, upper_bound)
    if need_to_change_upper_bound:
        return monte_carlo(func, a, b, num_experiments, count, lower_bound, upper_bound + 10)

    average_area /= num_experiments
    return average_area


def main():
    # print(solve_pl())
    a = 0
    b = 20
    print(monte_carlo(f, a, b, 100, 10))
    print(monte_carlo(f, a, b, 100, 100))
    print(monte_carlo(f, a, b, 100, 1000))
    print(monte_carlo(f, a, b, 100, 10000))
    print(monte_carlo(f, a, b, 10, 10000))
    print(monte_carlo(f, a, b, 1, 10000))
    print(monte_carlo(f, a, b, 1, 10))
    print(solve_quad(f, a, b))


if __name__ == '__main__':
    main()
