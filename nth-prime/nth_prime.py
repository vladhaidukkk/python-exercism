from itertools import count
from math import floor, sqrt


def is_prime(number):
    for divider in range(2, floor(sqrt(number)) + 1):
        res = number / divider
        if res.is_integer():
            return False
    return True


def prime(number):
    if number < 1:
        raise ValueError("there is no zeroth prime")

    primes_count = 0
    for num in count(2):
        if not is_prime(num):
            continue
        primes_count += 1
        if primes_count == number:
            return num
