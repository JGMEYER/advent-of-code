from collections import defaultdict
import re


def _superstrip(s):
    """Remove all leading and trailing spaces in addition to duplicate spaces."""
    pattern = re.compile(r"\s+")
    return pattern.sub(" ", s.strip())


class Board:
    def __init__(self, board_str):
        self.row_counts = [0, 0, 0, 0, 0]
        self.col_counts = [0, 0, 0, 0, 0]

        def _clean_row(row):
            return _superstrip(row).split(" ")

        self.board = []  # for debugging
        self.loc_map = {}
        self.marked = {}  # for debugging
        self.unmarked_score = 0
        for row_idx, row in enumerate(board_str.split("\n")):
            self.board.append([])
            for col_idx, num_str in enumerate(_clean_row(row)):
                num = int(num_str)
                self.board[-1].append(num)
                self.loc_map[num] = [row_idx, col_idx]
                self.marked[num] = False
                self.unmarked_score += num

    def mark(self, num):
        if num not in self.loc_map:
            return False

        r, c = self.loc_map[num]

        self.row_counts[r] += 1
        self.col_counts[c] += 1
        self.marked[num] = True
        self.unmarked_score -= num

        has_win = self.row_counts[r] == 5 or self.col_counts[c] == 5
        return has_win

    def __repr__(self):
        str = ""
        str += f"rows: {self.row_counts}\ncols: {self.col_counts}\n"
        for row in self.board:
            marked_row = ["X" if self.marked[num] else num for num in row]
            str += "{0:2} {1:2} {2:2} {3:2} {4:2}\n".format(*marked_row)
        return str


def _read_input(filename):
    with open(filename) as f:
        inputs = f.read().strip().split("\n\n")

    nums_drawn = [int(num) for num in inputs[0].split(",")]
    boards = [Board(board_str) for board_str in inputs[1:]]

    return nums_drawn, boards


def part1(input_filename):
    nums_drawn, boards = _read_input(input_filename)

    for num in nums_drawn:
        for b in boards:
            has_win = b.mark(num)
            if has_win:
                return num * b.unmarked_score

    return None


def part2(input_filename):
    nums_drawn, boards = _read_input(input_filename)
    incomplete_boards = set(boards)

    for num in nums_drawn:
        for b in boards:
            if b not in incomplete_boards:
                continue

            has_win = b.mark(num)
            if has_win:
                incomplete_boards.remove(b)
                # This was the last board to win
                if not incomplete_boards:
                    return num * b.unmarked_score

    return None


if __name__ == "__main__":
    print(part1("inputs/day4.txt"))
    print(part2("inputs/day4.txt"))
