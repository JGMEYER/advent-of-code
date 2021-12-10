import re

from common.input import read_file, input_filepath


class LineSegment:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    @property
    def is_horizontal(self):
        return self.y1 == self.y2

    @property
    def is_vertical(self):
        return self.x1 == self.x2

    @property
    def is_diagonal(self):
        return not (self.is_horizontal or self.is_vertical)

    def points(self):
        if self.is_horizontal:
            min_x, max_x = sorted([self.x1, self.x2])
            for x in range(min_x, max_x + 1):
                yield (x, self.y1)
        elif self.is_vertical:
            min_y, max_y = sorted([self.y1, self.y2])
            for y in range(min_y, max_y + 1):
                yield (self.x1, y)
        else:
            ((start_x, start_y), (end_x, end_y)) = sorted(
                [(self.x1, self.y1), (self.x2, self.y2)], key=lambda p: p[0]
            )
            for step, x in enumerate(range(start_x, end_x + 1)):
                if end_y > start_y:  # positive slope
                    yield (x, start_y + step)
                else:  # negative slope
                    yield (x, start_y - step)

    def __repr__(self):
        return f"{self.x1}, {self.y1}, {self.x2}, {self.y2}"


def _parse_input(test=False):
    input = read_file(input_filepath(day=5, test=test))
    pattern = r"(\d+)\,(\d+)\s\-\>\s(\d+)\,(\d+)"

    segments = []
    for iline in input:
        coords = [int(c) for c in re.match(pattern, iline).groups()]
        segments.append(LineSegment(*coords))
    return segments


def _num_overlapping_points(segments, ignore_diagonal=False):
    visited = set()
    overlaps = set()

    for seg in segments:
        if ignore_diagonal and seg.is_diagonal:
            continue

        for point in seg.points():
            if point in visited:
                overlaps.add(point)
            visited.add(point)

    return len(overlaps)


def part1():
    segments = _parse_input()
    return _num_overlapping_points(segments, ignore_diagonal=True)


def part2():
    segments = _parse_input()
    return _num_overlapping_points(segments)


if __name__ == "__main__":
    print(part1())
    print(part2())
