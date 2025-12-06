#!/usr/bin/env python
from dataclasses import dataclass, field


@dataclass(order=True)
class Node:
    lower: int
    upper: int=field(compare=False)


def read_input() -> tuple[list[Node], list[int]]:
    id_ranges = []
    ids = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            id_range = line.strip().split('-')
            if len(id_range) == 2:
                id_ranges.append(Node(int(id_range[0]), int(id_range[1])))
            elif len(id_range) == 1 and id_range[0] != '':
                ids.append(int(id_range[0]))
            else:
                continue

    return id_ranges, ids


def find_fresh_ids(id_ranges: list[Node], ids: list[tuple[int, int]]) -> list[int]:
    fresh_ids = []
    for _id in ids:
        for id_range in id_ranges:
            if _id in range(id_range.lower, id_range.upper+1):
                fresh_ids.append(_id)
                break

    return fresh_ids


def total_fresh_ingredients(id_ranges: list[Node]) -> int:
    num_fresh = 0
    cur_max = 0
    prev_max = 0
    for _id in sorted(id_ranges):
        cur_max = max(cur_max, _id.upper+1)
        cur_min = max(prev_max, _id.lower)
        new_range = (cur_max-cur_min)
        if new_range > 0:
            num_fresh += new_range

        prev_max = cur_max

    return num_fresh


if __name__ == '__main__':
    id_ranges, ids = read_input()
    id_ranges = sorted(id_ranges)

    fresh_ids = find_fresh_ids(id_ranges, ids)
    print(f"Found {len(fresh_ids)} fresh ids out of {len(ids)} ids")
    total_fresh_ids = total_fresh_ingredients(id_ranges)
    print(f"Max fresh ingredients: {total_fresh_ids}")

