from mypython.module import calc_module

_two_multiplayer = calc_module.multiplyer(2)
_add_five = calc_module.adder(5)
_two_division = calc_module.division(2)


def multiply_by_two(num: int) -> int:
    return _two_multiplayer(num)


def start_by_five(num: int) -> int:
    return _add_five(num)


def _divide_by_two(num: int) -> int:
    return _two_division(num)
