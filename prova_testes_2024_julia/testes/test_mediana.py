import pytest
from stat_funcs import StatsN2

@pytest.mark.mediana
@pytest.mark.parametrize("lista, expected", [
    ([1, 2, 3, 4, 5], 3),
    ([1, 1, 1, 1, 1], 1),
    ([1, 2, 2, 2, 5], 2),
])
def test_mediana(lista, expected):
    assert StatsN2.mediana(lista) == expected

@pytest.mark.mediana
@pytest.mark.xfail
def test_mediana_fail():
    assert StatsN2.mediana([]) == 1.0
