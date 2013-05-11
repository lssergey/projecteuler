"""
Solution for the 5th problem of ProjectEuler
http://projecteuler.net/problem=5

Use Python 3, feel da power!
"""

from collections import Counter
from functools import reduce
from itertools import starmap
from operator import mul, pow


def multipliers(n):
    """
    Not optimized algorithm, it works for low numbers.
    It wasn't tested on bigger ones.

    Example:
    if n == 36:
        return Counter({2: 2, 3: 2})

    @param n: integer
    @return Counter
    """
    
    muls = Counter()
    x = n
    d = 2

    while d < n/2 + 1:
        if x % d == 0:
            muls[d] += 1
            x = x/d
        else:
            d += 1

    # We've got a prime number
    if not muls:
        muls[n] += 1

    return muls


def lcm(numbers):
    """
    Least common multiple

    @param numbers: list of integers
    @return integer
    """

    lcm_powers = reduce(
        # Counter({2: 1, 3: 7}) | Counter({2: 5, 3: 3}) == Counter({2: 5, 3: 7})
        lambda acc, next_number: acc | multipliers(next_number),
        numbers,
        Counter())

    return reduce(mul, starmap(pow, lcm_powers.items()))


if __name__ == '__main__':
    print(lcm(range(1, 21)))
