import timeit

# оскільки масив містить елемент "1", любе цілоцисельне ріщення буде можливе
# також масив одразу відсортований
available_coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(coins_sum: int):
    result = {}
    sum_left = coins_sum
    for available_coin in available_coins:
        coins_picked = 0
        while sum_left >= available_coin:
            coins_picked += 1
            sum_left -= available_coin
        if coins_picked > 0:
            result[available_coin] = coins_picked

    return result


def find_min_coins(coins_sum: int):
    best_results = [{-1: 0 if i == 0 else -1} for i in range(coins_sum + 1)]

    for ongoing_sum in range(coins_sum + 1):
        for available_coin in available_coins:
            if available_coin <= ongoing_sum:
                prev_step_best = best_results[ongoing_sum - available_coin][-1]
                current_best = best_results[ongoing_sum][-1]
                if current_best == -1 or prev_step_best + 1 < current_best:
                    new_best = best_results[ongoing_sum - available_coin].copy()
                    new_best[-1] = prev_step_best + 1
                    new_best[available_coin] = new_best[available_coin] + 1 if available_coin in new_best.keys() else 1
                    best_results[ongoing_sum] = new_best

    result = best_results[coins_sum]
    result.pop(-1)
    return result


def do_test(name: str, count: int):
    timeit_report = timeit.timeit(f"{name}({count})",
                                  number=1000,
                                  setup=f"from __main__ import {name}"
                                  )
    print('name:{:<20s} count:{:5d} result:{:.4f}'.format(name, count, timeit_report))


def main():
    do_test("find_coins_greedy", 113)
    do_test("find_min_coins", 113)
    do_test("find_coins_greedy", 1131)
    do_test("find_min_coins", 1131)
    do_test("find_coins_greedy", 11312)
    do_test("find_min_coins", 11312)


if __name__ == '__main__':
    main()
