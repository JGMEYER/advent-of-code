from common.input import read_input


class SyntaxChecker:
    CLOSE_OPEN = {
        ")": "(",
        "]": "[",
        "}": "{",
        ">": "<",
    }
    CORRUPTED_SCORES = {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }
    AUTOCOMPLETE_SCORES = {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4,
    }

    @classmethod
    def score(cls, line):
        stack = []

        for c in line:
            c_is_open = c in ["(", "[", "{", "<"]
            if c_is_open:
                stack.append(c)
            else:
                c_correctly_closes = stack and stack[-1] == cls.CLOSE_OPEN[c]
                if c_correctly_closes:
                    stack.pop()
                else:
                    corrupted_score = cls.CORRUPTED_SCORES[c]
                    return corrupted_score, 0

        incomplete_score = 0
        while stack:
            c = stack.pop()
            incomplete_score *= 5
            incomplete_score += cls.AUTOCOMPLETE_SCORES[c]

        return 0, incomplete_score


def part1():
    input = read_input(day=10)
    score = 0
    for line in input:
        corrupted_score, _ = SyntaxChecker.score(line)
        score += corrupted_score
    return score


def part2():
    input = read_input(day=10)
    incomplete_scores = []
    for line in input:
        _, incomplete_score = SyntaxChecker.score(line)
        if incomplete_score:
            incomplete_scores.append(incomplete_score)
    # take middle
    return sorted(incomplete_scores)[len(incomplete_scores) // 2]


if __name__ == "__main__":
    print(part1())
    print(part2())
