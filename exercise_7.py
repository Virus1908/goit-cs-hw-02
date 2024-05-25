import random


def simulate_single_throw() -> int:
    return random.randint(1, 6)


def monte_carlo_simulation(num_experiments) -> dict:
    result = dict.fromkeys(range(2, 13), 0)
    for _ in range(num_experiments):
        two_sum = simulate_single_throw() + simulate_single_throw()
        result[two_sum] = result[two_sum] + 1

    return {k: v / num_experiments for k, v in result.items()}


def main7():
    result = monte_carlo_simulation(100000)
    print("Результат симуляції:")
    for s in range(2, 13):
        print(f"{s:2}  {result[s]}")
