from itertools import count, islice
from math import sqrt


def nth(iterable, n):
    return next(islice(iterable, n, None))


def prime_generator():

    primes = [2]

    def is_prime(n):
        for prime in primes:
            if prime > sqrt(n):
                break

            if n % prime == 0:
                return False

        return True

    yield 2
    for i in count(3, 2):
        if is_prime(i):
            primes.append(i)
            yield i


def solve(n=10001):
    return nth(prime_generator(), n - 1)


if __name__ == '__main__':
    print(solve())