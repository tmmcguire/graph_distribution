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

