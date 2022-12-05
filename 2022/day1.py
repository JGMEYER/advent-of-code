from common.input import auto_read_input


def _parse_input(lines):
    ## Start here
    snack_packs = [[]]
    for line in lines:
        if line:
            calories = int(line)
            snack_packs[-1].append(calories)
        else:
            snack_packs.append([])
    return snack_packs


def most_calories(snack_packs):
    return max([sum(pack) for pack in snack_packs])


def part1():
    snack_packs = _parse_input(auto_read_input())
    return most_calories(snack_packs)


def part2():
    _ = _parse_input(auto_read_input())
    return None


if __name__ == "__main__":
    print(part1())
    print(part2())
