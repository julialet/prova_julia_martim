import pytest
from stat_funcs import StatsN2

@pytest.mark.variancia
@pytest.mark.parametrize("lista, expected", [
    ([1, 2, 2, 3, 3, 4], 1.1),
    ([1, 2, 3, 4, 5], 2.5),
])
def test_variancia(lista, expected):
    assert StatsN2.variancia(lista) == pytest.approx(expected)

@pytest.mark.variancia
@pytest.mark.xfail
def test_variancia_fail():
    assert StatsN2.variancia([]) == 1.0
