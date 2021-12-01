from day1 import _num_depth_increases, _num_depth_increases_sliding_window


def test__num_depth_increases():
    depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert _num_depth_increases(depths) == 7


def test__num_depth_increases_sliding_window():
    depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert _num_depth_increases_sliding_window(depths) == 5
