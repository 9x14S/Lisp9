#!/usr/bin/python3

import operator
import sys

# TODO: define and set up runtime library
OPERATIONS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}

def print_usage(progname: str) -> None:
    print(
        f"usage: {progname} <lisp expr>", file=sys.stderr
    )

sexpr: str = ''

def pop():
    global sexpr
    sexpr = sexpr[1:]

def eval_sexpr() -> int:
    global sexpr
    # Assume it is well-formatted for now and that it is an expr of the like:
    # + 2 4

    if sexpr[0] == '(':
        pop()
        return eval_sexpr()

    if sexpr[0] in OPERATIONS:
        op = OPERATIONS[sexpr[0]]
        pop()
        pop() # Space
    else:
        raise ValueError(f"No operation '{sexpr[0]}'")

    if sexpr[0] == '(':
        pop()
        arg1 = eval_sexpr()
        pop() # Space
    else:
        arg1 = int(sexpr[0])
        pop()
        pop() # Space

    if sexpr[0] == '(':
        pop()
        arg2 = eval_sexpr()
        pop() # Space
    else:
        arg2 = int(sexpr[0])
        pop()

    if sexpr[0] == ')':
        pop()
    return op(int(arg1), int(arg2))


def main(argv: list[str]) -> int:
    global sexpr
    if len(argv) != 2:
        print_usage(argv[0])
        return 1
    sexpr = argv[1]
    print(f"Result: {eval_sexpr()}");
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
