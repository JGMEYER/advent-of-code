from enum import IntEnum
from typing import List

from common.input import read_input


class IntcodeParser:

    class OPCODE(IntEnum):
        ADD = 1
        MULTIPLY = 2
        TERMINATE = 99

    def __init__(self, ops_str: str):
        self.index = -4
        self.ops = [int(c) for c in ops_str.split(',')]

    def process(self, instruction: List[int]):
        op, p1, p2, pdest = instruction
        if op == self.OPCODE.ADD:
            self.ops[pdest] = self.ops[p1] + self.ops[p2]
        elif op == self.OPCODE.MULTIPLY:
            self.ops[pdest] = self.ops[p1] * self.ops[p2]
        else:
            raise ValueError(f"Invalid operation {op}")

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 4
        try:
            if self.ops[self.index] == 99:
                raise StopIteration
            instruction = self.ops[self.index:self.index+4]
        except IndexError:
            raise StopIteration
        return instruction

    def __getitem__(self, idx: int):
        return self.ops[idx]

    def __setitem__(self, idx: int, value: int):
        self.ops[idx] = value


def part1() -> int:
    ops_str = read_input(day=2)[0]
    parser = IntcodeParser(ops_str)

    # 1202 program alarm state
    parser[1] = 12
    parser[2] = 2

    for instruction in parser:
        parser.process(instruction)
    return parser[0]


def part2() -> int:
    ops_str = read_input(day=2)[0]

    for noun in range(100):
        for verb in range(100):
            parser = IntcodeParser(ops_str)

            parser[1] = noun
            parser[2] = verb

            for instruction in parser:
                parser.process(instruction)

            if parser[0] == 19690720:
                return 100 * noun + verb

    return -1


if __name__ == "__main__":
    print(part1())
    print(part2())
