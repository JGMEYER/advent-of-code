from common.input import auto_read_input
from day18 import (
    SnailNumParser,
    SnailNum,
    _parse_input,
    _sum_all,
    _max_mag_from_any_two,
)


def test__parse_input():
    ## Start here
    snail_nums = _parse_input(["[1,2]"])
    expected_num = SnailNum.from_list([None, 1, 2])
    assert snail_nums[0] == expected_num

    snail_nums = _parse_input(["[[1,2],3]"])
    expected_num = SnailNum.from_list([None, "@", 3, 1, 2])
    assert snail_nums[0] == expected_num


def test_SnailNumParser_unparse():
    lines = [
        "[1,2]",
        "[[1,2],3]",
        "[[1,2],[[3,4],5]]",
        "[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]",
    ]
    snail_nums = _parse_input(lines)
    assert SnailNumParser.unparse(snail_nums[0]) == lines[0]
    assert SnailNumParser.unparse(snail_nums[1]) == lines[1]
    assert SnailNumParser.unparse(snail_nums[2]) == lines[2]
    assert SnailNumParser.unparse(snail_nums[3]) == lines[3]


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


def test_SnailNum__explode():
    num = SnailNumParser.parse("[[[[[9,8],1],2],3],4]")
    expected_result = SnailNumParser.parse("[[[[0,9],2],3],4]")
    num._explode(15)
    assert num == expected_result

    num = SnailNumParser.parse("[7,[6,[5,[4,[3,2]]]]]")
    expected_result = SnailNumParser.parse("[7,[6,[5,[7,0]]]]")
    num._explode(30)
    assert num == expected_result

    num = SnailNumParser.parse("[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]")
    expected_result = SnailNumParser.parse("[[[[0,7],4],[[7,8],[6,0]]],[8,1]]")
    num._explode(22)
    assert num == expected_result


def test_SnailNum__split():
    num = SnailNumParser.parse("[[[[0,7],4],[[7,8],[0,13]]],[1,1]]")
    expected_result = SnailNumParser.parse(
        "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]"
    )
    num._split(22)
    assert num == expected_result


def test_SnailNum_add():
    a = SnailNumParser.parse("[[[[4,3],4],4],[7,[[8,4],9]]]")
    b = SnailNumParser.parse("[1,1]")

    """
    Steps are as follows:

    after addition: [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
    after explode:  [[[[0,7],4],[7,[[8,4],9]]],[1,1]]
    after explode:  [[[[0,7],4],[15,[0,13]]],[1,1]]
    after split:    [[[[0,7],4],[[7,8],[0,13]]],[1,1]]
    after split:    [[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
    after explode:  [[[[0,7],4],[[7,8],[6,0]]],[8,1]]
    """
    assert str(a.add(b)) == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"


def test_complex_example():
    lines = [
        "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]",  # 0
        "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]",  # 1
        "[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]",  # 2
        "[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]",  # 3
        "[7,[5,[[3,8],[1,4]]]]",  # 4
        "[[2,[2,2]],[8,[8,1]]]",  # 5
        "[2,9]",  # 6
        "[1,[[[9,3],9],[[9,0],[0,7]]]]",  # 7
        "[[[5,[7,4]],7],1]",  # 8
        "[[[[4,2],2],6],[8,7]]",  # 9
    ]
    snail_nums = _parse_input(lines)

    total = snail_nums[0]
    assert str(total) == "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]"

    """
    (thank you topaz on reddit for breakdown)
    Steps are as follows:

    after addition: [[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]
    after explode:  [[[[4,0],[5,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]
    after explode:  [[[[4,0],[5,4]],[[0,[7,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]
    after explode:  [[[[4,0],[5,4]],[[7,0],[15,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]
    after explode:  [[[[4,0],[5,4]],[[7,0],[15,5]]],[10,[[0,[11,3]],[[6,3],[8,8]]]]]
    after explode:  [[[[4,0],[5,4]],[[7,0],[15,5]]],[10,[[11,0],[[9,3],[8,8]]]]]
    after explode:  [[[[4,0],[5,4]],[[7,0],[15,5]]],[10,[[11,9],[0,[11,8]]]]]
    after explode:  [[[[4,0],[5,4]],[[7,0],[15,5]]],[10,[[11,9],[11,0]]]]
    after split:    [[[[4,0],[5,4]],[[7,0],[[7,8],5]]],[10,[[11,9],[11,0]]]]
    after explode:  [[[[4,0],[5,4]],[[7,7],[0,13]]],[10,[[11,9],[11,0]]]]
    after split:    [[[[4,0],[5,4]],[[7,7],[0,[6,7]]]],[10,[[11,9],[11,0]]]]
    after explode:  [[[[4,0],[5,4]],[[7,7],[6,0]]],[17,[[11,9],[11,0]]]]
    after split:    [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,9],[[11,9],[11,0]]]]
    after split:    [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,9],[[[5,6],9],[11,0]]]]
    after explode:  [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,14],[[0,15],[11,0]]]]
    after split:    [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[0,15],[11,0]]]]
    after split:    [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[0,[7,8]],[11,0]]]]
    after explode:  [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,0],[19,0]]]]
    after split:    [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,0],[[9,10],0]]]]
    after explode:  [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[0,10]]]]
    after split:    [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[0,[5,5]]]]]
    after explode:  [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
    after split:    [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
    after split:    [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]
    """
    total = total.add(snail_nums[1])
    assert (
        str(total)
        == "[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]"
    )

    # NOTE: Did not finish other intermediate steps after, but other, harder
    # tests are working


def test_simple_blind_examples():
    lines = [
        "[1,1]",
        "[2,2]",
        "[3,3]",
        "[4,4]",
    ]
    snums = _parse_input(lines)
    assert str(_sum_all(snums)) == "[[[[1,1],[2,2]],[3,3]],[4,4]]"

    lines = [
        "[1,1]",
        "[2,2]",
        "[3,3]",
        "[4,4]",
        "[5,5]",
    ]
    snums = _parse_input(lines)
    assert str(_sum_all(snums)) == "[[[[3,0],[5,3]],[4,4]],[5,5]]"

    lines = [
        "[1,1]",
        "[2,2]",
        "[3,3]",
        "[4,4]",
        "[5,5]",
        "[6,6]",
    ]
    snums = _parse_input(lines)
    assert str(_sum_all(snums)) == "[[[[5,0],[7,4]],[5,5]],[6,6]]"


def test_complex_blind_example():
    lines = [
        "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
        "[[[5,[2,8]],4],[5,[[9,9],0]]]",
        "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
        "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
        "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
        "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
        "[[[[5,4],[7,7]],8],[[8,3],8]]",
        "[[9,3],[[9,9],[6,[4,9]]]]",
        "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
        "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]",
    ]
    snums = _parse_input(lines)
    result = _sum_all(snums)
    assert result.magnitude() == 4140


def test__max_mag_from_any_two():
    lines = [
        "[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]",
        "[[[5,[2,8]],4],[5,[[9,9],0]]]",
        "[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]",
        "[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]",
        "[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]",
        "[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]",
        "[[[[5,4],[7,7]],8],[[8,3],8]]",
        "[[9,3],[[9,9],[6,[4,9]]]]",
        "[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]",
        "[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]",
    ]
    snums = _parse_input(lines)
    assert _max_mag_from_any_two(snums) == 3993
