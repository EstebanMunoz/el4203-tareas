import matplotlib.pyplot as plt

import os


def save_benchmarks_plot(name: str, *sol_methods: tuple[str]) -> None:
    if len(sol_methods) == 0:
        raise TypeError("At least one method should be passed, given 0.")
    
    benchmarks = dict()
    data_path = "../data/"
    for method in sol_methods:
        file_path = data_path + f"{method}_benchmark.txt"
        benchmarks[method] = get_benchmark(file_path)

        keys = benchmarks[method].keys()
        values = benchmarks[method].values()

        plt.plot(keys, values, label=method)

    plt.legend()
    plt.grid()

    plt.title("Execution time for different Fibonacci methods")
    plt.xlabel("Fibonacci Number")
    plt.ylabel("Execution Time [s]")

    figures_path = "../figures"
    if not os.path.isdir(figures_path):
        os.makedirs(figures_path)

    plt.savefig(f"{figures_path}/{name}.svg")


def get_benchmark(file_path: str) -> dict[int, float]:
    benchmark = dict()
    if not os.path.isfile(file_path):
        raise FileNotFoundError("The benchmark file doesn't exist. Make sure to create it before using it")

    with open(file_path, "r") as f:
        for line in f:
            num, time = line.split(":")
            num = int(num)
            time = float(time.strip())
            benchmark[num] = time

    return benchmark
