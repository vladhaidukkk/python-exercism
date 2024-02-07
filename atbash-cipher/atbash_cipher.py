from string import ascii_lowercase

ENCODING = str.maketrans(ascii_lowercase, ascii_lowercase[::-1])


def encode(plain_text):
    res = "".join(char for char in plain_text.lower() if char.isalnum()).translate(
        ENCODING
    )
    return " ".join(res[i : i + 5] for i in range(0, len(res), 5))


def decode(ciphered_text):
    return "".join(char for char in ciphered_text.lower() if char.isalnum()).translate(
        ENCODING
    )
