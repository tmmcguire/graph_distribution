import numpy as np
from .dice import *

def scrud(n, m, s):
    """
    Return the result of using SCRUD on n s-sided dice with m s-sided dice.

    SCRUD is Simple Combat Resolution Using Dice. A negative result means
    the n rolls scores that many excess successes; positive means the m rolls
    score that many successes.
    """
    n_rolls = roll_dice(n, s)
    n_rolls.sort()
    m_rolls = roll_dice(m, s)
    m_rolls.sort()
    sum = 0
    for i in range(1, min(n, m) + 1):
        if n_rolls[-i] < m_rolls[-i]:
            sum += 1
        elif n_rolls[-i] > m_rolls[-i]:
            sum -= 1
    return sum

def roll_scrud(r, n, m, s):
    """
    Return the resuls on r trials of SCRUD comparing n rolls and m rolls
    of s-sided dice.

    SCRUD is Simple Combat Resolution Using Dice. A negative result means
    the n rolls scores that many excess successes; positive means the m rolls
    score that many successes.
    """
    data = np.array([ scrud(n, m, s) for _ in range(0, r) ])
    return data
