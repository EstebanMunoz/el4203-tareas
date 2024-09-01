import numpy as np

from decorators import benchmark

class PathCount:
    def __init__(self, solution_method: str | None = None) -> None:
        self.solution_method = "recursive"
        if solution_method is not None:
            self.solution_method = self.set_solution_method(solution_method)
    

    def set_solution_method(self, solution_method: str) -> None:
        valid_methods = ["recursive", "dynamic", "combinatorial"]
        if solution_method not in valid_methods:
            raise ValueError(f"Not a valid solution method. Valid inputs are {valid_methods}")
        
        self.solution_method = solution_method

    
    @benchmark
    def solve(self, n: int, m: int) -> int:
        match self.solution_method:
            case "recursive":
                return self.recursive_path_count(n, m)
            case "dynamic":
                return self.dp_path_count(n, m)
            case "combinatorial":
                return self.combinatorial_path_count(n, m)


    def recursive_path_count(self, n: int, m: int) -> int:
        if n < 1 or m < 1:
            raise ValueError(f"Both arguments must be positive numbers, given {n=}, {m=}")
        if n == 1 or m == 1:
            return 1
        
        return self.recursive_path_count(n - 1, m) + self.recursive_path_count(n, m - 1)


    def dp_path_count(self, n: int, m: int) -> int:
        if n < 1 or m < 1:
            raise ValueError(f"Both arguments must be positive numbers, given {n=}, {m=}")
        lut = [[1 for _ in range(m)] for _ in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                lut[i][j] = lut[i - 1][j] + lut[i][j - 1]

        return lut[n-1][m-1]


    def factorial(self, n: int) -> int:
        result = 1
        for i in range(2, n+1):
            result *= i
        
        return result


    def combinatorial_path_count(self, n: int, m: int) -> int:
        if n < 1 or m < 1:
            raise ValueError(f"Both arguments must be positive numbers, given {n=}, {m=}")
        
        log_numerator = sum(np.log(i) for i in range(1, (n+m-2) + 1))
        log_denominator = sum(np.log(i) for i in range(1, (n-1) + 1)) + sum(np.log(j) for j in range(1, (m-1) + 1))
        log_result = log_numerator - log_denominator
        return int(np.exp(log_result))