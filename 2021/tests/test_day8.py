from day8 import _parse_input, SignalMap, SubmarineDisplay
from common.input import auto_read_input


def test__parse_input():
    ## Start here
    displays = _parse_input(auto_read_input()[:2])
    assert displays[0]._signal_patterns == [
        set("be"),
        set("cfbegad"),
        set("cbdgef"),
        set("fgaecd"),
        set("cgeb"),
        set("fdcge"),
        set("agebfd"),
        set("fecdb"),
        set("fabcd"),
        set("edb"),
    ]
    assert displays[0]._output_value == ["fdgacbe", "cefdb", "cefbgd", "gcbe"]
    assert displays[1]._signal_patterns == [
        set("edbfga"),
        set("begcd"),
        set("cbg"),
        set("gc"),
        set("gcadebf"),
        set("fbgde"),
        set("acbgfd"),
        set("abcde"),
        set("gfcbed"),
        set("gfec"),
    ]
    assert displays[1]._output_value == ["fcgedb", "cgb", "dgebacf", "gc"]


def test_SignalMap_decode_signals():
    signal_map = SignalMap()
    signal_patterns = [
        set("acedgfb"),
        set("cdfbe"),
        set("gcdfa"),
        set("fbcad"),
        set("dab"),
        set("cefabd"),
        set("cdfgeb"),
        set("eafb"),
        set("cagedb"),
        set("ab"),
    ]
    signal_map.map(signal_patterns)


def test_SubmarineDisplay_decode_outputs():
    displays = _parse_input(
        [
            "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
            "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
            "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
            "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
            "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
            "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
            "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
            "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
            "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
            "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
        ]
    )
    assert displays[0].decode_outputs() == 8394
    assert displays[1].decode_outputs() == 9781
    assert displays[2].decode_outputs() == 1197
    assert displays[3].decode_outputs() == 9361
    assert displays[4].decode_outputs() == 4873
    assert displays[5].decode_outputs() == 8418
    assert displays[6].decode_outputs() == 4548
    assert displays[7].decode_outputs() == 1625
    assert displays[8].decode_outputs() == 8717
    assert displays[9].decode_outputs() == 4315
