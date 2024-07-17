## Motivation ##

This repository is meant to contain code produced in TDD study sessions.


## Problems ##

#### Multi-tap Keypad Text Entry on an Old Mobile Phone ####

> From [codewars](https://www.codewars.com/kata/multi-tap-keypad-text-entry-on-an-old-mobile-phone/python)

```
------- ------- -------
|     | | ABC | | DEF |
|  1  | |  2  | |  3  |
------- ------- -------
------- ------- -------
| GHI | | JKL | | MNO |
|  4  | |  5  | |  6  |
------- ------- -------
------- ------- -------
|PQRS | | TUV | | WXYZ|
|  7  | |  8  | |  9  |
------- ------- -------
------- ------- -------
|  *  | |space| |  #  |
|     | |  0  | |     |
------- ------- -------
```

> **Test cases**:
> 1. Can call mult tap class (x)
> 2. If "R" is passed in, the amount of button *presses is 3
> 3. If "3" is passed in, the amount of button presses is 4
> 4. If "ABC" is passed in, the amount of button presses is 6
> 5. If "WHERE DO U WANT 2 MEET L8R" is passed in, the amount of button presses is 47


#### Word wrap ####

> From [codingdojo](https://codingdojo.org/kata/WordWrap/)

> **Description:** You write a class called Wrapper, that has a single static function named wrap that takes two arguments, a string, and a column number. The function returns the string, but with line breaks inserted at just the right places to make sure that no line is longer than the column number. You try to break lines at word boundaries.

Like a word processor, break the line by replacing the last space in a line with a newline.

> **Test cases**:
1. Can instantiate the Wrapper class
2. Can call the wrap method
3. assertThat(wrap("", 1), equalTo(""));
4. assertThat(wrap("word", 10), equalTo("word"));
5. assertThat(wrap("word", 2), equalTo("wo\nrd"))
6. assertThat(wrap("abcdefghij", 3), equalTo("abc\ndef\nghi\nj"));
7. assertThat(wrap("word word", 5), equalTo("word\nword"));
8. assertThat(wrap("word word", 6), equalTo("word\nword"));
9. assertThat(wrap("word word", 3), equalTo("wor\nd\nwor\nd"));
10. assertThat(wrap("word word", 4), equalTo("word\nword"));
