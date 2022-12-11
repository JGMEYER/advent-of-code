import re
from collections import namedtuple

from common.input import auto_read_input

Move = namedtuple('Move', ["count", "from_", "to"])


def _parse_input(lines):
    stack_definition_end_idx = 0

    for idx, line in enumerate(lines):
        matches = re.findall(r'\s+\d', line)
        if matches:
            num_stacks = len(matches)
            stack_definition_end_idx = idx
            break

    stacks = [[] for i in range(num_stacks + 1)]

    for stack_line_idx in range(stack_definition_end_idx - 1, -1, -1):
        line = lines[stack_line_idx]

        for match in re.finditer(r'\[([A-Z])\]', line):
            stack_id = ((match.start()) // 4) + 1
            stacks[stack_id].append(match.groups(1)[0])

    moves = []

    for move_line_idx in range(stack_definition_end_idx + 2, len(lines)):
        line = lines[move_line_idx]
        match = re.search(r'move (\d+) from (\d+) to (\d+)', line)
        if match:  # should always be true
            count, from_, to = match.groups()
            move = Move(int(count), int(from_), int(to))
            moves.append(move)

    return stacks, moves


def make_move_9000(stacks, move):
    for i in range(move.count):
        item = stacks[move.from_].pop()
        stacks[move.to].append(item)


def make_move_9001(stacks, move):
    stacks[move.to].extend(stacks[move.from_][-move.count:])
    stacks[move.from_] = stacks[move.from_][:-move.count]


def _print_stacks(stacks):
    for idx, stack in enumerate(stacks):
        print(f'{idx} {stack}')


def tops_of_stacks(stacks):
    return ''.join([stack[-1] for stack in stacks[1:]])


def part1():
    stacks, moves = _parse_input(auto_read_input())
    for move in moves:
        make_move_9000(stacks, move)
    return tops_of_stacks(stacks)


def part2():
    stacks, moves = _parse_input(auto_read_input())
    for move in moves:
        make_move_9001(stacks, move)
    return tops_of_stacks(stacks)


if __name__ == "__main__":
    print(part1())
    print(part2())
