from day20 import _parse_input, Image
from common.input import auto_read_input


def test__parse_input():
    ## Start here
    algorithm, img = _parse_input(auto_read_input())
    expected_algorithm = 0b00101001111101010101110110000011101101001110111100111110010000100100110011100111111011100011110010011111001100101111100011010100101100101000000101110111111011101111000101101100100100111110000010100001110010110000001000001001001001100100011011111101111011110101000100000001001010100011110110100000010010001101011001000110101100111010000001010000000101010111101110110001000001111010010010110100001100101111000011000110010001000000101000000010000000110011110010001010100011001010011100111110000000010011110000001001
    expected_img = {
        (0, 0),
        (0, 3),
        (1, 0),
        (2, 0),
        (2, 1),
        (2, 4),
        (3, 2),
        (4, 2),
        (4, 3),
        (4, 4),
    }
    expected_img = {
        (0, 0): True,
        (0, 1): False,
        (0, 2): False,
        (0, 3): True,
        (0, 4): False,
        (1, 0): True,
        (1, 1): False,
        (1, 2): False,
        (1, 3): False,
        (1, 4): False,
        (2, 0): True,
        (2, 1): True,
        (2, 2): False,
        (2, 3): False,
        (2, 4): True,
        (3, 0): False,
        (3, 1): False,
        (3, 2): True,
        (3, 3): False,
        (3, 4): False,
        (4, 0): False,
        (4, 1): False,
        (4, 2): True,
        (4, 3): True,
        (4, 4): True,
    }
    assert algorithm == expected_algorithm
    assert img == expected_img


def test__pixel_on_after_enhance():
    algorithm, img = _parse_input(auto_read_input())

    # value_idx = 34
    assert img._pixel_on_after_enhance(algorithm, 2, 2, 0) == True

    # value_idx: 18
    assert img._pixel_on_after_enhance(algorithm, 0, 0, 0) == False

    # value_idx: 134
    assert img._pixel_on_after_enhance(algorithm, 4, 3, 0) == False

    # value_idx: 312
    assert img._pixel_on_after_enhance(algorithm, 4, 3, 0) == False


def test_enhance():
    algorithm, img = _parse_input(auto_read_input())

    img = img.get_enhanced(algorithm, 0)
    assert img.num_on() == 24

    img = img.get_enhanced(algorithm, 1)
    assert img.num_on() == 35

    # Slow
    for gen in range(2, 50):  # rest up to 50 gens
        img = img.get_enhanced(algorithm, gen)
    assert img.num_on() == 3351
