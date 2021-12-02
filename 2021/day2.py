from common.input import read_input


class Submarine:
    def __init__(self):
        self.horiz_pos = 0
        self.depth = 0

    def forward(self, n):
        self.horiz_pos += n

    def up(self, n):
        self.depth -= n

    def down(self, n):
        self.depth += n

    @property
    def mult(self):
        return self.horiz_pos * self.depth

    def __str__(self):
        return f"horiz_pos: {self.horiz_pos}, depth: {self.depth}, mult: {self.horiz_pos * self.depth}"

    def process_cmd_strs(self, input):
        for line in input:
            cmd_str, n_str = line.split(" ")
            cmd = getattr(self, cmd_str)
            cmd(int(n_str))


class AimSubmarine(Submarine):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def forward(self, n):
        self.horiz_pos += n
        self.depth += self.aim * n

    def up(self, n):
        self.aim -= n

    def down(self, n):
        self.aim += n


def part1():
    cmd_strs = read_input(day=2)
    submarine = Submarine()
    submarine.process_cmd_strs(cmd_strs)
    return submarine.mult


def part2():
    cmd_strs = read_input(day=2)
    submarine = AimSubmarine()
    submarine.process_cmd_strs(cmd_strs)
    return submarine.mult


if __name__ == "__main__":
    print(part1())
    print(part2())
