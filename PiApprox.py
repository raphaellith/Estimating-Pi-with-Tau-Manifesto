from math import sqrt, floor, ceil, isclose
from typing import Union
import functools

from Scraper import get_freq_ranking_dict
from Constants import BETA, LETTERS_IN_ALPHABET


def lerp(a, b, t):
    """
    Performs linear interpolation.
    """
    return a + (b - a) * t


@functools.cache
def freq(r: Union[int, float]):
    """
    A frequency function. See blog post.
    """
    if r < 1:
        raise ValueError(f"Cannot evaluate freq_function on r = {r}. " +
                         "The domain of freq_function is the set of all real numbers >= 1")

    freq_dict = get_freq_ranking_dict()

    if isinstance(r, int) or isclose(r, round(r)):  # if r is an integer
        r = round(r)
        return freq_dict[r]

    a = 1 / freq(floor(r))
    b = 1 / freq(ceil(r))
    t = r - floor(r)

    return 1/lerp(a, b, t)


def r_est(r: float):
    """
    A function that approximates the reciprocal of r.
    If r < 1 + BETA, this function directly returns the actual value of 1/r.
    """
    if r < 1 + BETA:
        return 1/r
    return freq(r - BETA) / ((1 + BETA) * freq(1))


def estimate_pi():
    """
    Approximates the value of pi.
    """
    partial_sum = 0

    for n in range(1, LETTERS_IN_ALPHABET + 1):
        partial_sum += (r_est(n)) ** 2

    pi_estimation = sqrt(6 * partial_sum)

    return pi_estimation


if __name__ == '__main__':
    print(estimate_pi())
