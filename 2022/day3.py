from common.input import auto_read_input


def _halve_str(s: str) -> tuple:
    return s[:len(s)//2], s[len(s)//2:]


def get_priority(c: chr) -> int:
    ascii = ord(c)

    if 97 <= ascii <= 122:  # lowercase
        return ascii - 97 + 1  # (1 -> 26)
    elif 65 <= ascii <= 90:  # uppercase
        return ascii - 65 + 27  # (27 -> 52)
    else:
        return -1  # should not occur


def _parse_input(lines):
    ## Start here
    return lines


def part1():
    lines = _parse_input(auto_read_input())
    rucksacks: list(list(str)) = [_halve_str(line) for line in lines]

    sum_priorities = 0

    for compart1, compart2 in rucksacks:
        shared_item = list(set(compart1) & set(compart2))[0]  # Guaranteed only 1 shared
        sum_priorities += get_priority(shared_item)

    return sum_priorities


def part2():
    lines = _parse_input(auto_read_input())
    groups: list(list(str)) = [lines[i:i+3] for i in range(0, len(lines), 3)]

    sum_priorities = 0

    for group in groups:
        rucksack_a, rucksack_b, rucksack_c = group
        shared_item = list(set(rucksack_a) & set(rucksack_b) & set(rucksack_c))[0]  # Guaranteed only 1 shared
        sum_priorities += get_priority(shared_item)

    return sum_priorities

if __name__ == "__main__":
    print(part1())
    print(part2())
