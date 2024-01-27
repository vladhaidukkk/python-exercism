from itertools import product
from random import shuffle
from string import ascii_uppercase

names = [
    chars + code
    for chars, code in product(
        ("".join(p) for p in product(ascii_uppercase, ascii_uppercase)),
        (str(i).zfill(3) for i in range(1000)),
    )
]
shuffle(names)
NAMES = iter(names)


class Robot:
    def __init__(self):
        self.reset()

    def reset(self):
        self.name = next(NAMES)
