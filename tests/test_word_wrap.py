import pytest
from src.word_wrap import Wrapper

@pytest.fixture
def wrapper():
    return Wrapper()

def test_case_3(wrapper):
    string = ""
    col_num = 1
    expected = ""
    result = wrapper.wrap(string, col_num)
    assert result == expected

def test_case_4(wrapper):
    string = "word"
    col_num = 10
    expected = "word"
    result = wrapper.wrap(string, col_num)
    assert result == expected

def test_case_5(wrapper):
    string = "word"
    col_num = 2
    expected = "wo\nrd"
    result = wrapper.wrap(string, col_num)
    assert result == expected

def test_case_6(wrapper):
    string = "abcdefghij"
    col_num = 3
    expected = "abc\ndef\nghi\nj"
    result = wrapper.wrap(string, col_num)
    assert result == expected

def test_case_7(wrapper):
    string = "word word"
    col_num = 5
    expected = "word\nword"
    result = wrapper.wrap(string, col_num)
    assert result == expected

# def test_case_8(wrapper):
#     string = "word word"
#     col_num = 6
#     expected = "word\nword"
#     result = wrapper.wrap(string, col_num)
#     assert result == expected


# def test_case_9(wrapper):
#     string = "word word"
#     col_num = 3
#     expected = "wor\nd\nwor\nd"
#     result = wrapper.wrap(string, col_num)
#     assert result == expected

# def test_case_10(wrapper):
#     string = "word word"
#     col_num = 4
#     expected = "word\nword"
#     result = wrapper.wrap(string, col_num)
#     assert result == expected

# def test_case_(wrapper):
#     string = "word word word"
#     col_num = 11
#     expected = "word word\nword"
#     result = wrapper.wrap(string, col_num)
#     assert result == expected

