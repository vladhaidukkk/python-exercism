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


def value(colors):
    a = COLORS[colors[0].lower()]
    b = COLORS[colors[1].lower()]
    return int(f"{a}{b}")
