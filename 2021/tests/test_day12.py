from day12 import _parse_input
from common.input import auto_read_input


def test__parse_input():
    ## Start here

    #     start
    #     /   \
    # c--A-----b--d
    #     \   /
    #      end
    graph = _parse_input(auto_read_input(suffix=1))
    expected_edges = {
        "start": {"A", "b"},
        "A": {"start", "c", "b", "end"},
        "b": {"start", "A", "d", "end"},
        "c": {"A"},
        "d": {"b"},
        "end": {"A", "b"},
    }
    assert graph.edges == expected_edges


def test_Graph_paths_visiting_all_small_caves_at_most_once_1():
    graph = _parse_input(auto_read_input(suffix=1))
    paths = graph.paths_visiting_all_small_caves_at_most_once()
    expected_paths = {
        "start,A,b,A,c,A,end",
        "start,A,b,A,end",
        "start,A,b,end",
        "start,A,c,A,b,A,end",
        "start,A,c,A,b,end",
        "start,A,c,A,end",
        "start,A,end",
        "start,b,A,c,A,end",
        "start,b,A,end",
        "start,b,end",
    }
    assert paths == expected_paths


def test_Graph_paths_visiting_all_small_caves_at_most_once_2():
    graph = _parse_input(auto_read_input(suffix=2))
    paths = graph.paths_visiting_all_small_caves_at_most_once()
    expected_paths = {
        "start,HN,dc,HN,end",
        "start,HN,dc,HN,kj,HN,end",
        "start,HN,dc,end",
        "start,HN,dc,kj,HN,end",
        "start,HN,end",
        "start,HN,kj,HN,dc,HN,end",
        "start,HN,kj,HN,dc,end",
        "start,HN,kj,HN,end",
        "start,HN,kj,dc,HN,end",
        "start,HN,kj,dc,end",
        "start,dc,HN,end",
        "start,dc,HN,kj,HN,end",
        "start,dc,end",
        "start,dc,kj,HN,end",
        "start,kj,HN,dc,HN,end",
        "start,kj,HN,dc,end",
        "start,kj,HN,end",
        "start,kj,dc,HN,end",
        "start,kj,dc,end",
    }
    assert paths == expected_paths


def test_Graph_paths_visiting_all_small_caves_at_most_once_3():
    graph = _parse_input(auto_read_input(suffix=3))
    paths = graph.paths_visiting_all_small_caves_at_most_once()
    assert len(paths) == 226


def test_Graph_paths_visiting_all_small_caves_at_most_once_one_small_cave_at_most_twice_1():
    graph = _parse_input(auto_read_input(suffix=1))
    paths = (
        graph.paths_visiting_all_small_caves_at_most_once_one_small_cave_at_most_twice()
    )
    expected_paths = {
        "start,A,b,A,b,A,c,A,end",
        "start,A,b,A,b,A,end",
        "start,A,b,A,b,end",
        "start,A,b,A,c,A,b,A,end",
        "start,A,b,A,c,A,b,end",
        "start,A,b,A,c,A,c,A,end",
        "start,A,b,A,c,A,end",
        "start,A,b,A,end",
        "start,A,b,d,b,A,c,A,end",
        "start,A,b,d,b,A,end",
        "start,A,b,d,b,end",
        "start,A,b,end",
        "start,A,c,A,b,A,b,A,end",
        "start,A,c,A,b,A,b,end",
        "start,A,c,A,b,A,c,A,end",
        "start,A,c,A,b,A,end",
        "start,A,c,A,b,d,b,A,end",
        "start,A,c,A,b,d,b,end",
        "start,A,c,A,b,end",
        "start,A,c,A,c,A,b,A,end",
        "start,A,c,A,c,A,b,end",
        "start,A,c,A,c,A,end",
        "start,A,c,A,end",
        "start,A,end",
        "start,b,A,b,A,c,A,end",
        "start,b,A,b,A,end",
        "start,b,A,b,end",
        "start,b,A,c,A,b,A,end",
        "start,b,A,c,A,b,end",
        "start,b,A,c,A,c,A,end",
        "start,b,A,c,A,end",
        "start,b,A,end",
        "start,b,d,b,A,c,A,end",
        "start,b,d,b,A,end",
        "start,b,d,b,end",
        "start,b,end",
    }
    assert paths == expected_paths


def test_Graph_paths_visiting_all_small_caves_at_most_once_one_small_cave_at_most_twice_2():
    graph = _parse_input(auto_read_input(suffix=2))
    paths = (
        graph.paths_visiting_all_small_caves_at_most_once_one_small_cave_at_most_twice()
    )
    assert len(paths) == 103


def test_Graph_paths_visiting_all_small_caves_at_most_once_one_small_cave_at_most_twice_3():
    graph = _parse_input(auto_read_input(suffix=3))
    paths = (
        graph.paths_visiting_all_small_caves_at_most_once_one_small_cave_at_most_twice()
    )
    assert len(paths) == 3509
