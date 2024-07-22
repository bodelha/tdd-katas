import pytest
from src.word_wrap import Wrapper

@pytest.fixture
def wrapper():
    return Wrapper()

@pytest.mark.parametrize("string, col_num, expected", [
    ("", 1, ""),
    ("word", 10, "word"),
    ("word", 2, "wo\nrd"),
    ("abcdefghij", 3, "abc\ndef\nghi\nj"),
    ("word word", 5, "word\nword"),
    ("word word", 6, "word\nword"),
    ("word word", 3, "wor\nd\nwor\nd"),
    ("word word", 4, "word\nword"),
    ("word word word", 11, "word word\nword"),
])
def test_wrapper_wrap(wrapper, string, col_num, expected):
    result = wrapper.wrap(string, col_num)
    assert result == expected
