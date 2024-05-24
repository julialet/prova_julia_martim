import pytest
from stat_funcs import StatsN2

@pytest.mark.unimodal
@pytest.mark.parametrize("lista, expected", [
    ([1, 2, 2, 3, 4], 2),
    ([1, 1, 1, 1, 1], 1),
])
def test_unimodal(lista, expected):
    assert StatsN2.unimodal(lista) == expected

@pytest.mark.unimodal
@pytest.mark.xfail
def test_unimodal_fail():
    assert StatsN2.unimodal([]) == 1
