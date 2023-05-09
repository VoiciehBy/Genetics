from objects import horses
from horse import horse

first_parent = horses[0]
second_parent = horses[1]


def set_first_parent(g_object):
    global first_parent
    first_parent = g_object


def set_second_parent(g_object):
    global second_parent
    second_parent = g_object


def get_first_parent() -> horse:
    return first_parent


def get_second_parent() -> horse:
    return second_parent
