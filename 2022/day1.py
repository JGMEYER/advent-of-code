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


def top3_most_calories_total(snack_packs):
    sorted_calories = sorted([sum(pack) for pack in snack_packs], reverse=True)
    return sum(sorted_calories[:3])


def part1():
    snack_packs = _parse_input(auto_read_input())
    return most_calories(snack_packs)


def part2():
    snack_packs = _parse_input(auto_read_input())
    return top3_most_calories_total(snack_packs)


if __name__ == "__main__":
    print(part1())
    print(part2())
