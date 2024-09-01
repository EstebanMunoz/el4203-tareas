from solutions import PathCountSolution, RecursiveSolution
from decorators import benchmark

class PathCount:
    def __init__(self, solution_method: PathCountSolution | None = None) -> None:
        self.set_solution_method(solution_method)


    def set_solution_method(self, solution_method: PathCountSolution | None) -> None:
        self.solution_method = solution_method
        if solution_method is None:
            self.solution_method = RecursiveSolution()


    @benchmark
    def count(self, n: int, m: int) -> int:
        if n < 1 or m < 1:
            raise ValueError(f"Both arguments must be positive numbers, given {n=}, {m=}")
        
        return self.solution_method.count(n, m)
