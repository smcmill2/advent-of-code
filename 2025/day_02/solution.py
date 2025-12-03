#!/usr/bin/env python
import re
from functools import reduce

def factors(n):
    return set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def get_ids():
    with open("input.txt", "r") as f:
        ids = f.read().strip().split(",")
        fl_list = list(map(lambda x: (int(x[0]), int(x[1])), map(lambda x: x.split("-"), ids)))

    return fl_list


def check_valid_id_range(first, last):
    invalid_ids = set()
    for _id in range(first, last + 1):
        _id = str(_id)
        if len(_id) % 2 == 1:
            continue
        else:
            mid = int(len(_id) // 2)
            if _id[:mid] == _id[mid:]:
                invalid_ids.add(int(_id))
    return invalid_ids

def check_additional_invalid_ids(first, last):
    invalid_ids = set()
    for _id in range(first, last + 1):
        _id = str(_id)
        facs = sorted(list(factors(len(_id))), reverse=True)
        for fac in facs[1:]:
            if fac > len(_id) // 2:  # can't be repeated
                continue
            elif len(_id) % fac != 0:
                continue
            else:
                needed_count = len(_id) // fac
                found = re.findall(_id[:fac], _id)
                if len(found) == needed_count and needed_count > 1:
                    invalid_ids.add(int(_id))

    return invalid_ids

if __name__ == "__main__":
    fl_list = get_ids()
    invalid_ids = set()
    additional_invalid_ids = set()
    for id_range in fl_list:
        invalid_ids.update(check_valid_id_range(*id_range))
        additional_invalid_ids.update(check_additional_invalid_ids(*id_range))

    print(f"{sum(invalid_ids)=}")
    print(f"{sum(additional_invalid_ids)=}")