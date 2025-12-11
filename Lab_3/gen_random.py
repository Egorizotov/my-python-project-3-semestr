from random import randint


def Gen_random(amount, min_value, max_value):
    return [randint(min_value, max_value) for _ in range(amount)]
