import re
from collections import namedtuple

from common.input import auto_read_input

RangePair = namedtuple('RangePair', ['min_a', 'max_a', 'min_b', 'max_b'])


def one_range_fully_contains_other(min_a, max_a, min_b, max_b):
    return (min_a <= min_b <= max_b <= max_a) or (min_b <= min_a <= max_a <= max_b)


def ranges_overlap_at_all(min_a, max_a, min_b, max_b):
    return (
        one_range_fully_contains_other(min_a, max_a, min_b, max_b)
        or (min_a <= min_b <= max_a <= max_b)
        or (min_b <= min_a <= max_b <= max_a)
    )


def _parse_input(lines):
    ## Start here
    range_pairs = []
    for line in lines:
        groups = re.search(r'(\d+)\-(\d+),(\d+)\-(\d+)', line).groups()
        range_pair = RangePair(*(int(val) for val in groups))
        range_pairs.append(range_pair)
    return range_pairs


def part1():
    range_pairs = _parse_input(auto_read_input())
    return sum(one_range_fully_contains_other(*range_pair) for range_pair in range_pairs)


def part2():
    range_pairs = _parse_input(auto_read_input())
    return sum(ranges_overlap_at_all(*range_pair) for range_pair in range_pairs)


if __name__ == "__main__":
    print(part1())
    print(part2())
