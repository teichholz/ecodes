import os

input = ""
if __name__ == "__main__":
    input = os.fdopen(3, "r").read().strip()


def part1(input=input):
    nails = list(map(int, input.splitlines()))

    m = min(nails)
    return sum(n - m for n in nails)


def part2(input=input):
    return part1(input)


def part3(input=input):
    nails = list(map(int, input.splitlines()))

    nails.sort()
    med_i = len(nails) // 2
    med = nails[med_i]

    return sum(med - n for n in nails[:med_i]) + sum(n - med for n in nails[med_i:])
