import os

from helpers import add, dirs4, dirs8

input = ""
if __name__ == "__main__":
    input = os.fdopen(3, "r").read().strip()


def part1(input=input):
    return solve(input, dirs4)


def part2(input=input):
    return part1(input)


def part3(input=input):
    return solve(input, dirs8)


def solve(input, dirs):
    lines = input.splitlines()
    grid = {
        (row, col)
        for row, line in enumerate(lines)
        for col, c in enumerate(line)
        if c == "#"
    }
    sum = 0
    while grid:
        sum += len(grid)

        # remove outer wall
        to_delete = set()
        for pos in grid:
            for dir in dirs:
                if add(pos, dir) not in grid:
                    to_delete.add(pos)
                    break
        grid -= to_delete

    return sum
