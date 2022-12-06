from common.input import auto_read_input

MOVE_MAP = {
    # Opponent
    'A': 0,  # Rock
    'B': 1,  # Paper
    'C': 2,  # Scissors
    # You
    'X': 0,  # Rock     or Lose
    'Y': 1,  # Paper    or Draw
    'Z': 2,  # Scissors or Win
}


def _parse_input(lines):
    ## Start here
    moves = []
    for line in lines:
        opp_move_chr, your_move_chr = line.split(' ')
        moves.append([MOVE_MAP[opp_move_chr], MOVE_MAP[your_move_chr]])
    return moves


def _round_outcome_score(opp_move: int, your_move: int) -> int:
    if opp_move == your_move:
        return 3  # Tie
    elif (opp_move + 1) % 3 == your_move:
        return 6  # Win
    else:
        return 0  # Loss


def score(opp_move: int, your_move: int) -> int:
    return (your_move + 1) + _round_outcome_score(opp_move, your_move)


def determine_move(opp_move: int, desired_outcome: int):
    match desired_outcome:
        case 0:  # Lose
            return (opp_move + 2) % 3
        case 1:  # Draw
            return opp_move
        case 2:  # Win
            return (opp_move + 1) % 3


def part1():
    moves = _parse_input(auto_read_input())
    return sum(score(opp_move, your_move) for opp_move, your_move in moves)


def part2():
    moves = _parse_input(auto_read_input())

    total_score = 0
    for opp_move, desired_outcome in moves:
        your_move = determine_move(opp_move, desired_outcome)
        total_score += score(opp_move, your_move)

    return total_score


if __name__ == "__main__":
    print(part1())
    print(part2())
