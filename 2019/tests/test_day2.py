from pytest import raises

from day2 import IntcodeParser


def test_intcode_parser_iter():
    parser = IntcodeParser("1,9,10,3,2,3,11,0,99,30,40,50")
    assert next(parser) == [1, 9, 10, 3]
    assert next(parser) == [2, 3, 11, 0]
    with raises(StopIteration):
        next(parser)


def _process(input, expected) -> bool:
    parser = IntcodeParser(input)
    for instruction in parser:
        parser.process(instruction)
    return parser.ops == expected


def test_intcode_parser_process():
    assert _process(
        "1,0,0,0,99",
        [2, 0, 0, 0, 99],
    )
    assert _process(
        "2,3,0,3,99",
        [2, 3, 0, 6, 99],
    )
    assert _process(
        "2,4,4,5,99,0",
        [2, 4, 4, 5, 99, 9801],
    )
    assert _process(
        "1,1,1,4,99,5,6,0,99",
        [30, 1, 1, 4, 2, 5, 6, 0, 99],
    )
    assert _process(
        "1,9,10,3,2,3,11,0,99,30,40,50",
        [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
    )
