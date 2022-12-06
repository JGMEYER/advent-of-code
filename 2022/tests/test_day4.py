from day4 import _parse_input, RangePair, one_range_fully_contains_other, ranges_overlap_at_all
from common.input import auto_read_input


def test__parse_input():
    ## Start here
    ranges = _parse_input(auto_read_input())
    assert ranges == [
        RangePair(2, 4, 6, 8),
        RangePair(2, 3, 4, 5),
        RangePair(5, 7, 7, 9),
        RangePair(2, 8, 3, 7),
        RangePair(6, 6, 4, 6),
        RangePair(2, 6, 4, 8),
    ]


def test_one_range_fully_contains_other():
    assert one_range_fully_contains_other(*RangePair(2, 4, 6, 8)) == False
    assert one_range_fully_contains_other(*RangePair(2, 3, 4, 5)) == False
    assert one_range_fully_contains_other(*RangePair(5, 7, 7, 9)) == False
    assert one_range_fully_contains_other(*RangePair(2, 8, 3, 7))
    assert one_range_fully_contains_other(*RangePair(6, 6, 4, 6))
    assert one_range_fully_contains_other(*RangePair(2, 6, 4, 8)) == False


def test_ranges_overlap_at_all():
    assert ranges_overlap_at_all(*RangePair(2, 4, 6, 8)) == False
    assert ranges_overlap_at_all(*RangePair(2, 3, 4, 5)) == False
    assert ranges_overlap_at_all(*RangePair(5, 7, 7, 9))
    assert ranges_overlap_at_all(*RangePair(2, 8, 3, 7))
    assert ranges_overlap_at_all(*RangePair(6, 6, 4, 6))
    assert ranges_overlap_at_all(*RangePair(2, 6, 4, 8))
