from enum import Enum, IntEnum

from common.input import auto_read_input


class RPSType(IntEnum):
    # Core logic depends on these values
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


MOVE_MAP = {
    # Opponent
    'A': RPSType.ROCK,
    'B': RPSType.PAPER,
    'C': RPSType.SCISSORS,
    # You
    'X': RPSType.ROCK,
    'Y': RPSType.PAPER,
    'Z': RPSType.SCISSORS,
}


class GameResult(Enum):
    LOSE = 0
    TIE = 1
    WIN = 2


def _parse_input(lines):
    ## Start here
    moves = []
    for line in lines:
        opp_move_chr, your_move_chr = line.split(' ')
        moves.append([MOVE_MAP[opp_move_chr], MOVE_MAP[your_move_chr]])
    return moves


def _round_outcome_score(opp_move: RPSType, your_move: RPSType):
    if opp_move.value == your_move.value:
        return 3  # Tie
    elif (opp_move.value + 1) % 3 == your_move.value:
        return 6  # Win
    else:
        return 0  # Loss


def score(opp_move: RPSType, your_move: RPSType):
    return (your_move.value + 1) + _round_outcome_score(opp_move, your_move)


def part1():
    moves = _parse_input(auto_read_input())
    return sum(score(opp_move, your_move) for opp_move, your_move in moves)


def part2():
    _ = _parse_input(auto_read_input())
    return None


if __name__ == "__main__":
    print(part1())
    print(part2())
