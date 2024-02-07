MATCHING_BRACKETS = {
    "[": "]",
    "{": "}",
    "(": ")",
}
OPENING_BRACKETS = MATCHING_BRACKETS.keys()
CLOSING_BRACKETS = MATCHING_BRACKETS.values()

def is_paired(string):
    nesting = []
    
    for char in string:
        if char in OPENING_BRACKETS:
            nesting.append(char)
        elif char in CLOSING_BRACKETS:
            if nesting and char == MATCHING_BRACKETS[nesting[-1]]:
                nesting.pop()
            else:
                return False

    return not nesting
