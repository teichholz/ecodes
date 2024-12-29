import os
from itertools import batched

input = os.fdopen(3, "r").read().strip()


def part1(input=input):
    cost = {"A": 0, "B": 1, "C": 3}
    return sum(cost[c] for c in input)


def part2(input=input):
    b = list(batched(input, n=2))
    cost_single = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}
    cost = {
        (l, r): cost_single[l] + cost_single[r] + (2 if "x" not in l + r else 0)
        for l in cost_single.keys()
        for r in cost_single.keys()
    }
    return sum(cost[c] for c in b)


def part3(input=input):
    b = list(batched(input, n=3))
    cost_single = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}

    def group_bonus(non_xs: int):
        if non_xs == 3:
            return 2 * non_xs
        if non_xs == 2:
            return non_xs
        return 0

    cost = {
        (c1, c2, c3): cost_single[c1]
        + cost_single[c2]
        + cost_single[c3]
        + group_bonus(3 - sum(1 if c == "x" else 0 for c in c1 + c2 + c3))
        for c1 in cost_single.keys()
        for c2 in cost_single.keys()
        for c3 in cost_single.keys()
    }

    return sum(cost[c] for c in b)
