# --- Day 3: Spiral Memory --- https://github.com/dainnilsson/adventofcode-2017/blob/master/day3.py
import math
import os
import utilities.utils as utils

def pos(index):
    """WIP
    """
    r = int(math.sqrt(index - 1) + 1) // 2
    d = 2 * r - 1
    i = index - d*d - 1
    return (r, i - r + 1) if i < d else (r - i + d, r) if i < 2 *d + 2 else \
        (-r, r - i - 1 + 2 * d + 2) if i < 3 * d + 2 else (i - r - 3 * d - 2, -r)

def sum_iterable(iterable):
    return sum([abs(n) for n in iterable])

def find_sum_larger_than_input(index):
    """WIP
    """
    m, s, i = {(0, 0): 1}, 1, 2
    while s <= index:
        (x, y), i = pos(i), i + 1
        m[x, y] = s = sum(m.get((x + j % 3 - 1, y + j//3), 0) for j in range(-3, 6))
    return s

def main():
    squares = int(utils.read_input(os.path.join("fixtures", "input_3.txt")))
    utils.pretty_print(3, sum_iterable(pos(squares)), find_sum_larger_than_input(squares))

if __name__ == "__main__":
    main()
