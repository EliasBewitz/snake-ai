import math

from utils.numbers import special_round


def test_numbers():
    assert special_round(special_number=1.5) == 2
    assert special_round(special_number=1.4) == 1
    assert special_round(special_number=1.6) == 2
    assert special_round(special_number=1.7) == 2
    assert special_round(special_number=1.8) == 2
    assert special_round(special_number=math.nan) is math.nan
