#!/usr/bin/env python

"""
Trigger event cache detect and dynamic exclusion skip
"""

# from dataclasses import dataclass
# from functools import lru_cache
import time

# @dataclass
class EventCache:
    """example exercise on caching events triggered extrinsically"""

    # dataclass does not allow dict?!
    def __init__(self):
        self.event_name: str = "Start"
        self.event_timeout_sec: int = 600
        self.event_cache: dict = {}

    def update(self, name: str, timeout: int = 600) -> None:
        """update the event timeline sim"""

        # you can only set the event and its timeout once
        if name in self.event_cache:
            if time.monotonic() - self.event_cache[name] > 10:
                del self.event_cache[name]
            time.sleep(1)
            return

        print(f"Updating {name=} with timeout {timeout} seconds ...")
        self.event_name = name
        self.event_timeout_sec = timeout
        self.event_cache[name] = time.monotonic()
        time.sleep(1)
        return
