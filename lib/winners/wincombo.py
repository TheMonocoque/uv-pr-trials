"""
trying some random and itertools
"""

from random import choice, choices, sample
from itertools import permutations, combinations


def demo_combo_choice_sample() -> None:
    """demo combo"""

    print("Combination...")
    lister: list = ["A", "B", "C"]
    for combo in combinations(range(4), 2):
        print(combo)

    print("Permutations")
    for combo in permutations(lister):
        print(combo)

    print(choice(lister))
    print(choices(lister, k=2))

    print("\nTwo winners...")
    print("winners=", sample(lister, k=2))
