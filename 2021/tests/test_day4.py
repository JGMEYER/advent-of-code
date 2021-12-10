from day4 import _superstrip, part1, part2


def test__superstrip():
    str = "  \t  foo   \t   bar \t  "
    actual = _superstrip(str)
    expected = "foo bar"
    assert actual == expected


def test_part1():
    assert part1("tests/test_inputs/test_day4.txt") == 4512


def test_part2():
    assert part2("tests/test_inputs/test_day4.txt") == 1924
