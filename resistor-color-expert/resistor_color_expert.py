import math

COLORS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

TOLERANCES = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}


def split_into_groups(lst, size):
    return


def resistor_label(colors):
    colors = [color.lower() for color in colors]

    num = "".join(str(COLORS[color]) for color in colors[:-2])
    zeros = COLORS[colors[-2]] * "0"
    tolerance = TOLERANCES[colors[-1]]

    val = f"{num}{zeros}".lstrip("0") or "0"
    groups_n = math.ceil(len(val) / 3)
    groups = [
        group for i in range(groups_n) if set(group := val[i * 3 : i + 3]) - set("0")
    ]

    if groups_n == 1:
        prefix = ""
    elif groups_n == 2:
        prefix = "kilo"
    elif groups_n == 3:
        prefix = "mega"
    else:
        prefix = "giga"

    return f"{val} {prefix}ohms ±{tolerance}%"
