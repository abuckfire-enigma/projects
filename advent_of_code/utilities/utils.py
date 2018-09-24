import os

def pretty_print(day, part, ans):
    print "The answer to day {}, part {} is: {}".format(day, part, ans)


def get_input_path(day):
    return os.path.join("fixtures", "input_" + day + ".txt")


def parse_file_contents(day, reader_type="txt", index=False):
    path = get_input_path(day)
    with open(path, "r") as reader:
        if reader_type == "txt":
            return reader.read().strip()

        if reader_type == "list":
            if index:
                return [map(int, line.split()) for line in reader]
            return [map(int, line.split())[0] for line in reader]

        if reader_type == "text_list":
            return [line.split() for line in reader]
