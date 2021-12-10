from typing import List


def read_file(filepath: str) -> List[str]:
    """Read a file"""
    with open(filepath) as f:
        return f.read().strip().split("\n")


def input_filepath(*, day: int, test: bool = False) -> str:
    """Returns paths to both question and test inputs"""
    return (
        f"tests/test_inputs/test_day{day}.txt"
        if test
        else f"inputs/day{day}.txt"
    )


def read_input(*, day: int, test: bool = False) -> List[str]:
    """Read the input file for a particular day"""
    import os
    import warnings

    warnings.warn(
        "read_input is deprecated, use auto_read_input instead",
        DeprecationWarning,
    )
    filepath = os.path.abspath(input_filepath(day=day, test=test))
    return read_file(filepath)


def read_test_input(*, day: int) -> List[str]:
    """Read the test input file for a particular day"""
    import os
    import warnings

    warnings.warn(
        "read_test_input is deprecated, use auto_read_input with test=False instead",
        DeprecationWarning,
    )
    filepath = os.path.abspath(input_filepath(day=day, test=True))
    return read_file(filepath)


def auto_read_input() -> List[str]:
    """Read the input file for a particular day based on the .py file invoking the function"""
    import inspect
    import re

    # This is generally probably a bad idea...
    filename = inspect.stack()[1].filename
    file_pattern = r"(test_)?day(\d+)\.py$"

    match = re.search(file_pattern, filename)
    if not match:
        raise Exception(
            f'Invoker filename {filename} must match pattern "{file_pattern}"'
        )

    groups = match.groups()
    test, day = bool(groups[0]), int(groups[1])

    filepath = input_filepath(day=day, test=test)
    return read_file(filepath)
