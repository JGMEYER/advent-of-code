from day6 import _parse_input, start_of_packet_marker
from common.input import auto_read_input


def test__parse_input():
    ## Start here
    assert _parse_input(auto_read_input()) == "mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def test_start_of_packet_marker():
    start_of_packet_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    start_of_packet_marker('bvwbjplbgvbhsrlpgdmjqwftvncz') == 5
    start_of_packet_marker('nppdvjthqldpwncqszvftbrmjlhg') == 6
    start_of_packet_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg') == 10
    start_of_packet_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11
    start_of_packet_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14) == 19
    start_of_packet_marker('bvwbjplbgvbhsrlpgdmjqwftvncz', 14) == 23
    start_of_packet_marker('nppdvjthqldpwncqszvftbrmjlhg', 14) == 23
    start_of_packet_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 14) == 29
    start_of_packet_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', 14) == 26
