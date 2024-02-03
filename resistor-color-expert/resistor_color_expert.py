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


def get_label_components(colors):
    if len(colors) < 3:
        num = "".join(str(COLORS[color]) for color in colors[:-1])
        zeros = ""
        tolerance = ""
    if len(colors) == 3:
        num = "".join(str(COLORS[color]) for color in colors[:-1])
        zeros = COLORS[colors[-1]] * "0"
        tolerance = ""
    elif len(colors) > 3:
        num = "".join(str(COLORS[color]) for color in colors[:-2])
        zeros = COLORS[colors[-2]] * "0"
        tolerance = TOLERANCES[colors[-1]]

    return f"{num}{zeros}".lstrip("0") or "0", tolerance


def split_val_in_groups(val):
    reversed_val = val[::-1]
    groups = [reversed_val[i : i + 3] for i in range(0, len(reversed_val), 3)]
    return [group[::-1] for group in groups][::-1]


def resistor_label(colors):
    val, tolerance = get_label_components([c.lower() for c in colors])
    groups = split_val_in_groups(val)

    if len(groups) > 1:
        val = f"{groups[0]}.{''.join(groups[1:])}".rstrip("0").rstrip(".")

    if len(groups) == 1:
        prefix = ""
    elif len(groups) == 2:
        prefix = "kilo"
    elif len(groups) == 3:
        prefix = "mega"
    else:
        prefix = "giga"

    if tolerance:
        return f"{val} {prefix}ohms ±{tolerance}%"
    else:
        return f"{val} {prefix}ohms"
