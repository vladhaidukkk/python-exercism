def response(hey_bob):
    hey_bob = hey_bob.strip()
    is_upper = hey_bob.isupper()
    is_question = hey_bob.endswith("?")

    if not hey_bob:
        return "Fine. Be that way!"
    if is_upper:
        return "Calm down, I know what I'm doing!" if is_question else "Whoa, chill out!"
    return "Sure." if is_question else "Whatever."
