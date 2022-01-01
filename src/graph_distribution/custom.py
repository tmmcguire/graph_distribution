import numpy as np
from .dice import *

def scrud(n, m, s):
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
    data = np.array([
        scrud(n, m, s)
        for _ in range(0, r)
    ])
    return data
