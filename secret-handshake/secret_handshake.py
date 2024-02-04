def commands(binary_str):
    actions = []

    for i, digit in enumerate(reversed(binary_str)):
        if digit != "1":
            continue

        if i == 0:
            actions.append("wink")
        elif i == 1:
            actions.append("double blink")
        elif i == 2:
            actions.append("close your eyes")
        elif i == 3:
            actions.append("jump")
        elif i == 4:
            actions.reverse()

    return actions
