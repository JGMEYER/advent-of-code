from common.input import auto_read_input


def start_of_packet_marker(datastream, num_uniq_req=4):
    for idx in range(0, len(datastream)):
        if len(set(datastream[idx:idx+num_uniq_req])) == num_uniq_req:
            return idx
    return -1


def _parse_input(lines):
    ## Start here
    datastream = lines[0]
    return datastream


def part1():
    datastream = _parse_input(auto_read_input())
    return start_of_packet_marker(datastream) + 4


def part2():
    datastream = _parse_input(auto_read_input())
    return start_of_packet_marker(datastream, 14) + 14


if __name__ == "__main__":
    print(part1())
    print(part2())
