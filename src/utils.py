from numpy import array, zeros, uint8
from random import randint


def clamp(x, a, b) -> int:
    return int(max(a, min(x, b)))


def combine(a: array, b: array) -> array:
    a_length = a.shape[0]
    b_length = b.shape[0]
    result = zeros(a_length + b_length, dtype=uint8)

    for i in range(a_length):
        result[i] = a[i]
    for i in range(b_length):
        result[a_length - 1 + i] = b[i]
    return result


def generate_binary_array(n: int) -> array:
    a = zeros(n, dtype=uint8)
    for i in range(n):
        a[i] = randint(0, 1)
    return array(a)


def generate_two_different_numbers(a=0, b=1) -> list:
    n_0 = randint(a, b)
    n_1 = randint(a, b)
    while(n_1 == n_0):
        n_1 = randint(a, b)
    return list([n_0, n_1])
