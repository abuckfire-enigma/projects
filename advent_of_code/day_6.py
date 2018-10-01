#--- Day 6: Memory Reallocation ---
import copy
import os
import logging
import sys
import utilities.utils as utils

NUMBER_OF_BANKS = 16


def set_new_bank_value(bank_value, dist_amount, remainder):
    if dist_amount == 0 and remainder > 0:
        return bank_value + 1, remainder - 1
    return bank_value + dist_amount, remainder


def redistribute(banks, num_banks=NUMBER_OF_BANKS):
    bank_index, max_bank_amount = banks.index(max(banks)), max(banks)
    dist_amount, remainder = divmod(max_bank_amount, num_banks - 1)
    new_banks = copy.deepcopy(banks)

    for i in range(bank_index + 1, num_banks):
        new_banks[i], remainder = set_new_bank_value(new_banks[i], dist_amount, remainder)

    for j in range(bank_index):
        new_banks[j], remainder = set_new_bank_value(new_banks[j], dist_amount, remainder)

    new_banks[bank_index] = remainder
    return new_banks


def redistribute_until_loop_found(banks, num_cycles=False):
    previous_distributions = []
    current_distribution = banks
    iterations = 0
    while current_distribution not in previous_distributions:
        previous_distributions.append(current_distribution)
        current_distribution = redistribute(current_distribution)
        iterations += 1

    if num_cycles:
        return iterations - previous_distributions.index(current_distribution)

    return iterations


def run(day):
    banks = utils.parse_file_contents(day, reader_type="list", index=True)[0]
    return redistribute_until_loop_found(banks), redistribute_until_loop_found(banks, num_cycles=True)
    # note to self: try this problem with a recursive solution
