import collections
import re

import utilities.utils as utils

t = collections.namedtuple("lll", "weight children parent")

def parse_programs_to_nodes(programs):
    nodes = collections.defaultdict(dict)
    for program in programs:
        name = program[0]
        weight = int(program[1][1:-1])
        children = [re.sub(",", "", c) for c in program[3:]]
        nodes[name] = t(weight, children)
        for child in children:
            nodes[child]["parent"] = name
    return nodes


def find_bottom_program(nodes):
    for node in nodes:
        if not nodes[node].get("parent"):
            return node

def find_child_weights(children, nodes):
    for c in children:
        print c, nodes[c]
    #return [nodes[child]["weight"] for child in children]


def find_unbalanced_program(root, nodes):
    children = nodes[root]["children"]
    child_weights = find_child_weights(children, nodes)


def run(day):
    #programs = utils.parse_file_contents(day, reader_type="text_list", index=True)
    programs = [['pbga', '(66)'], ['xhth', '(57)'], ['ebii', '(61)'], ['havc', '(66)'], ['ktlj', '(57)'], ['fwft', '(72)', '->', 'ktlj,', 'cntj,', 'xhth'], ['qoyq', '(66)'], ['padx', '(45)', '->', 'pbga,', 'havc,', 'qoyq'], ['tknk', '(41)', '->', 'ugml,', 'padx,', 'fwft'], ['jptl', '(61)'], ['ugml', '(68)', '->', 'gyxo,', 'ebii,', 'jptl'], ['gyxo', '(61)'], ['cntj', '(57)']]
    nodes = parse_programs_to_nodes(programs)
    for node in nodes:
        print node, nodes[node]
    root = find_bottom_program(nodes)
    print root
    print find_unbalanced_program(root, nodes)
    #return redistribute_until_loop_found(banks), redistribute_until_loop_found(banks, num_cycles=True)

run("7")


"""
1. get root node
2. for every child of the root
    - calculate it's weight
    - if min(weight) == max(weight)
        continue
    - if 
"""
