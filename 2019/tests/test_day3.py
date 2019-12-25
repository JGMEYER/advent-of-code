from day3 import intersections, Point


def test_insersections():
    wire1 = ["R8", "U5", "L5", "D3"]
    wire2 = ["U7", "R6", "D4", "L4"]
    inters = intersections(wire1,  wire2)
    assert len(inters) == 2
    assert Point(3, 3) in inters
    assert Point(6, 5) in inters
