from numpy.random import default_rng

def roll_dice(r, s):
    """
    Roll a dice with s sides r times.

    Returns an array of length r containing the rolls.
    """
    return default_rng().integers(1, s+1, r)

###=====================================

### Combine dice by addition. (The normal thing to do.)

def roll_ndice(n, r, s):
    """
    Roll n dice with s sides, summing the results, r times.

    Returns an array of length r containing the values.
    """
    data = roll_dice(r, s)
    for _ in range(1, n):
        data = data + roll_dice(r, s)
    return data

def roll_nd6(n, r):
    """
    Roll n 6-sided dice, summing the results, r times.

    Returns an array of length r containing the values.
    """
    return roll_ndice(n, r, 6)

###=====================================

### Combine dice by multiplication.

def mult_ndice(n, r, s):
    """
    Roll n dice with s sides, multiplying the results, r times.

    Returns an array of length r containing the values.
    """
    data = roll_dice(r, s)
    for _ in range(1, n):
        data = data * roll_dice(r, s)
    return data

def mult_nd6(n, r):
    """
    Roll n 6-sided dice, multiplying the results, r times.

    Returns an array of length r containing the values.
    """
    return mult_ndice(n, r, 6)

###=====================================

### Roll a single dice; if a high-value is rolled, roll again and add
### that value.

def cascade_dice(r, s):
    """Roll one s-sided dice r times.

    If the maximum value is rolled, roll again and add the maximum
    value. Repeat until no more max-values are rolled.

    Returns an array of length r containing the values.

    """
    data = roll_dice(r, s)
    for i in range(0, data.size):
        max = s
        while data[i] == max:
            data[i] += roll_dice(1, s)[0]
            max += s
    return data

def cascade_ndice(n, r, s):
    """
    Make n cascading s-sided dice rolls (see cascade_dice), adding the results, r times.

    Returns an array of length r containing the values.
    """
    data = cascade_dice(r, s)
    for _ in range(1, n):
        data = data + cascade_dice(r, s)
    return data

def cascade_nd6(n, r):
    """
    Make n cascading 6-sided dice rolls (see cascade_ndice), adding the results, r times.

    Returns an array of length r containing the values.
    """
    return cascade_ndice(n, r, 6)

###=====================================

### Successes: roll a dice greater than m

def successes(r, s, min=None):
    """
    Return r trials of (1 if value >= min) on s-sided dice.

    By default, min = s.
    """
    min = min if min is not None else s
    return (roll_dice(r, s) >= min) * 1

def success_ndice(n, r, s, min=None):
    """
    Return r trials of the number of successes on n s-sided dice.

    A success is greater than or equal to min, default s (the maximum number
    on a dice).
    """
    data = successes(r, s, min)
    for _ in range(1, n):
        data = data + successes(r, s, min)
    return data
