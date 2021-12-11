from collections import defaultdict
from typing import List

from common.input import auto_read_input

# NOTE: This one got gross. Absolutely not cleaned up. Just bruteforces the
# solution after removing some possible solutions by narrowing down the "easy"
# digits. I kept procrastinating on this one, but really wanted the gold star.
# Hey, it runs quickly and is correct. What more could you want?


class SignalMap:
    DEFAULT_DIGIT_TO_SIGNAL_PATTERNS = {
        0: set("abcefg"),
        1: set("cf"),
        2: set("acdeg"),
        3: set("acdfg"),
        4: set("bdcf"),
        5: set("abdfg"),
        6: set("abdefg"),
        7: set("acf"),
        8: set("abcdefg"),
        9: set("abcdfg"),
    }

    # segments: digit
    UNIQUE_SEGMENT_COUNTS = {2: 1, 4: 4, 3: 7, 7: 8}

    def __init__(self):
        self._new_signal_patterns_to_digit = None
        self._possible_maps = {
            # {default: new}
            "a": {"a", "b", "c", "d", "e", "f", "g"},
            "b": {"a", "b", "c", "d", "e", "f", "g"},
            "c": {"a", "b", "c", "d", "e", "f", "g"},
            "d": {"a", "b", "c", "d", "e", "f", "g"},
            "e": {"a", "b", "c", "d", "e", "f", "g"},
            "f": {"a", "b", "c", "d", "e", "f", "g"},
            "g": {"a", "b", "c", "d", "e", "f", "g"},
        }
        self._digit_to_confirmed_pattern = {digit: None for digit in range(10)}

    def is_mapped(self):
        return bool(self._new_signal_patterns_to_digit)

    def _could_map_to(self, signal_pattern, num):
        for sig in signal_pattern:
            self._used_in_digit[sig].add(num)

    def _narrow_for_given(self, pattern, digit):
        for sig in self.DEFAULT_DIGIT_TO_SIGNAL_PATTERNS[digit]:
            self._possible_maps[sig] = self._possible_maps[sig].intersection(
                pattern
            )

    def map(self, signal_patterns):
        # Get easy ones out of the way
        for pat in signal_patterns:
            easy_digit = SignalMap.UNIQUE_SEGMENT_COUNTS.get(len(pat))
            if easy_digit:
                self._digit_to_confirmed_pattern[easy_digit] = pat
                self._narrow_for_given(pat, easy_digit)

        # HACK: I give up
        def bruteforce(sig_idx=0, cur_map={}):
            if sig_idx >= 7:
                new_signal_patterns_to_digit = {}
                for (
                    digit,
                    default_pat,
                ) in self.DEFAULT_DIGIT_TO_SIGNAL_PATTERNS.items():
                    new_pat = set()
                    for sig in default_pat:
                        new_pat.add(cur_map[sig])
                    new_signal_patterns_to_digit[
                        tuple(sorted(list(new_pat)))
                    ] = digit

                for pat in signal_patterns:
                    if (
                        tuple(sorted(list(pat)))
                        not in new_signal_patterns_to_digit
                    ):
                        return None

                return new_signal_patterns_to_digit

            default_sig = "abcdefg"[sig_idx]

            remaining_new_sigs = self._possible_maps[default_sig] - set(
                cur_map.values()
            )

            for new_sig in remaining_new_sigs:
                map = cur_map.copy()
                map[default_sig] = new_sig
                working_map = bruteforce(sig_idx + 1, map)
                if working_map is not None:
                    return working_map

            return None

        self._new_signal_patterns_to_digit = bruteforce()

    def decode_output(self, output_value: List[str]):
        if not self.is_mapped():
            raise Exception("Must first map")

        decoded_output = []
        for encoded_digit in output_value:
            decoded_output.append(
                self._new_signal_patterns_to_digit[
                    tuple(sorted(encoded_digit))
                ]
            )

        return decoded_output


class SubmarineDisplay:
    def __init__(self, signal_patterns, output_value):
        self._signal_patterns = signal_patterns
        self._output_value = output_value
        self.signal_map = SignalMap()

    def __repr__(self):
        return f"signal_patterns: {self._signal_patterns}, output_value: {self._output_value}"

    def num_easy_outputs(self):
        num = 0
        for digit in self._output_value:
            num_segments = len(digit)
            if num_segments in [2, 4, 3, 7]:  # i.e. digits 1, 4, 7, 8
                num += 1
        return num

    def decode_outputs(self):
        if not self.signal_map.is_mapped():
            self.signal_map.map(self._signal_patterns)
        decoded_output = self.signal_map.decode_output(self._output_value)
        return sum(
            [
                digit * 10 ** (len(decoded_output) - idx - 1)
                for idx, digit in enumerate(decoded_output)
            ]
        )


def _parse_input(lines):
    ## Start here
    displays = []

    for line in lines:
        signal_patterns_str, output_value_str = line.split(" | ")
        signal_patterns = [
            set(pat_str) for pat_str in signal_patterns_str.split(" ")
        ]
        output_value = output_value_str.split(" ")
        display = SubmarineDisplay(signal_patterns, output_value)
        displays.append(display)

    return displays


def part1():
    displays = _parse_input(auto_read_input())
    return sum([d.num_easy_outputs() for d in displays])


def part2():
    displays = _parse_input(auto_read_input())
    return sum([d.decode_outputs() for d in displays])


if __name__ == "__main__":
    print(part1())
    print(part2())
