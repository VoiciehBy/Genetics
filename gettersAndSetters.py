from objects import horses
from horse import horse

global first_parent_id
global second_parent_id

global first_parent
global second_parent

first_parent = horses[0]
second_parent = horses[1]


def setFirstParent(g_object):
    global first_parent
    first_parent = g_object


def setSecondParent(g_object):
    global second_parent
    second_parent = g_object


def setFirstParentId(i):
    global first_parent_id
    first_parent_id = i


def setSecondParentId(i):
    global second_parent_id
    second_parent_id = i


def getFirstParent() -> horse:
    global first_parent
    return first_parent


def getSecondParent() -> horse:
    global second_parent
    return second_parent


def getFirstParentId() -> int:
    global first_parent_id
    return int(first_parent_id)


def getSecondParentId() -> int:
    global second_parent_id
    return int(second_parent_id)
