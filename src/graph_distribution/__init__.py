import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, norm, lognorm

from . dice import *

def _possible_values(rolls):
    min = np.min(rolls)
    max = np.max(rolls)
    return np.array([i for i in range(min, max + 1)])

def _uniform_dist(rolls):
    min = np.min(rolls)
    max = np.max(rolls)
    ud = uniform(loc=min, scale=max-min)
    x = np.linspace(ud.ppf(0), ud.ppf(1), rolls.size)
    pdf = uniform.pdf(x, loc=min, scale=max) * rolls.size
    return x, pdf

def _normal_dist(rolls):
    mean = np.mean(rolls)
    sd = np.std(rolls)
    nd = norm(loc=mean, scale=sd)
    x = np.linspace(nd.ppf(0.01), nd.ppf(0.99), rolls.size)
    pdf = nd.pdf(x) * rolls.size
    return x, pdf

def _lognormal_dist(rolls):
    scale = np.exp(np.mean(np.log(rolls)))
    s = np.std(np.log(rolls))
    nd = lognorm(scale=scale, s=s)
    x = np.linspace(nd.ppf(0.001), nd.ppf(0.9999), rolls.size)
    pdf = nd.pdf(x) * rolls.size
    return x, pdf

def graph_rolls(rolls, shift=0):
    """
    Return a Matplotlib Figure with the annotated histogram of `rolls`.

    If `rolls` has zero elements, this function will throw an error. In
    this case, set `shift` to 1, which shifts all values up one. All 
    properties of the graph are preserved, but with each element one greater
    than it should be.

    The histogram includes a display of the probability distribution
    function for the following distributons corresponding to the data:

    * Uniform distribution

    * Normal distribution

    * Lognormal distrbution
    """
    rolls += shift
    bb = np.insert(_possible_values(rolls) + 0.5, 0, [0.0])
    hist, bins = np.histogram(rolls, bb)
    # Graph
    fig, ax = plt.subplots(1,1)
    ax.set_xlim([np.min(rolls) - 1, np.max(rolls) + 1])
    ax.set_ylim([0, np.max(hist) * 1.5])
    ax.yaxis.set_major_formatter(lambda y, pos: '{:2}%'.format(100 * y / rolls.size))
    if shift != 0:
        ax.set_xlabel('Shifted by %d' % shift)
    # Uniform distribution
    ux, updf = _uniform_dist(rolls)
    _ = ax.plot(ux, updf, 'r-', label='Uniform')
    # Normal Distribution
    nx, npdf = _normal_dist(rolls)
    _ = ax.plot(nx, npdf, 'g-', label='Normal')
    # Lognormal Distribution
    lx, lpdf = _lognormal_dist(rolls)
    _ = ax.plot(lx, lpdf, 'b-', label='Lognormal')
    # Histogram
    _ = ax.bar(_possible_values(rolls), hist, align='center', width = 0.7, label = 'Rolls')
    _ = ax.legend(loc='best')
    return fig
