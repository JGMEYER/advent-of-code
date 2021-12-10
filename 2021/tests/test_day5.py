from day5 import _num_overlapping_points, _parse_input, LineSegment


def test_LineSegment_points_horizontal():
    seg = LineSegment(9, 7, 7, 7)
    assert list(seg.points()) == [(7, 7), (8, 7), (9, 7)]


def test_LineSegment_points_vertical():
    seg = LineSegment(1, 1, 1, 3)
    assert list(seg.points()) == [(1, 1), (1, 2), (1, 3)]


def test_LineSegment_points_diagonal():
    assert list(LineSegment(1, 1, 3, 3).points()) == [(1, 1), (2, 2), (3, 3)]
    assert list(LineSegment(9, 7, 7, 9).points()) == [(7, 9), (8, 8), (9, 7)]


def test_num_overlapping_points():
    segments = _parse_input(test=True)
    assert _num_overlapping_points(segments, ignore_diagonal=True) == 5

    segments = _parse_input(test=True)
    assert _num_overlapping_points(segments) == 12
