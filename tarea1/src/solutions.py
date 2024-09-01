from typing import Protocol

import numpy as np


class PathCountSolution(Protocol):
    def count(self, n: int, m: int) -> int:
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...


class RecursiveSolution:
    def count(self, n: int, m: int) -> int:
        if n == 1 or m == 1:
            return 1
        
        return self.count(n - 1, m) + self.count(n, m - 1)
    
    def __str__(self) -> str:
        return "Recursive"
    
    def __repr__(self) -> str:
        return "Recursive"
    

class DinamycSolution:
    def count(self, n: int, m: int) -> int:
        num_paths = np.ones((n, m), dtype=np.uint64)

        for i in range(1, n):
            for j in range(1, m):
                num_paths[i,j] = num_paths[i-1,j] + num_paths[i,j-1]
        
        return num_paths[n-1,m-1]
    
    def __str__(self) -> str:
        return "Dynamic"
    
    def __repr__(self) -> str:
        return "Dynamic"
    

class CombinatorialSolution:
    def count(self, n: int, m: int) -> int:
        log_numerator = np.sum(np.log(np.arange(1, (n+m-2)+1)))
        log_denominator = np.sum(np.log(np.arange(1, (n-1)+1))) + np.sum(np.log(np.arange(1, (m-1)+1)))
        log_result = log_numerator - log_denominator
        return round(np.exp(log_result))
    
    def __str__(self) -> str:
        return "Combinatorial"
    
    def __repr__(self) -> str:
        return "Combinatorial"
