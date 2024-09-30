from pathlib import Path
from time import perf_counter
from typing import Any, Callable


def benchmark(func: Callable) -> Callable:
    avoid_deletion = set()

    def wrapper(*args: tuple[Any]) -> Any:
        nonlocal avoid_deletion

        # Benchmark the function call
        self, n, m = args
        start_time = perf_counter()
        result = func(self, n, m)
        stop_time = perf_counter()
        total_time = stop_time - start_time

        # Save the benchmark to a file
        data_path = Path("../data")
        if not data_path.exists():
            Path.mkdir(data_path)

        file_path = data_path / f"{self.solution_method}_benchmark.txt"
        if file_path.is_file() and file_path not in avoid_deletion:
            file_path.unlink()
            avoid_deletion.add(file_path)

        with Path.open(file_path, "a") as benchmark:
            benchmark.write(f"{n}, {m}, {total_time}\n")

        return result

    return wrapper
