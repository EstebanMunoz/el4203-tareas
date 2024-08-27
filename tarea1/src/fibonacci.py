from math import sqrt

from decorators import benchmark


class Fibonacci:
    def __init__(self, sol_method: str | None = None) -> None:
        self.sol_method = "recursive"
        if sol_method is not None:
            self.sol_method = self.set_sol_method(sol_method)


    @benchmark
    def calculate(self, num: int) -> int:
        if self.sol_method == "recursive":
            return self.recursive_solution(num)
        elif self.sol_method == "iterative":
            return self.iter_solution(num)
        elif self.sol_method == "numeric":
            return self.numeric_solution(num)


    def recursive_solution(self, num: int) -> int:
        if num < 0:
            raise ValueError(f"The given integer must be non-negative, received {num=}")

        if num == 0:
            return 0
        if num == 1:
            return 1
        
        return self.recursive_solution(num - 1) + self.recursive_solution(num - 2)


    def iter_solution(self, num: int) -> int:
        if num < 0:
            raise ValueError(f"The given integer must be non-negative, received {num=}")
        
        if num == 0:
            return 0

        fib_sequence = [0, 1]
        for k in range(2, num+1):
            next_fib_num = fib_sequence[k-1] + fib_sequence[k-2]
            fib_sequence.append(next_fib_num)

        return fib_sequence[-1]
    

    def numeric_solution(self, num: int) -> int:
        sqrt_5 = sqrt(5)
        return round(1/sqrt_5 * ( ((1 + sqrt_5)/2)**num - ((1 - sqrt_5)/2)**num ))


    def set_sol_method(self, sol_method: str) -> None:
        valid_inputs = ["recursive", "iterative", "numeric"]
        if sol_method not in valid_inputs:
            raise ValueError(f"Not a valid input. Valid inputs are {valid_inputs}")
        
        self.sol_method = sol_method
