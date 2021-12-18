import re
from common.input import auto_read_input


HEAD_NODE = "^"
EMPTY_NODE = "@"


class SnailNum(dict):
    """Binary tree to represent a snail number.

    It's a binary tree stored as a heap in a dict to keep it easily indexable
    and expandable.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self[0] = HEAD_NODE

    def __repr__(self):
        keys = self.keys()
        arr = [None] * (max(keys) + 1)
        for idx in keys:
            arr[idx] = self.get(idx)
        return str(arr)

    @classmethod
    def from_list(cls, l):
        d = {}
        for idx, val in enumerate(l):
            d[idx] = val
        return SnailNum(d)

    def get_left_idx(self, idx):
        return (2 * idx) + 1

    def get_right_idx(self, idx):
        return (2 * idx) + 2

    def get_parent_idx(self, idx):
        return (idx - 1) // 2

    def _magnitude(self, idx):
        left_idx = self.get_left_idx(idx)
        right_idx = self.get_right_idx(idx)

        left = self.get(left_idx)
        right = self.get(right_idx)

        if left is not None and right is not None:
            return 3 * self._magnitude(left_idx) + 2 * self._magnitude(
                right_idx
            )
        elif left is None and right is None:
            return self[idx]
        else:
            raise ValueError(
                f"SnailNum does not contain a pair at parent {idx}, left {left_idx}, right {right_idx}"
            )

    def magnitude(self):
        return self._magnitude(0)

    @classmethod
    def _merge(cls, a, b):
        # NOTE: Making this a heap made merging unnecessarily complex
        result = SnailNum()

        def _traverse(num, num_idx, result, result_idx):
            num_left_idx = num.get_left_idx(num_idx)
            num_right_idx = num.get_right_idx(num_idx)

            result_left_idx = result.get_left_idx(result_idx)
            result_right_idx = result.get_right_idx(result_idx)

            left = num.get(num_left_idx)
            right = num.get(num_right_idx)

            if left is not None and right is not None:
                result[result_idx] = EMPTY_NODE
                _traverse(num, num_left_idx, result, result_left_idx)
                _traverse(num, num_right_idx, result, result_right_idx)
            elif left is None and right is None:
                result[result_idx] = num[num_idx]
            else:
                raise ValueError(
                    f"SnailNum does not contain a pair at parent {num_idx}, left {num_left_idx}, right {num_right_idx}"
                )

        _traverse(a, 0, result, 1)  # all a goes to result head's left
        _traverse(b, 0, result, 2)  # all b goes to result head's right

        return result

    def add(self, other):
        return SnailNum._merge(self, other)


class SnailNumParser:
    @classmethod
    def parse(cls, str):
        # match all brackets, commas, and numbers
        pattern = r"([\[\]\,]|\d+)"

        snum = SnailNum()
        c_idx = 0

        for match in re.findall(pattern, str):
            if match == "[":
                left_idx = snum.get_left_idx(c_idx)
                left = snum.get(left_idx)
                if not left:
                    snum[left_idx] = EMPTY_NODE
                c_idx = left_idx
            elif match == "]":
                c_idx = snum.get_parent_idx(c_idx)
                pass
            elif match == ",":
                c_idx = snum.get_parent_idx(c_idx)
                right_idx = snum.get_right_idx(c_idx)
                right = snum.get(right_idx)
                if not right:
                    snum[right_idx] = EMPTY_NODE
                c_idx = right_idx
            elif match.isdigit():
                snum[c_idx] = int(match)

        return snum


def _parse_input(lines):
    ## Start here
    snail_nums = [SnailNumParser.parse(line) for line in lines]
    return snail_nums


def part1():
    _ = _parse_input(auto_read_input())
    return None


def part2():
    _ = _parse_input(auto_read_input())
    return None


if __name__ == "__main__":
    print(part1())
    print(part2())
