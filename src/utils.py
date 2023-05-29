from numpy import array, zeros, uint8
from random import randint, choices
import webcolors
import os


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


def rgb_to_hex(rgb) -> str:
    return str(webcolors.rgb_to_hex(rgb))


def make_data_directory():
    os.chdir("..")
    cwd = os.getcwd()
    the_path = os.path.join(cwd, "data")
    is_data_directory_not_exists = not(os.path.exists(the_path))
    if is_data_directory_not_exists:
        os.mkdir(the_path)
    os.chdir("./src")


def yes_or_no(yes_probability) -> bool:
    no_probability = 1 - yes_probability
    return bool(choices([True, False], weights=[yes_probability, no_probability])[0])
