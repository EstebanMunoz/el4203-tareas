from path_count import PathCount
from plot_benchmarks import save_benchmarks_plot
from solutions import (
    CombinatorialSolution,
    DinamycSolution,
    MathCombSolution,
    RecursiveSolution,
)

if __name__ == "__main__":
    max_grid_dim = 17
    path_count = PathCount()

    solutions = [
        RecursiveSolution(),
        DinamycSolution(),
        CombinatorialSolution(),
        MathCombSolution(),
    ]

    for solution in solutions:
        path_count.set_solution_method(solution)
        for k in range(2, max_grid_dim + 1):
            if k != 2:
                path_count.count(k - 1, k)
            path_count.count(k, k)

    str_sols = [str(solution) for solution in solutions]
    save_benchmarks_plot("benchmarks", *str_sols)
