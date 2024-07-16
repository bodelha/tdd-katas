import pytest

from src.mult_tap_keypad import count_button_presses


def test_Return3IfRPassedIn():
    result = count_button_presses("R")
    assert result == 3


def test_Return4If3PassedIn():
    result = count_button_presses("3")
    assert result == 4


def test_Return6IfABCPassedIn():
    result = count_button_presses("ABC")
    assert result == 6


def test_Return47IfABCPassedIn():
    result = count_button_presses("WHERE DO U WANT 2 MEET L8R")
    assert result == 47


def test_Return6IfAbcPassedIn():
    result = count_button_presses("Abc")
    assert result == 6


def test_Return8IfPassedIn():
    result = count_button_presses("A*b#c")
    assert result == 8
