phrases = [
    (None, "the horse and the hound and the horn"),
    ("belonged to", "the farmer sowing his corn"),
    ("kept", "the rooster that crowed in the morn"),
    ("woke", "the priest all shaven and shorn"),
    ("married", "the man all tattered and torn"),
    ("kissed", "the maiden all forlorn"),
    ("milked", "the cow with the crumpled horn"),
    ("tossed", "the dog"),
    ("worried", "the cat"),
    ("killed", "the rat"),
    ("ate", "the malt"),
    ("lay in", "the house that Jack built."),
]


def recite(start_verse, end_verse):
    return [
        " ".join(
            ("This is " if i == 0 else f"that {phrase[0]} ") + phrase[1]
            for i, phrase in enumerate(phrases[-start:])
        )
        for start in range(start_verse, end_verse + 1)
    ]
