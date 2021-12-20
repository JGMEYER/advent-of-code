from common.input import auto_read_input


class Image(dict):
    def __str__(self):
        # Expensive, but for debugging
        min_r = min(self, key=lambda p: p[0])[0]
        max_r = max(self, key=lambda p: p[0])[0]
        min_c = min(self, key=lambda p: p[1])[1]
        max_c = max(self, key=lambda p: p[1])[1]

        x_shift = -min_r
        y_shift = -min_c

        h = max_r - min_r + 1
        w = max_c - min_c + 1

        arr = [[None] * w for _ in range(h)]
        for (r_raw, c_raw), is_on in self.items():
            r = r_raw + x_shift
            c = c_raw + y_shift
            arr[r][c] = "#" if is_on else "."

        return "\n".join(["".join(row) for row in arr])

    def _pixel_on_after_enhance(self, algorithm, r, c, void_value):
        value_idx = 0

        for direction in range(9):
            n_row = r + ((direction // 3) - 1)
            n_col = c + ((direction % 3) - 1)

            n = self.get((n_row, n_col))
            if n is not None:
                value_idx ^= int(n) << 9 - direction - 1
            else:
                value_idx ^= void_value << 9 - direction - 1

        return bool(algorithm & (1 << (512 - value_idx - 1)))

    def num_on(self):
        return len([v for v in self.values() if v])

    def get_enhanced(self, algorithm, gen):
        """gen=0 means first ITERATION after original"""

        void_value = 0
        first_algo_val = int(bool(algorithm & (1 << 511)))

        if first_algo_val == 1:
            # Odd generations will have "1" voids
            void_value = gen % 2

        enhanced = Image()
        visited = set()

        # Scan x+-1 and y+-1 to account for this pixel impacting neighbors'
        # calculations.
        for pixel in self.keys():
            r, c = pixel

            for direction in range(9):
                n_row = r + ((direction % 3) - 1)
                n_col = c + ((direction // 3) - 1)

                if (n_row, n_col) in visited:
                    continue

                enhanced[(n_row, n_col)] = self._pixel_on_after_enhance(
                    algorithm, n_row, n_col, void_value=void_value
                )

                visited.add((n_row, n_col))

        return enhanced


def _parse_input(lines):
    ## Start here
    algorithm_str = lines[0].replace(".", "0").replace("#", "1")
    algorithm = int(algorithm_str, 2)

    img = Image()
    for r, img_line in enumerate(lines[2:]):
        for c, chr in enumerate(img_line):
            img[(r, c)] = chr == "#"

    return algorithm, img


def part1():
    algorithm, img = _parse_input(auto_read_input())
    for gen in range(2):
        img = img.get_enhanced(algorithm, gen)
    return img.num_on()


def part2():
    algorithm, img = _parse_input(auto_read_input())
    for gen in range(50):
        print(f"gen: {gen}")
        img = img.get_enhanced(algorithm, gen)
    print(img)
    return img.num_on()


if __name__ == "__main__":
    print(part1())
    print(part2())
