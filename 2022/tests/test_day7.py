from day7 import _parse_input
from common.input import auto_read_input


def test__parse_input():
    ## Start here
    fs = _parse_input(auto_read_input())
    assert fs.fs == {
        '/': {'a': {'e': {'i': 584}, 'f': 29116, 'g': 2557, 'h.lst': 62596}, 'b.txt': 14848514, 'c.dat': 8504156,
              'd': {'j': 4060174, 'd.log': 8033020, 'd.ext': 5626152, 'k': 7214296}}}


def test_Filesystem_dir_sizes():
    fs = _parse_input(auto_read_input())
    dir_data = {}
    fs.dir_sizes(dir_data)
    assert dir_data == {'/a/e': 584, '/a': 94853, '/d': 24933642, '/': 48381165}