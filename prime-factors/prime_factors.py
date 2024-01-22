from itertools import count


def get_next_factor(value):
    if value == 1:
        return None, value

    for divider in count(2):
        res = value / divider
        if res.is_integer():
            return divider, res


def factors(value):
    res = []
    while True:
        factor, value = get_next_factor(value)
        if factor is None:
            break
        res.append(factor)
    return res
