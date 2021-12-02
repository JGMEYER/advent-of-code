from day2 import Submarine, AimSubmarine


def test_process_cmd_strs():
    submarine = Submarine()
    cmd_strs = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]
    submarine.process_cmd_strs(cmd_strs)
    assert submarine.horiz_pos == 15
    assert submarine.depth == 10


def test_process_cmd_strs_with_aim():
    submarine = AimSubmarine()
    cmd_strs = [
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2",
    ]
    submarine.process_cmd_strs(cmd_strs)
    assert submarine.horiz_pos == 15
    assert submarine.depth == 60
