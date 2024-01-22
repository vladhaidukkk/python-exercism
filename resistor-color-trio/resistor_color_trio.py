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


def label(colors):
    val = "{}{}{}".format(
        COLORS[colors[0].lower()],
        COLORS[colors[1].lower()],
        COLORS[colors[2].lower()] * "0",
    )
    val = val.lstrip("0") or "0"
    zeros_n = val.count("0")
    val = val.replace(zeros_n // 3 * "000", "")

    if 0 <= zeros_n <= 2:
        prefix = ""
    elif 3 <= zeros_n <= 5:
        prefix = "kilo"
    elif 6 <= zeros_n <= 8:
        prefix = "mega"
    else:
        prefix = "giga"

    return f"{val} {prefix}ohms"
