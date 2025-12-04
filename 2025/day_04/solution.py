#!/usr/bin/env python
import numpy as np
from numpy._typing import NDArray
from scipy.ndimage import convolve


def read_input() -> NDArray:
    with open('input.txt', 'r') as f:
        rows = f.read().splitlines()
        grid = [[c == '@' for c in row] for row in rows]

    return np.array(grid).astype(int)


def get_neighbors(grid: NDArray) -> NDArray:
    neighbors = np.ones((3,3))
    neighbors[1,1] = 0

    num_neighbors = convolve(grid, neighbors, mode='constant', cval=0.0)
    return num_neighbors * grid


def remove_accessible(neighbors: NDArray, grid: NDArray) -> tuple[int, NDArray]:
    removable = (neighbors < 4) * grid
    total_removable = np.sum(removable)
    remaining = grid - removable

    return total_removable, remaining


if __name__ == '__main__':
    grid = read_input()
    neighbors = get_neighbors(grid)
    rolls_removed, remaining = remove_accessible(neighbors, grid)

    total_rolls = rolls_removed
    print(f"Initially Accessible: {total_rolls}")
    while rolls_removed > 0:
        neighbors = get_neighbors(remaining)
        rolls_removed, remaining = remove_accessible(neighbors, remaining)
        total_rolls += rolls_removed

    print(f"Exhaustively Accessible: {total_rolls}")
