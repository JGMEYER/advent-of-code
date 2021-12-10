from common.input import read_test_input
from day10 import SyntaxChecker


def test_SyntaxChecker_corrupted_score():
    total_corrupted_score = 0
    for line in read_test_input(day=10):
        corrupted_score, _ = SyntaxChecker.score(line)
        total_corrupted_score += corrupted_score
    assert total_corrupted_score == 26397


def test_SyntaxChecker_incomplete_score():
    all_incomplete_scores = []
    for line in read_test_input(day=10):
        _, incomplete_score = SyntaxChecker.score(line)
        all_incomplete_scores.append(incomplete_score)
    assert all_incomplete_scores == [
        288957,
        5566,
        0,
        1480781,
        0,
        0,
        995444,
        0,
        0,
        294,
    ]
