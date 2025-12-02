#!/usr/bin/env python

def get_instructions():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        return [(-1 if line[0] == "L" else 1) * int(line[1:]) for line in lines]

def rotate_dial(distance: int, cur_pos: int=50) -> tuple[int, int, int]:
    num_zeros = 0

    move = cur_pos + distance
    pos = move % 100

    if distance > 0:
        crosses = max(0, (move - 1) // 100 - (cur_pos - 1) // 100)
    elif distance < 0:
        crosses = max(0, cur_pos // 100 - move // 100)
    else:
        crosses = 0

    if pos == 0:
        num_zeros += 1

    print(f"{cur_pos=}, {distance=}, {pos=}, {num_zeros=}, {crosses=}")

    return pos, num_zeros, crosses

if __name__ == '__main__':
    pos = 50
    instructions = get_instructions()
    num_zeros = 0
    num_passes = 0
    for instruction in instructions:
        pos, zeros, passes = rotate_dial(instruction, cur_pos=pos)
        num_zeros += zeros
        num_passes += passes

    print(f"Number of zeros: {num_zeros}, Number of zero crosses: {num_passes}")
