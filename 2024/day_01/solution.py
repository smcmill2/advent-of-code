#!/usr/bin/env python
from collections import defaultdict
from pathlib import Path


def parse_input(input_str: str) -> tuple[list[int], list[int]]:
    tuples = list(map(lambda x: tuple(x.split()), input_str.strip().split("\n")))
    list1, list2 = zip(*tuples)
    return list(map(int, list1)), list(map(int, list2))


def compare_lists(list1: list[int], list2: list[int]) -> bool:
    list1.sort()
    list2.sort()

    diff = 0
    for _l1, _l2 in zip(list1, list2):
        diff += abs(_l1 - _l2)

    return diff


def similarity_score(list1: list[int], list2: list[int]) -> float:
    list1.sort()
    list2_counts = defaultdict(int)
    for _l2 in list2:
        list2_counts[_l2] += 1

    score = 0
    for _l1 in list1:
        score += _l1 * list2_counts.get(_l1, 0)

    return score


if __name__ == "__main__":
    input_file = Path("input.txt")
    with input_file.open("r") as f:
        input_str = f.read()
    input_data = parse_input(input_str)
    print(f"Solution 1: {compare_lists(*input_data)}")
    print(f"Solution 2: {similarity_score(*input_data)}")
