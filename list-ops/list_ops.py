def append(list1, list2):
    return list1 + list2


def concat(lists):
    return [item for list in lists for item in list]


def filter(function, list):
    return [item for item in list if function(item)]


def length(list):
    length = 0
    for _ in list:
        length += 1
    return length


def map(function, list):
    return [function(item) for item in list]


def foldl(function, list, initial):
    res = initial
    for item in list:
        res = function(res, item)
    return res


def foldr(function, list, initial):
    res = initial
    for item in list[::-1]:
        res = function(res, item)
    return res


def reverse(list):
    res = []
    for item in list:
        res = [item] + res
    return res
