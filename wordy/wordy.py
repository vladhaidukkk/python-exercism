import re
from enum import Enum


def _parse_question(question):
    if not re.match(r"What", question, re.IGNORECASE):
        raise ValueError("unknown operation")

    question_match = re.match(r"What is (?P<op>.+)\?", question, re.IGNORECASE)
    if not question_match:
        raise ValueError("syntax error")

    operation = question_match.group("op")
    args = []
    for chunk in operation.split():
        if chunk.isascii() and (
            chunk.isdigit() or (chunk[1:].isdigit() and chunk[0] in "+-")
        ):
            args.append(int(chunk))
        elif args and isinstance(args[-1], str):
            args[-1] = f"{args[-1]} {chunk}"
        else:
            args.append(chunk)
    return args


class Op(Enum):
    PLUS = "plus"
    MINUS = "minus"
    MULTIPLY = "multiplied by"
    DIVIDE = "divided by"


def answer(question):
    args = _parse_question(question)
    if not isinstance(args[0], int):
        raise ValueError("syntax error")

    res = args[0]
    for idx, op in enumerate(args[1::2]):
        if not isinstance(op, str):
            raise ValueError("syntax error")

        for operation in Op:
            if operation.value in op:
                break
        else:
            raise ValueError("unknown operation")

        next_num_idx = idx * 2 + 2
        if len(args) <= next_num_idx:
            raise ValueError("syntax error")
        next_num = args[next_num_idx]

        match op:
            case Op.PLUS.value:
                res += next_num
            case Op.MINUS.value:
                res -= next_num
            case Op.MULTIPLY.value:
                res *= next_num
            case Op.DIVIDE.value:
                res //= next_num
            case _:
                raise ValueError("syntax error")
    return res
