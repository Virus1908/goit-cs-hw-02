def greedy_algorithm(items_dict, capacity: int):
    items = sorted(items_dict.items(), key=lambda x: x[1]["cost"] / x[1]["calories"])
    total_value = 0
    foods = []
    for food, data in items:
        if capacity >= data["cost"]:
            capacity -= data["cost"]
            total_value += data["calories"]
            foods.append(food)
    return foods, total_value


def dynamic_programming_solve(capacity, wt, val, n):
    table = [[(0, []) for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                table[i][w] = (0, [])
            elif wt[i - 1] <= w:
                with_item = val[i - 1] + table[i - 1][w - wt[i - 1]][0]
                without_item = table[i - 1][w][0]
                if with_item > without_item:
                    new_list = table[i - 1][w - wt[i - 1]][1].copy()
                    new_list.append(i - 1)
                    table[i][w] = (with_item, new_list)
                else:
                    table[i][w] = table[i - 1][w]
            else:
                table[i][w] = table[i - 1][w]

    return table[n][capacity]


def dynamic_programming(items_dict, capacity: int):
    weights = [data["cost"] for data in items_dict.values()]
    values = [data["calories"] for data in items_dict.values()]
    names = [food for food in items_dict.keys()]
    calories, foods = dynamic_programming_solve(capacity, weights, values, len(items_dict))
    return list(map(lambda i: names[i], foods)), calories


def main6():
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }
    capacity = 100
    print(greedy_algorithm(items, capacity))
    print(dynamic_programming(items, capacity))
