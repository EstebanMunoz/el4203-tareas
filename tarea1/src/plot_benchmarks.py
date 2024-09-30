from pathlib import Path

import matplotlib.pyplot as plt


def save_benchmarks_plot(name: str, *sol_methods: tuple[str]) -> None:
    if len(sol_methods) == 0:
        raise TypeError("At least one solution should be passed, given 0.")

    benchmarks = {}
    data_path = Path("../data/")
    for solution in sol_methods:
        file_path = data_path / f"{solution}_benchmark.txt"
        benchmarks[solution] = get_benchmark(file_path)

        keys = benchmarks[solution].keys()
        values = benchmarks[solution].values()

        plt.plot(keys, values, label=solution)

    plt.legend()
    plt.grid()

    plt.title("Execution time for different count methods")
    plt.xlabel("$n + m$")
    plt.ylabel("Execution Time [s]")

    figures_path = Path("../figures")
    if not figures_path.exists():
        Path.mkdir(figures_path)

    plt.savefig(figures_path / f"{name}.svg")


def get_benchmark(file_path: Path) -> dict[int, float]:
    benchmark = {}
    if not file_path.is_file():
        raise FileNotFoundError(
            "The benchmark file doesn't exist. Make sure to create it before using it"
        )

    with Path.open(file_path, "r") as f:
        for line in f:
            n, m, time = line.split(",")
            n, m = int(n), int(m)
            time = float(time.strip())
            benchmark[n + m] = time

    return benchmark
