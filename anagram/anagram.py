from itertools import permutations


def find_anagrams(word, candidates):
    variants = [
        variant
        for permutation in permutations(word.lower(), len(word))
        if (variant := "".join(permutation)) != word.lower()
    ]
    return [candidate for candidate in candidates if candidate.lower() in variants]
