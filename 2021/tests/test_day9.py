import math

from day9 import _parse_input, Basin, Point, HeightMap
from common.input import auto_read_input


def test__parse_input():
    ## Start here
    heightmap = _parse_input(auto_read_input())
    assert heightmap._heights == [
        [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
        [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
        [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
        [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
        [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
    ]


def test_HeightMap_neighbors():
    heightmap = HeightMap([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    assert heightmap.neighbors(0, 0) == [
        None,
        Point(0, 1, 1),
        Point(1, 0, 3),
        None,
    ]
    assert heightmap.neighbors(1, 1) == [
        Point(0, 1, 1),
        Point(1, 2, 5),
        Point(2, 1, 7),
        Point(1, 0, 3),
    ]
    assert heightmap.neighbors(2, 2) == [
        Point(1, 2, 5),
        None,
        None,
        Point(2, 1, 7),
    ]
    # Pull from cache
    assert (2, 2) in heightmap._neighbors_cache
    assert heightmap._neighbors_cache[(2, 2)] == heightmap.neighbors(2, 2)


def test_HeightMap_is_low_point():
    heightmap = HeightMap([[2, 1, 2], [0, 3, 2], [1, 0, 2]])
    assert heightmap.is_low_point(0, 1) == True
    assert heightmap.is_low_point(1, 1) == False
    assert heightmap.is_low_point(1, 0) == True
    assert heightmap.is_low_point(1, 2) == False
    assert heightmap.is_low_point(2, 0) == False
    assert heightmap.is_low_point(2, 2) == False


def test_HeightMap_get_all_low_points():
    heightmap = _parse_input(auto_read_input())
    assert heightmap.get_all_low_points() == [
        Point(0, 1, 1),
        Point(0, 9, 0),
        Point(2, 2, 5),
        Point(4, 6, 5),
    ]


def test_Basin_size():
    heightmap = _parse_input(auto_read_input())
    b1 = Basin(heightmap, Point(0, 1, 1))
    assert b1.size == 3
    b2 = Basin(heightmap, Point(0, 9, 0))
    assert b2.size == 9
    b3 = Basin(heightmap, Point(2, 2, 5))
    assert b3.size == 14
    b4 = Basin(heightmap, Point(4, 6, 5))
    assert b4.size == 9

    basins = [b1, b2, b3, b4]
    top3_basins = sorted(basins, key=lambda b: b.size)[-3:]
    assert math.prod([b.size for b in top3_basins]) == 1134
