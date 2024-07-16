## Motivation ##

This repository is meant to contain code produced in TDD study sessions.


## Problems ##

#### Multi-tap Keypad Text Entry on an Old Mobile Phone ####

> From [codewars] (https://www.codewars.com/kata/multi-tap-keypad-text-entry-on-an-old-mobile-phone/python)


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

> Test cases:
> 1. Can call mult tap class (x)
> 2. If "R" is passed in, the amount of button *presses is 3
> 3. If "3" is passed in, the amount of button presses is 4
> 4. If "ABC" is passed in, the amount of button presses is 6
> 5. If "WHERE DO U WANT 2 MEET L8R" is passed in, the amount of button presses is 47