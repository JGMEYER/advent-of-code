from collections import defaultdict

from common.input import auto_read_input


def _step_population(population):
    num_breeding = population[0]

    # decrement timers
    for days_left in sorted(population.keys())[:-1]:
        population[days_left] = population[days_left + 1]

    population[6] += num_breeding  # resting fish
    population[8] = num_breeding  # new fish

    return population


def _parse_input(lines):
    ## Start here

    # days_left: num_fish_with_days_left
    population = {days_left: 0 for days_left in range(9)}

    for line in lines:
        for num_str in line.split(","):
            population[int(num_str)] += 1
    return population


def part1():
    population = _parse_input(auto_read_input())
    for day in range(80):
        _step_population(population)
    return sum(population.values())


def part2():
    population = _parse_input(auto_read_input())
    for day in range(256):
        _step_population(population)
    return sum(population.values())


if __name__ == "__main__":
    print(part1())
    print(part2())
