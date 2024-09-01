from typing import Callable, Any
from time import perf_counter
import os


def benchmark(func: Callable) -> Callable:
    avoid_deletion = set()

    def wrapper(*args: tuple[Any]):
        nonlocal avoid_deletion

        # Benchmark the function call
        self, n, m = args
        start_time = perf_counter()
        result = func(self, n, m)
        stop_time = perf_counter()
        total_time = stop_time - start_time

        # Save the benchmark to a file
        data_path = "../data"
        if not os.path.isdir(data_path):
            os.makedirs(data_path)

        file_path = f"{data_path}/{self.solution_method}_benchmark.txt"
        if os.path.isfile(file_path) and file_path not in avoid_deletion:
            os.remove(file_path)
            avoid_deletion.add(file_path)
            
        with open(file_path, "a") as benchmark:
            benchmark.write(f"{n}, {m}, {total_time}\n")

        return result
    
    return wrapper
