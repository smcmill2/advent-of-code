#!/usr/bin/env python
import numpy as np


def read_input():
    with open("input.txt", "r") as f:
        banks = f.readlines()

    print(bank)

    return [list(map(lambda x: int(x), bank.strip())) for bank in banks]


def max_jolts(bank: list[int]) -> int:
    mj = 0
    d0 = 0
    for i in range(len(bank) - 1):
        if bank[i] > d0 and mj // 10 <= d0:
            d0 = bank[i]
        else:
            continue

        d1 = 0
        for j in range(i + 1, len(bank)):
            if bank[j] > d1:
                d1 = bank[j]
        mj = max([mj, d0 * 10 + d1])

        if mj // 10 == 9:
            break

    return mj


def max_sub_jolts_idx(bank: list[int], start: int = 0, end: int = 1) -> int:
    if end == 0:
        sub_bank = bank[start:]
    else:
        sub_bank = bank[start:-end]

    return int(np.argmax(sub_bank))


def dyn_max_jolts(bank: list[int], num_digits: int = 2) -> int:
    digits = []
    idx = 0

    while idx < len(bank) - (num_digits - len(digits) - 1) and len(digits) < num_digits:
        offset = idx
        idx = max_sub_jolts_idx(bank, offset, num_digits - len(digits) - 1)
        digits.append(bank[idx + offset])
        idx = idx + offset + 1

    return int(''.join([str(d) for d in digits]))

if __name__ == "__main__":
    banks = read_input()

    for num_batteries in [2, 12]:
        max_jolt_list = list(map(lambda x: dyn_max_jolts(x, num_digits=num_batteries), banks))
        print(f"{num_batteries=} {sum(max_jolt_list)=}")
