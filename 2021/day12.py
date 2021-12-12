from collections import defaultdict
from typing import Dict, Set

from common.input import auto_read_input


class Graph:
    def __init__(self):
        self.edges: Dict[str : Set[str]] = defaultdict(set)

    def add_undirected_edge(self, node_a: str, node_b: str):
        self.edges[node_a].add(node_b)
        self.edges[node_b].add(node_a)

    def _is_start_end(self, node: str):
        return node in ["start", "end"]

    def _is_small_cave(self, node: str):
        return node.lower() == node and not self._is_start_end(node)

    def paths_visiting_all_small_caves_at_most_once(self):
        paths_queue = [["start"]]
        valid_paths = set()

        while paths_queue:
            path = paths_queue.pop(0)
            last_node = path[-1]

            for next_node in self.edges[last_node]:
                if next_node == "end":
                    valid_paths.add(",".join(path) + ",end")
                    continue

                if not self._is_start_end(next_node) and (
                    # large cave
                    not self._is_small_cave(next_node)
                    or (
                        # OR small cave not yet visited
                        self._is_small_cave(next_node)
                        and next_node not in path
                    )
                ):
                    paths_queue.append(path + [next_node])

        return valid_paths

    def paths_visiting_all_small_caves_at_most_once_one_small_cave_at_most_twice(
        self,
    ):
        paths_queue = [(["start"], None)]  # node, special_cave_node
        valid_paths = set()

        while paths_queue:
            path, special_cave_old = paths_queue.pop(0)
            last_node = path[-1]

            for next_node in self.edges[last_node]:
                if next_node == "start":
                    continue

                if next_node == "end":
                    valid_paths.add(",".join(path) + ",end")
                    continue

                special_cave = special_cave_old

                if self._is_small_cave(next_node):
                    if next_node in path:
                        if not special_cave:
                            special_cave = next_node
                        else:
                            continue

                paths_queue.append((path + [next_node], special_cave))

        return valid_paths


def _parse_input(lines):
    ## Start here
    graph = Graph()
    for line in lines:
        a, b = line.split("-")
        graph.add_undirected_edge(a, b)
    return graph


def part1():
    graph = _parse_input(auto_read_input())
    return len(graph.paths_visiting_all_small_caves_at_most_once())


def part2():
    graph = _parse_input(auto_read_input())
    return len(
        graph.paths_visiting_all_small_caves_at_most_once_one_small_cave_at_most_twice()
    )


if __name__ == "__main__":
    print(part1())
    print(part2())
