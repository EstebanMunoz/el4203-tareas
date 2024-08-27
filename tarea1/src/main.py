from fibonacci import Fibonacci
from plot_benchmarks import save_benchmarks_plot

if __name__ == "__main__":
    n = 40
    fibonacci = Fibonacci()

    methods = ["recursive", "iterative"]
    for method in methods:
        fibonacci.set_sol_method(method)
        for k in range(n):
            fibonacci.calculate(k)

    save_benchmarks_plot("benchmarks", *methods)
    