DAYS = (
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
)
PRESENTS = (
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
)


def recite(start_verse, end_verse):
    start_verse -= 1

    def format_presents(stop):
        ordered_presents = PRESENTS[0:stop][::-1]
        return (
            ordered_presents[0]
            if len(ordered_presents) == 1
            else ", ".join(ordered_presents[:-1]) + f", and {ordered_presents[-1]}"
        )

    return [
        (
            f"On the {DAYS[i]} day of Christmas my true love gave to me: "
            f"{format_presents(i + 1)}."
        )
        for i in range(start_verse, end_verse)
    ]