from objects import first_parent, second_parent, first_parent_id, second_parent_id
from horse import horse


def setFirstParent(object):
    global first_parent
    first_parent = object


def setSecondParent(object):
    global second_parent
    second_parent = object


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
