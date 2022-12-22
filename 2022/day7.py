import math
import re

from common.input import auto_read_input


class Filesystem(object):
    def __init__(self):
        self.fs = {"/": {}}
        self.pwd = []
        self.pushd_stack = []

    def cd(self, dirname, mkdir_if_not_exists=False):
        match dirname:
            case "..":
                self.pwd.pop()
            case "/":
                self.pwd = ["/"]
            case default:
                if mkdir_if_not_exists and not self.file_at(self.pwd + [dirname]):
                    self.mkdir(dirname)
                self.pwd.append(dirname)

    def ls(self, path=None):
        return self.file_at(path) if path else self.file_at(self.pwd)

    def mkdir(self, name):
        self.file_at(self.pwd)[name] = {}

    def touch(self, name, size=0):
        self.file_at(self.pwd)[name] = size

    def pushd(self):
        self.pushd_stack.append(self.fs)

    def popd(self):
        self.fs = self.pushd_stack.pop()

    def file_at(self, path):
        d = self.fs
        for k in path:
            d = d.get(k)
        return d

    @staticmethod
    def path_to_str(path):
        return "/" + "/".join(path[1:])

    @staticmethod
    def is_dir(file):
        return type(file) is dict

    def dir_sizes(self, data, dir_path=["/"]):
        f = self.file_at(dir_path)
        if self.is_dir(f):
            dir_size = 0
            for sub_f in f:
                dir_size += self.dir_sizes(data, dir_path + [sub_f])
            data[self.path_to_str(dir_path)] = dir_size
            return dir_size
        else:
            return f


def _parse_input(lines):
    fs = Filesystem()
    crx = 0

    while crx < len(lines):
        m = re.match(r"\$ (\w+)(?:\s(.+))?", lines[crx])
        arg1, arg2 = m.groups()

        if arg1 == "cd":
            fs.cd(arg2, True)
            crx += 1
            continue
        elif arg1 == "ls":
            crx += 1
            while crx < len(lines) and not lines[crx].startswith("$"):
                m = re.match(r"(dir|\d+)\s([\w\.]+)", lines[crx])
                desc, name = m.groups()
                if desc == 'dir':
                    fs.mkdir(name)
                else:
                    fs.touch(name, size=int(desc))
                crx += 1
            continue
        else:
            raise ValueError("Unknown cmd")

    return fs


def part1():
    fs = _parse_input(auto_read_input())
    dir_data = {}
    fs.dir_sizes(dir_data)

    sum_of_dirs_less_than_100000 = 0

    for d_name, size in dir_data.items():
        if size <= 100000:
            sum_of_dirs_less_than_100000 += size

    return sum_of_dirs_less_than_100000


def part2():
    fs = _parse_input(auto_read_input())
    dir_data = {}
    fs.dir_sizes(dir_data)

    avail_space = 70000000 - dir_data['/']
    needed_space = 30000000

    min_dir_delete_size = math.inf
    for d_name, size in dir_data.items():
        if avail_space + size >= needed_space:
            min_dir_delete_size = min(min_dir_delete_size, size)

    return min_dir_delete_size


if __name__ == "__main__":
    print(part1())
    print(part2())
