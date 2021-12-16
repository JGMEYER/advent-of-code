from abc import ABC
from enum import Enum
from functools import reduce
from typing import List

from common.input import auto_read_input


def hex_str_to_bin_str(msg):
    msg_bin_length = len(msg) * 4
    # Ensure we maintain leading zeroes
    return (bin(int(msg, 16))[2:]).zfill(msg_bin_length)


def to_bin_str(msg):
    return bin(int(msg, 16))[2:]


def bin_str_to_int(msg):
    return int(msg, 2)


class Packet(ABC):
    class Type(Enum):
        SUM = 0
        PROD = 1
        MIN = 2
        MAX = 3
        LITERAL = 4
        GT = 5
        LT = 6
        EQ = 7

    def __init__(self, version, type_id):
        self.version = version
        self.type_id = type_id

    def __eq__(self, other):
        if not isinstance(other, Packet):
            return NotImplemented
        return self.version == other.version and self.type_id == other.type_id

    def sum_version(self):
        return self.version


# NOTE: Definitely a strange construction considering Packet.Type. This is a
# side effect of only having partial information in part 1, so I'm keeping it
# in to explain how I arrived there. Ideally there may only be one Packet
# object.
class LiteralPacket(Packet):
    def __init__(self, version, type_id, value):
        super().__init__(version, type_id)
        self.value = value

    def __repr__(self):
        return f"LiteralPacket(version={self.version}, type_id={self.type_id}, value={self.value})"

    def __eq__(self, other):
        if not isinstance(other, LiteralPacket):
            return NotImplemented
        return super().__eq__(other) and self.value == other.value


class OperatorPacket(Packet):
    def __init__(self, version, type_id):
        super().__init__(version, type_id)
        self.subpackets: List[Packet] = []

    def __repr__(self):
        return f"OperatorPacket(version={self.version}, type_id={self.type_id}, subpackets={self.subpackets})"

    def __eq__(self, other):
        if not isinstance(other, LiteralPacket):
            return NotImplemented
        return super().__eq__(other) and self.subpackets == other.subpackets

    @property
    def value(self):
        if self.type_id == Packet.Type.SUM.value:
            return sum((p.value for p in self.subpackets))
        elif self.type_id == Packet.Type.PROD.value:
            return reduce(
                lambda x, y: x * y, [p.value for p in self.subpackets]
            )
        elif self.type_id == Packet.Type.MIN.value:
            return min((p.value for p in self.subpackets))
        elif self.type_id == Packet.Type.MAX.value:
            return max((p.value for p in self.subpackets))
        elif self.type_id == Packet.Type.GT.value:
            return int(self.subpackets[0].value > self.subpackets[1].value)
        elif self.type_id == Packet.Type.LT.value:
            return int(self.subpackets[0].value < self.subpackets[1].value)
        elif self.type_id == Packet.Type.EQ.value:
            return int(self.subpackets[0].value == self.subpackets[1].value)

    def sum_version(self):
        return self.version + sum((p.sum_version() for p in self.subpackets))

    def add_subpacket(self, packet: Packet):
        self.subpackets.append(packet)


class MessageParser:
    @classmethod
    def _read_bin_str(cls, bin_str, cursor, n_bits):
        next_cursor = cursor + n_bits
        return next_cursor, bin_str[cursor:next_cursor]

    @classmethod
    def _read_int(cls, bin_str, cursor, n_bits):
        next_cursor = cursor + n_bits
        return next_cursor, int(bin_str[cursor:next_cursor], 2)

    @classmethod
    def _parse_literal(cls, bin_str, version, type_id, cursor):
        value_bin_str = ""
        keep_parsing = True

        while keep_parsing:
            cursor, value_segment = cls._read_bin_str(bin_str, cursor, 5)
            keep_parsing = int(value_segment[0]) == 1
            value_bin_str += value_segment[1:]

        value = bin_str_to_int(value_bin_str)
        return cursor, LiteralPacket(version, type_id, value)

    @classmethod
    def _parse_operator(cls, bin_str, version, type_id, cursor):
        cursor, length_type_id = cls._read_int(bin_str, cursor, 1)
        operator_packet = OperatorPacket(version, type_id)

        if length_type_id == 0:
            cursor, subpackets_bit_len = cls._read_int(bin_str, cursor, 15)
            subpackets_end_idx = cursor + subpackets_bit_len

            while cursor < subpackets_end_idx:
                cursor, subpacket = cls._parse(bin_str, cursor)
                operator_packet.add_subpacket(subpacket)

        else:
            cursor, num_subpackets = cls._read_int(bin_str, cursor, 11)
            for _ in range(num_subpackets):
                cursor, subpacket = cls._parse(bin_str, cursor)
                operator_packet.add_subpacket(subpacket)

        return cursor, operator_packet

    @classmethod
    def _parse(cls, bin_str, cursor=0):
        cursor, version = cls._read_int(bin_str, cursor, 3)
        cursor, type_id = cls._read_int(bin_str, cursor, 3)

        if type_id == Packet.Type.LITERAL.value:
            cursor, packet = cls._parse_literal(
                bin_str, version, type_id, cursor
            )
        else:
            cursor, packet = cls._parse_operator(
                bin_str, version, type_id, cursor
            )

        return cursor, packet

    @classmethod
    def parse(cls, msg_hex_str):
        bin_str = hex_str_to_bin_str(msg_hex_str)
        _, packet = cls._parse(bin_str)
        return packet


def _parse_input(lines):
    ## Start here
    msg = lines[0]
    return msg


def part1():
    msg = _parse_input(auto_read_input())
    packet = MessageParser.parse(msg)
    return packet.sum_version()


def part2():
    msg = _parse_input(auto_read_input())
    packet = MessageParser.parse(msg)
    return packet.value


if __name__ == "__main__":
    print(part1())
    print(part2())
