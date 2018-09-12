# --- Day 1: Inverse Capcha ---

import os
import utilities.utils as utils


def sum_if_match_next_digit(number):
    """
    Adds int in a number if int[0] == int[1] and if int[0] == int[len(number)]
    Returns:
        integer of the sum
    """
    circular_condition = [int(number[0]) if number[0] == number[-1:] else 0][0]
    return sum([int(number[i]) for i in range(len(number)-1) if number[i] == number[i+1]]) + circular_condition


def sum_if_match_halfway_digit(number):
    """
    For a given number, checks to see if it equals the digit halfway away from it.
    If it does, add it, otherwise, continue
    Returns:
        integer sum of result
    """
    midway_point = len(number) / 2
    return sum([int(number[i]) for i in range(midway_point) if number[i] == number[i + midway_point]]) * 2


def main():
    number = utils.read_input(os.path.join("fixtures", "input_1.txt"))
    utils.pretty_print(1, sum_if_match_next_digit(number), sum_if_match_halfway_digit(number))

if __name__ == "__main__":
    main()