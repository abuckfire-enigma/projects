def pretty_print(day, day_p1, day_p2):
    print "The answer to day {}, part 1 is: {}".format(day, day_p1)
    print "The answer to day {}, part 2 is: {}".format(day, day_p2)

def read_input(in_file):
    with open(in_file, "r") as reader:
        return reader.read().strip()

def read_matrix_input(in_file):
    with open(in_file, "r") as reader:
        return [map(int, line.split()) for line in reader]

def read_input_text(in_file):
    with open(in_file, "r") as reader:
        return [line.split() for line in reader]