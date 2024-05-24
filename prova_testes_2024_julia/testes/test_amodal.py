import pytest
from stat_funcs import StatsN2

@pytest.mark.amodal
@pytest.mark.parametrize("lista, expected", [
    ([1, 2, 3, 4, 5], "Não existe moda"),
    ([1, 1, 1, 1, 1], "Existe moda"),
])
def test_amodal(lista, expected):
    assert StatsN2.amodal(lista) == expected

@pytest.mark.amodal
@pytest.mark.xfail
def test_amodal_fail():
    assert StatsN2.amodal([]) == "Existe moda"
