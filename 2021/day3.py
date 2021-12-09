from common.input import read_input


def _to_gamma_epsilon(binary_strs):
    bin_length = len(binary_strs[0])
    gamma_bin, epsilon_bin = 0b0, 0b0

    for chr_idx in range(bin_length):
        num_ones = sum(
            [
                1 if (int(binary_str[chr_idx]) == 1) else 0
                for binary_str in binary_strs
            ]
        )

        most_common = 1 if num_ones >= len(binary_strs) / 2 else 0
        least_common = 0 if most_common == 1 else 1

        gamma_bin = (gamma_bin << 1) ^ most_common
        epsilon_bin = (epsilon_bin << 1) ^ least_common

    return int(gamma_bin), int(epsilon_bin)


def _split_most_least_common(binary_strs, idx):
    ones = []
    zeroes = []

    for str in binary_strs:
        if str[idx] == "1":
            ones.append(str)
        if str[idx] == "0":
            zeroes.append(str)

    if len(ones) >= len(zeroes):
        most, least = ones, zeroes
    else:
        most, least = zeroes, ones

    return most, least


def _get_life_support_ratings(binary_strs):
    most, least = _split_most_least_common(binary_strs, 0)

    idx = 1
    while idx < len(binary_strs) and len(most) > 1:
        most, _ = _split_most_least_common(most, idx)
        idx += 1

    idx = 1
    while idx < len(binary_strs) and len(least) > 1:
        _, least = _split_most_least_common(least, idx)
        idx += 1

    oxygen_generator_rating = int(most[0], 2)
    co2_scrubber_rating = int(least[0], 2)

    return oxygen_generator_rating, co2_scrubber_rating


def part1():
    binary_strs = read_input(day=3)
    gamma, epsilon = _to_gamma_epsilon(binary_strs)
    return gamma * epsilon


def part2():
    binary_strs = read_input(day=3)
    oxygen_generator_rating, co2_scrubber_rating = _get_life_support_ratings(
        binary_strs
    )
    return oxygen_generator_rating * co2_scrubber_rating


if __name__ == "__main__":
    print(part1())
    print(part2())
