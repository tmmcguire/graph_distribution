from numpy.random import default_rng
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import uniform, norm, lognorm

def roll_ndice(n, r, s):
    """
    Roll n dice with s sides, summing the results, r times.

    Returns an array of length r containing the values.
    """
    data = default_rng().integers(1, s+1, r)
    for _ in range(1, n):
        data = data + default_rng().integers(1, s+1, r)
    return data

def roll_nd6(n, r):
    """
    Roll n 6-sided dice, summing the results, r times.

    Returns an array of length r containing the values.
    """
    return roll_ndice(n, r, 6)

