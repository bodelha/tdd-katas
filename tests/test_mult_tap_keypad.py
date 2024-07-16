import pytest
from src.mult_tap_keypad import count_button_presses


@pytest.mark.parametrize(
    "input_str, expected_presses",
    [
        ("R", 3),
        ("3", 4),
        ("ABC", 6),
        ("WHERE DO U WANT 2 MEET L8R", 47),
        ("Abc", 6),
        ("A*b#c", 8),
    ],
)
def test_count_button_presses(input_str, expected_presses):
    result = count_button_presses(input_str)
    assert result == expected_presses
