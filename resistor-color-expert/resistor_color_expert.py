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


def split_string_in_groups(string):
    reversed_string = string[::-1]
    groups = [reversed_string[i : i + 3] for i in range(0, len(reversed_string), 3)]
    result = [group[::-1] for group in groups]
    return result[::-1]


def resistor_label(colors):
    colors = [color.lower() for color in colors]

    num = "".join(str(COLORS[color]) for color in colors[:-2])
    if len(colors) > 2:
        zeros = COLORS[colors[-2]] * "0"
        tolerance = TOLERANCES[colors[-1]]
    else:
        zeros = ""
        tolerance = ""

    val = f"{num}{zeros}".lstrip("0") or "0"
    groups = split_string_in_groups(val)
    groups_n = len(groups)
    if len(groups) > 1:
        val = f"{groups[0]}.{''.join(groups[1:])}"
        val = val.rstrip("0")
        val = val.rstrip(".")

    if groups_n == 1:
        prefix = ""
    elif groups_n == 2:
        prefix = "kilo"
    elif groups_n == 3:
        prefix = "mega"
    else:
        prefix = "giga"

    if tolerance:
        return f"{val} {prefix}ohms ±{tolerance}%"
    else:
        return f"{val} {prefix}ohms"
