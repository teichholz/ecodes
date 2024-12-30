import day01

from helpers import readday


def test_day01_1():
    out = day01.part1(readday(1, 1, 2024))
    assert out == 1404


def test_day01_2():
    out = day01.part2(readday(1, 2, 2024))
    assert out == 5237


def test_day01_3():
    out = day01.part3(readday(1, 3, 2024))
    assert out == 28225
