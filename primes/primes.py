import math

from ..utils import rotations

def is_prime(n):
    """
        Simple but fairly quick primality checker.
    """
    if n == 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**(1/2) + 1), 2):
        if n % i == 0:
            return False    

    return True


def primes(index_range=None, int_range=None):
    """
        Generates all primes, by default. Can also generate primes within a
        given index range (e.g. the first 50 primes, or the 20th to the 50th
        primes) by using the 'index_range' option, or a given interval for
        the primes (e.g. primes between 100 and 1000) by using the
        'int_range' option.
    """    
    if index_range:
        n = 2
        i = 1
        while i not in index_range:
            if is_prime(n):
                i += 1
            n += 1
        while i in index_range:
            if is_prime(n):
                yield n
                i += 1
            n += 1
        return
    elif int_range:
        for n in int_range:
            if is_prime(n):
                yield n
        return

    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


def prime_factors(n, multiplicities=False):
    """
        Generates the distinct prime factors of a positive integer n in an
        ordered sequence. If the 'multiplicities' option is True then it
        generates pairs of prime factors of n and their multiplicities
        (highest p-power dividing n for a given prime factor p), e.g. for
        n = 54 = 2^1 x 3^3 we have

            54 -> 2, 3
            54, multiplicities=True -> (2, 1), (3, 3)

        This is precisely the prime factorisation of n.
    """
    if n == 1:
        return

    if is_prime(n):
        if not multiplicities:
            yield n
        else:
            yield n, 1
        return

    pf = (p for p in primes(int_range=range(2, math.ceil(math.sqrt(n)))) if n % p == 0)
    if not multiplicities:
        for p in pf:
            yield p
    else:
        pfm = ((p, max(e for e in reversed(range(1, math.ceil(math.log(n, p)))) if n % p**e == 0)) for p in pf)
        for p, m in pfm:
            yield p, m


def is_circular_prime(n):
    """
        A circular prime p satisfies the property that all (right) rotations of
        its digits yield primes also, e.g. 197 is a prime whose rotations 719
        and 971 are also primes.
    """
    if any(not is_prime(rot) for rot in rotations(n)):
        return False
    return True


def circular_primes(ubound):
    """
        Generates the sequence of all circular primes below a given upper
        bound.
    """
    for n in range(1, ubound):
        if is_circular_prime(n):
            yield n