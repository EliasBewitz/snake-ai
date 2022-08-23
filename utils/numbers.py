import math


def special_round(special_number: float, special_decimals: int = 0):
    """
    Round a number to a certain number of decimals.
    """
    if special_number is math.nan:
        return math.nan

    return round(number=special_number)
