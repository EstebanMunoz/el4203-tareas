from path_count import PathCount
from plot_benchmarks import save_benchmarks_plot

if __name__ == "__main__":
    dim = 17
    path_count = PathCount()

    methods = ["recursive", "dynamic", "combinatorial"]
    for method in methods:
        path_count.set_solution_method(method)
        for k in range(3, dim+1):
            if k != 3:
                path_count.solve(k-2, k-1)
            path_count.solve(k-1, k-1)

    save_benchmarks_plot("benchmarks", *methods)
    