#!/usr/bin/env python

import time
import os

from typing import Protocol
from collections.abc import Callable
from multiprocessing import Pool


# Test routines
def loop_test() -> None:
    time.sleep(2)


def f(x: int) -> int:
    loop_test()
    return x * x * x


# Protocol and Runners
class Runnable(Protocol):
    """Protocol for run_function interface"""

    def run_function(self, f: Callable) -> None:
        raise NotImplementedError

    def report(self) -> None:
        raise NotImplementedError


class PoolRun:
    """
    Test Runnable for using multiprocess pool that uses cpus in parallel
    """

    def __init__(self):
        self.time_spent: float = 0
        pass

    # This cost more time because the function is not that expensive over Pool!
    def run_function(self, f: Callable) -> None:
        inject_int = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        start = time.monotonic()
        with Pool(os.cpu_count()) as p:
            print(p.map(f, inject_int))
        elapsed = time.monotonic() - start
        self.time_spent = elapsed
        print(f"Pool time: {elapsed}")

    def report(self) -> None:
        print(f"This took {self.time_spent}")


class NormalRun:
    """
    Test Runnable for normal function call that runs things sequentially
    """

    def __init__(self):
        pass

    def run_function(self, f: Callable) -> None:
        inject_int = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        start = time.monotonic()
        result = []
        for zzz in inject_int:
            result.append(f(zzz))
        print(f"{result=}")
        elapsed = time.monotonic() - start
        self.time_spent = elapsed
        print(f"Basic for loop: {elapsed}")

    def report(self) -> None:
        print(f"This took {self.time_spent}")


if __name__ == "__main__":
    print("This library")
    print(f"Using CPUs={os.cpu_count()}")
