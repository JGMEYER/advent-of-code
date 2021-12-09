from common.input import read_test_input
from day3 import _to_gamma_epsilon, _get_life_support_ratings


def test__to_gamma_epsilon():
    binary_strs = read_test_input(day=3)
    gamma, epsilon = _to_gamma_epsilon(binary_strs)
    assert gamma == 22
    assert epsilon == 9


def test__get_life_support_ratings():
    binary_strs = read_test_input(day=3)
    oxygen_generator_rating, co2_scrubber_rating = _get_life_support_ratings(
        binary_strs
    )
    assert oxygen_generator_rating == 23
    assert co2_scrubber_rating == 10
