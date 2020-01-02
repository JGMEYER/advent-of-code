from common.input import read_input

from z3 import sat, And, BitVecs, BV2Int, Or, Solver


def valid_passwords(pw_min=0, pw_max=999999):
    """
    This could easily be solved without a SAT solver, but this was a great
    excuse to learn how to use z3.
    """
    s = Solver()

    # pw is 6 digit number
    m = BitVecs("pw[0] pw[1] pw[2] pw[3] pw[4] pw[5]", 8)

    # each digit must be between 0 and 9
    for i in range(6):
        s.add(m[i] >= 0)
        s.add(m[i] <= 9)

    # value is within range of puzzle input
    s.add((BV2Int(m[0]) * 100000
           + BV2Int(m[1]) * 10000
           + BV2Int(m[2]) * 1000
           + BV2Int(m[3]) * 100
           + BV2Int(m[4]) * 10
           + BV2Int(m[5]) * 1) >= pw_min)
    s.add((BV2Int(m[0]) * 100000
           + BV2Int(m[1]) * 10000
           + BV2Int(m[2]) * 1000
           + BV2Int(m[3]) * 100
           + BV2Int(m[4]) * 10
           + BV2Int(m[5]) * 1) <= pw_max)

    # digits never decrease from left to right
    increase_clause = And([m[i-1] <= m[i] for i in range(1, 6)])
    s.add(increase_clause)

    # must have at least one double
    doubles_clause = Or([m[i-1] == m[i] for i in range(1, 6)])
    s.add(doubles_clause)

    valid = []

    while s.check() == sat:
        model = s.model()

        ans = 0
        nope = []

        for idx, i in enumerate(m):
            ans += model[i].as_long() * 10**(5-idx)
            nope.append(i != model[i])

        # prevent this solution in the future
        s.add(Or(nope))

        valid.append(ans)

    return valid


def part1() -> int:
    range_str = read_input(day=4)[0]
    pw_min, pw_max = range_str.split('-')

    valid = valid_passwords(pw_min, pw_max)
    print(valid)  # debug
    print(sorted(valid))
    return len(valid)


def part2() -> int:
    pass


if __name__ == "__main__":
    print(part1())
    print(part2())
