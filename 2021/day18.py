import math
import re

from common.input import auto_read_input


HEAD_NODE = "^"
EMPTY_NODE = "@"


class SnailNum(dict):
    """Binary tree to represent a snail number.

    It's a binary tree stored as a heap in a dict to keep it easily indexable
    and expandable.
    """

    ORDER_PREORDER = -1
    ORDER_INORDER = 0
    ORDER_POSTORDER = 1

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self[0] = HEAD_NODE

    def __repr__(self):
        return SnailNumParser.unparse(self)

    @classmethod
    def from_list(cls, l):
        d = {}
        for idx, val in enumerate(l):
            d[idx] = val
        return SnailNum(d)

    @classmethod
    def get_left_idx(cls, idx):
        return (2 * idx) + 1

    @classmethod
    def get_right_idx(cls, idx):
        return (2 * idx) + 2

    @classmethod
    def get_parent_idx(cls, idx):
        return (idx - 1) // 2

    def get_left(self, idx):
        left_idx = SnailNum.get_left_idx(idx)
        return left_idx, self.get(left_idx)

    def get_right(self, idx):
        right_idx = SnailNum.get_right_idx(idx)
        return right_idx, self.get(right_idx)

    def get_parent(self, idx):
        parent_idx = SnailNum.get_parent_idx(idx)
        return parent_idx, self.get(parent_idx)

    @classmethod
    def depth(cls, idx):
        depth = 0
        while idx > 0:
            idx = SnailNum.get_parent_idx(idx)
            depth += 1
        return depth

    def _foreach(self, func, order, cur_idx=0):
        cur = self.get(cur_idx)

        if cur is None:
            return

        left_idx, left = self.get_left(cur_idx)
        right_idx, right = self.get_right(cur_idx)

        if order == SnailNum.ORDER_PREORDER:
            func(cur_idx, cur)
            self._foreach(func, order, left_idx)
            self._foreach(func, order, right_idx)
        elif order == SnailNum.ORDER_INORDER:
            self._foreach(func, order, left_idx)
            func(cur_idx, cur)
            self._foreach(func, order, right_idx)
        elif order == SnailNum.ORDER_POSTORDER:
            self._foreach(func, order, left_idx)
            self._foreach(func, order, right_idx)
            func(cur_idx, cur)

    def foreach(self, func, order: int):
        self._foreach(func, order)

    def _magnitude(self, idx):
        # TODO cleanup to use get_left and get_right
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

        # TODO refactor to use foreach?
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

    @classmethod
    def _reduce(cls, snum):
        idx = 0
        order_type = cls.ORDER_INORDER
        order_traversal = []

        def func(k, v):
            order_traversal.append((k, v))

        snum.foreach(func, order_type)

        # seed the loop
        num_explosions = 1
        num_splits = 1

        while num_explosions > 0 or num_splits > 0:
            num_explosions = 0
            num_splits = 0

            for k, v in order_traversal:
                if type(v) == int and cls.depth(k) == 5:
                    parent_idx = SnailNum.get_parent_idx(k)
                    snum._explode(parent_idx)
                    order_traversal = []
                    snum.foreach(func, order_type)
                    num_explosions += 1
                    break

            idx = 0
            while num_explosions == 0 and idx < len(order_traversal):
                k, v = order_traversal[idx]
                if type(v) == int and v > 9:
                    snum._split(k)
                    order_traversal = []
                    snum.foreach(func, order_type)
                    num_splits += 1
                    break
                idx += 1

        return snum

    def add(self, other):
        result = SnailNum._merge(self, other)
        result = SnailNum._reduce(result)
        return result

    def _explode(self, idx):
        inorder_traversal = []

        def func(k, v):
            inorder_traversal.append((k, v))

        self.foreach(func, SnailNum.ORDER_INORDER)
        inorder_traversal = [k for k, v in inorder_traversal if type(v) == int]

        left_idx, left = self.get_left(idx)
        right_idx, right = self.get_right(idx)

        # Scan list to find neighbors for each value, if exists
        closest_left_search_idx = inorder_traversal.index(left_idx) - 1
        closest_right_search_idx = inorder_traversal.index(right_idx) + 1

        if closest_left_search_idx >= 0:
            closest_left_idx = inorder_traversal[closest_left_search_idx]
            self[closest_left_idx] += left

        if closest_right_search_idx < len(inorder_traversal):
            closest_right_idx = inorder_traversal[closest_right_search_idx]
            self[closest_right_idx] += right

        # Set current node value to 0
        self[idx] = 0
        del self[left_idx]
        del self[right_idx]

    def _split(self, idx):
        cur = self[idx]
        left_idx = self.get_left_idx(idx)
        right_idx = self.get_right_idx(idx)

        new_left = math.floor(cur / 2)
        new_right = math.ceil(cur / 2)

        self[idx] = EMPTY_NODE
        self[left_idx] = new_left
        self[right_idx] = new_right


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

    @classmethod
    def unparse(cls, snum):
        def _dfs(cur_idx):
            cur = snum.get(cur_idx)
            left_idx = SnailNum.get_left_idx(cur_idx)
            right_idx = SnailNum.get_right_idx(cur_idx)

            if cur in (EMPTY_NODE, HEAD_NODE):
                return [_dfs(left_idx), _dfs(right_idx)]
            elif type(cur) == int:
                return cur

        arr = _dfs(0)
        return str(arr).replace(" ", "")


def _parse_input(lines):
    ## Start here
    snail_nums = [SnailNumParser.parse(line) for line in lines]
    return snail_nums


def _sum_all(snums):
    result = snums[0]

    for idx in range(1, len(snums)):
        result = result.add(snums[idx])

    return result


def _max_mag_from_any_two(snums):
    max_mag = -math.inf
    for a_idx, a in enumerate(snums):
        for b_idx, b in enumerate(snums):
            if a_idx == b_idx:
                continue
            max_mag = max(max_mag, a.add(b).magnitude())
    return max_mag


def part1():
    snums = _parse_input(auto_read_input())
    return _sum_all(snums).magnitude()


def part2():
    # This one takes a minute or so, but not crazy long
    snums = _parse_input(auto_read_input())
    return _max_mag_from_any_two(snums)


if __name__ == "__main__":
    print(part1())
    print(part2())
