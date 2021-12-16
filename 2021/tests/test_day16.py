from day16 import (
    _parse_input,
    hex_str_to_bin_str,
    LiteralPacket,
    OperatorPacket,
    MessageParser,
)
from common.input import auto_read_input


def test__parse_input():
    ## Start here
    msg = _parse_input(auto_read_input())
    assert msg == "test input"


def test_hex_str_to_bin_str():
    msg = "D2FE28"
    bin_str = hex_str_to_bin_str(msg)
    assert bin_str == "110100101111111000101000"

    msg = "38006F45291200"
    bin_str = hex_str_to_bin_str(msg)
    assert (
        bin_str == "00111000000000000110111101000101001010010001001000000000"
    )

    msg = "EE00D40C823060"
    bin_str = hex_str_to_bin_str(msg)
    assert (
        bin_str == "11101110000000001101010000001100100000100011000001100000"
    )


def test_MessageParser_parse():
    # Simple case, i.e. packet literal
    packet = MessageParser.parse("D2FE28")
    assert packet == LiteralPacket(6, 4, 2021)
    version_sum = packet.sum_version()
    assert version_sum == 6

    packet = MessageParser.parse("8A004A801A8002F478")
    version_sum = packet.sum_version()
    assert version_sum == 16

    packet = MessageParser.parse("620080001611562C8802118E34")
    version_sum = packet.sum_version()
    print(packet)
    assert version_sum == 12

    packet = MessageParser.parse("C0015000016115A2E0802F182340")
    version_sum = packet.sum_version()
    assert version_sum == 23

    packet = MessageParser.parse("A0016C880162017C3686B18A3D4780")
    version_sum = packet.sum_version()
    assert version_sum == 31


def test_OperatorPacket_value():
    packet = MessageParser.parse("C200B40A82")
    assert packet.value == 3

    packet = MessageParser.parse("04005AC33890")
    assert packet.value == 54

    packet = MessageParser.parse("880086C3E88112")
    assert packet.value == 7

    packet = MessageParser.parse("CE00C43D881120")
    assert packet.value == 9

    packet = MessageParser.parse("D8005AC2A8F0")
    assert packet.value == 1

    packet = MessageParser.parse("F600BC2D8F")
    assert packet.value == 0

    packet = MessageParser.parse("9C005AC2F8F0")
    assert packet.value == 0

    packet = MessageParser.parse("9C0141080250320F1802104A08")
    assert packet.value == 1
