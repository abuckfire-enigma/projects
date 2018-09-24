import argparse
import importlib
import sys

import utilities.utils as utils


def main():
    parser = argparse.ArgumentParser("Execute an advent of code day")
    parser.add_argument("-day", type=str, required=True, help="Specify an advent of code day to execute")
    args = parser.parse_args()

    advent_day = importlib.import_module('day_' + args.day)
    part_1, part_2 = advent_day.run(args.day)
    utils.pretty_print(args.day, 1, part_1)
    utils.pretty_print(args.day, 2, part_2)


if __name__ == "__main__":
    main()
