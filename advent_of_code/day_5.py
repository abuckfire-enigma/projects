# --- Day 2: Corruption Checksum ---
import os
import utilities.utils as utils


def incrementer(curr_offset, incr):
    return curr_offset + incr


def increment_conditionally(curr_offset, incr):
    if curr_offset >= 3:
        return curr_offset - incr
    return curr_offset + incr


def escape_cycle(offsets, condition, incr=1):
    curr = 0
    num_moves = 0
    while curr < len(offsets):
        num_moves += 1
        offset_value = offsets[curr]
        offsets[curr] = condition(offset_value, incr)
        curr += offset_value
 
    return num_moves


def main():
    offsets = utils.read_list_input(os.path.join("fixtures", "input_5.txt"))
    utils.pretty_print(5, escape_cycle(offsets, incrementer),
                       escape_cycle(offsets, increment_conditionally))

if __name__ == "__main__":
    main()
