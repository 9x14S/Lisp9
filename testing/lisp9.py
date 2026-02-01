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

def eval_sexpr() -> int:
    global sexpr
    result: int = 0
    if sexpr.startswith('('):
        sexpr = sexpr[1:]
        return eval_sexpr()
    # Assume it is well-formatted for now and that it is an expr of the like:
    # + 2 4
    if sexpr[0] in OPERATIONS:
        op = OPERATIONS[sexpr[0]]
        arg1 = sexpr[2]
        arg2 = sexpr[4]
        result = op(int(arg1), int(arg2))
        sexpr = sexpr[5:]
    else:
        result = int(sexpr[0])
    if sexpr[0] == ')':
        sexpr = sexpr[1:]
    return result

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
