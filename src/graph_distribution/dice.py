from numpy.random import default_rng
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import uniform, norm, lognorm

def roll_nd6(n, rolls):
    data = default_rng().integers(1, 7, rolls)
    for _ in range(1, n):
        data = data + default_rng().integers(1, 7, rolls)
    return data
