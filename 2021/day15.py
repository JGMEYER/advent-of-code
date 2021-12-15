import math
from queue import PriorityQueue

from common.input import auto_read_input


def _parse_input(lines):
    ## Start here
    grid = []
    for line in lines:
        grid.append([int(s) for s in line])
    return grid


def _neighbors(grid, r, c):
    neighbors = []
    # top
    if r > 0:
        neighbors.append((grid[r - 1][c], (r - 1, c)))
    # right
    if c < len(grid[0]) - 1:
        neighbors.append((grid[r][c + 1], (r, c + 1)))
    # bottom
    if r < len(grid) - 1:
        neighbors.append((grid[r + 1][c], (r + 1, c)))
    # left
    if c > 0:
        neighbors.append((grid[r][c - 1], (r, c - 1)))
    return neighbors


# Optimization for pt2
def lowest_threat_level_bfs(grid):
    target_r, target_c = len(grid) - 1, len(grid[0]) - 1

    visited = set()
    q = PriorityQueue()
    q.put((0, (0, 0)))

    while not q.empty():
        threat_level, (r, c) = q.get()
        if (r, c) in visited:
            continue

        neighbors = _neighbors(grid, r, c)
        for n_threat_level, (n_r, n_c) in neighbors:
            if n_r == target_r and n_c == target_c:
                return threat_level + n_threat_level
            if (n_r, n_c) in visited:
                continue
            q.put((threat_level + n_threat_level, (n_r, n_c)))

        visited.add((r, c))

    # How'd we end up here?
    return None


def lowest_threat_level(grid):
    len_r, len_c = len(grid), len(grid[0])
    memo = [[math.inf] * len_c for r in range(len_r)]

    for r in range(len_r):
        for c in range(len_c):
            cur_threat = grid[r][c]
            prev_threats = []
            if r > 0:
                prev_threats.append(memo[r - 1][c])
            if c > 0:
                prev_threats.append(memo[r][c - 1])
            lowest_prev_threat = min(prev_threats) if prev_threats else 0
            memo[r][c] = cur_threat + lowest_prev_threat

    # Don't count first value in calcs
    return memo[len_r - 1][len_c - 1] - grid[0][0]


def expand_5x(orig_grid):
    orig_len_r, orig_len_c = len(orig_grid), len(orig_grid[0])
    len_r, len_c = orig_len_r * 5, orig_len_c * 5
    expanded_grid = [[-1] * len_c for r in range(len_r)]

    for r in range(orig_len_r):
        for c in range(orig_len_c):
            expanded_grid[r][c] = orig_grid[r][c]

    for r in range(len_r):
        for c in range(len_c):
            if r < orig_len_r and c < orig_len_c:
                # Already populated
                continue
            elif r < orig_len_r:
                # Look left
                prior_c = (
                    c
                    if c // orig_len_c == 0
                    else orig_len_c * (c // orig_len_c - 1) + c % orig_len_c
                )
                expanded_grid[r][c] = (expanded_grid[r][prior_c]) % 9 + 1
            else:
                # Look up
                prior_r = (
                    r
                    if r // orig_len_r == 0
                    else orig_len_r * (r // orig_len_r - 1) + r % orig_len_r
                )
                expanded_grid[r][c] = (expanded_grid[prior_r][c]) % 9 + 1

    return expanded_grid


def part1():
    grid = _parse_input(auto_read_input())
    return lowest_threat_level(grid)


def part2():
    grid = _parse_input(auto_read_input())
    grid = expand_5x(grid)
    return lowest_threat_level_bfs(grid)


if __name__ == "__main__":
    print(part1())
    print(part2())
