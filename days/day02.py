import os

input = ""
if __name__ == "__main__":
    input = os.fdopen(3, "r").read().strip()


def part1(input=input):
    words, sentence = input.split("\n\n")
    words = words[6:].split(",")

    count = 0
    for word in words:
        for i in range(len(sentence) - len(word)):
            if sentence[i: i + len(word)] == word:
                count += 1

    return count


def part2(input=input):
    words, sentences = input.split("\n\n")
    words = words[6:].split(",")
    sentences = sentences.split("\n")

    sum = 0
    for sentence in sentences:
        seen = set()
        for word in words:
            for i in range(len(sentence) - len(word) + 1):
                if (
                    sentence[i: i + len(word)] == word
                    or sentence[i: i + len(word)][::-1] == word
                ):
                    seen |= set(range(i, i + len(word)))

        sum += len(seen)
    return sum


def part3(input=input):
    """
    Already did that on the 2024 AOC
    """
    pass
