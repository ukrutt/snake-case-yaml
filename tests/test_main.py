"""Sample test file."""

from snake_case_yaml import main


def test_add_two():
    """Sample test routine."""
    arg_x = 2
    arg_y = 3
    ans_z = main.add_two(arg_x, arg_y)
    assert ans_z == 5
