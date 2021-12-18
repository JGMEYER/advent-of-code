from day18 import SnailNumParser, _parse_input, SnailNum


def test__parse_input():
    ## Start here
    snail_nums = _parse_input(["[1,2]"])
    expected_num = SnailNum.from_list([None, 1, 2])
    assert snail_nums[0] == expected_num

    snail_nums = _parse_input(["[[1,2],3]"])
    expected_num = SnailNum.from_list([None, "@", 3, 1, 2])
    assert snail_nums[0] == expected_num


def test_SnailNum_magnitude():
    snail_nums = _parse_input(
        [
            "[1,2]",
            "[[1,2],3]",
            "[[1,2],[[3,4],5]]",
            "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]",
        ]
    )
    assert snail_nums[0].magnitude() == 7
    assert snail_nums[1].magnitude() == 27
    assert snail_nums[2].magnitude() == 143
    assert snail_nums[3].magnitude() == 3488


def test_SnailNum__merge():
    left = SnailNumParser.parse("[1,2]")
    right = SnailNumParser.parse("[[3,4],5]")
    expected_result = SnailNumParser.parse("[[1,2],[[3,4],5]]")
    assert SnailNum._merge(left, right) == SnailNumParser.parse(
        "[[1,2],[[3,4],5]]"
    )

    left = SnailNumParser.parse("[[[[4,3],4],4],[7,[[8,4],9]]]")
    right = SnailNumParser.parse("[1,1]")
    expected_result = SnailNumParser.parse(
        "[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]"
    )
    assert SnailNum._merge(left, right) == expected_result
