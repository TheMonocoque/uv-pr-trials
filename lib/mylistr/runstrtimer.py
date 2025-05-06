#!usr/bin/env python

"""
test perf on string join
"""

import time
from itertools import repeat


def run_loop_test() -> None:
    """repeat faster loop"""

    # loop faster
    start = time.monotonic()
    for _ in range(100_000_000):
        _ = "boomv4"
    elapsed = time.monotonic() - start
    print(f"range loop: {elapsed:.5f}")

    start = time.monotonic()
    for _ in repeat(None, 100_000_000):
        _ = "boomv4"
    elapsed = time.monotonic() - start
    print(f"repeat loop: {elapsed:.5f}")
