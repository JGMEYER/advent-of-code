import re

from common.input import auto_read_input


class DeterministicDice:
    def __init__(self):
        self._last_roll = 0

    def roll_3(self):
        rolls = (
            self._last_roll + 1,
            self._last_roll + 2,
            self._last_roll + 3,
        )
        self._last_roll += 3
        return rolls


def new_loc(starting_pos, move_num):
    starting_pos = (starting_pos - 1) % 10
    ending_pos = (starting_pos + move_num) % 10 + 1
    return ending_pos


def _parse_input(lines):
    ## Start here
    pattern = r"Player \d starting position: (\d+)"
    p1_pos = int(re.match(pattern, lines[0]).groups()[0])
    p2_pos = int(re.match(pattern, lines[1]).groups()[0])
    return p1_pos, p2_pos


def play_game(p1_pos, p2_pos):
    p1_score = 0
    p2_score = 0

    dice = DeterministicDice()

    while True:
        for dice_val in dice.roll_3():
            p1_pos = new_loc(p1_pos, dice_val)
        p1_score += p1_pos

        if p1_score >= 1000:
            break

        for dice_val in dice.roll_3():
            p2_pos = new_loc(p2_pos, dice_val)
        p2_score += p2_pos

        if p2_score >= 1000:
            break

    return min(p1_score, p2_score) * dice._last_roll


def part1():
    p1_pos, p2_pos = _parse_input(auto_read_input())
    return play_game(p1_pos, p2_pos)


def part2():
    _ = _parse_input(auto_read_input())
    return None


if __name__ == "__main__":
    print(part1())
    print(part2())
