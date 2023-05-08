from numpy import array, zeros, uint8
from random import randint


def clamp(x, a, b) -> int:
    return int(max(a, min(x, b)))


def combine(a, b) -> array:
    l = a.shape[0]
    l_1 = b.shape[0]
    result = zeros(l + l_1, dtype=uint8)

    for i in range(l):
        result[i] = a[i]
    for i in range(l_1):
        result[l - 1 + i] = b[i]
    return result


def generateBinaryArray(n) -> array:
    a = zeros(n, dtype=uint8)
    for i in range(n):
        a[i] = randint(0, 1)
    return a


def generateTwoDifferentNumbers(a=0, b=1) -> list:
    n_0 = randint(a, b)
    n_1 = randint(a, b)
    while(n_1 == n_0):
        n_1 = randint(a, b)
    return list([n_0, n_1])
