# --- Day 2: Corruption Checksum ---
import os
import utilities.utils as utils


def compute_max_diff(arr):
    """
    Takes numbers and returns the difference between the largest and smallest
    Args:
        List of numbers
    Returns:
        int: diff between max and min values in the list
    """
    return max(arr) - min(arr)


def compute_rem_0(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length):
            if i == j:
                continue
            quotient, remainder = divmod(arr[i], arr[j])
            if remainder == 0:
                return quotient


def compute_checksum(matrix):
    """
    Computes checksum of matrix
    Args:
        matrix: list of lists
    Returns:
        integer of the checksum
    """
    return sum([compute_max_diff(row) for row in matrix])


def compute_sum_even_divide(matrix):
    return sum([compute_rem_0(row) for row in matrix])


def main():
    matrix = utils.read_matrix_input(os.path.join("fixtures", "input_2.txt"))
    utils.pretty_print(2, compute_checksum(matrix), compute_sum_even_divide(matrix))

if __name__ == "__main__":
    main()
