import matplotlib.pyplot as plt

import os


def save_benchmarks_plot(name: str, *sol_methods: tuple[str]) -> None:
    if len(sol_methods) == 0:
        raise TypeError("At least one solution should be passed, given 0.")
    
    benchmarks = dict()
    data_path = "../data/"
    for solution in sol_methods:
        file_path = data_path + f"{solution}_benchmark.txt"
        benchmarks[solution] = get_benchmark(file_path)

        keys = benchmarks[solution].keys()
        values = benchmarks[solution].values()

        plt.plot(keys, values, label=solution)

    plt.legend()
    plt.grid()

    plt.title("Execution time for different count methods")
    plt.xlabel("$n + m$")
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
            n, m, time = line.split(",")
            n, m = int(n), int(m)
            time = float(time.strip())
            benchmark[n+m] = time

    return benchmark
