def multiplyer(by: int):
    return lambda x: by * x


def adder(start: int):
    return lambda y: start + y


def subtraction(start: int):
    return lambda y: start - y


def division(start: int):
    return lambda y: start / y
